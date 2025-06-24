# OpenC3 COSMOS Ground Station

OpenC3 COSMOS is a cloud native, containerized, microservice oriented command and control system, enabling an all-in-one management platform. This repository will host the files and documentation required to build a custom ground station for a ghost satellite mission.

A few concepts are required to understand COSMOS. A short summary was written based on the [official documentation](https://docs.openc3.com/docs/configuration):

> - Plugins: how you configure and extend COSMOS. Plugins define targets, their communication properties, and configure the interfaces needed to talk to them. Each plugin is built as a Ruby gem and thus has a `plugin.gemspec` file which builds it. Plugins have a `plugin.txt` file which declares all the variables used by the plugin and how to interface to the target it contains.
>
> - Targets: external pieces of hardware and/or software that COSMOS communicates with. Targets can receive commands sent by COSMOS and respond with telemetry.
>
> - Commands: information sent to targets. They can come from a script (Script Runner), a tool like Command Sender, or just generally through an API call. The commands packets' structure is defined in the `cmd.txt`.
>
> - Telemetry: information received by targets. The system will log the raw packet, parse it to engineering values, and log the converted data. The telemetry packets' structure is defined in the `tlm.txt`.
> 
> - Interfaces: established connections to targets, enabling data transfer. They are defined by the top level INTERFACE keyword in the `plugin.txt` file. The interface could be TCP/IP, UDP, serial, MQTT, or custom ones.
>
> - Protocols: behaviour of an interface, including differentiating packet boundaries and modifying data as necessary. They are typically used to define the logic to delineate packets and manipulate data as it written to and read from interfaces.
>
> - Conversions: data manipulation functions. They can be applied to both command parameters and telemetry items to modify the values sent to and received from targets.

<br /> 

## Installing the required software

### Docker

All COSMOS microservices are docker containers, which is why Docker is the first package needed to be installed. Following the [Docker Engine installation guide for Ubuntu](https://docs.docker.com/engine/install/ubuntu/):

> 1. Set up Docker's `apt` repository:
>```bash
>user@machine ~
># Add Docker official GPG key
>$ sudo apt-get update
>$ sudo apt-get install ca-certificates curl
>$ sudo install -m 0755 -d /etc/apt/keyrings
>$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
>$ sudo chmod a+r /etc/apt/keyrings/docker.asc
>
># Add the repository to apt sources
>$ echo \
>  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
>  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
>  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
>$ sudo apt-get update
>```
>
> 2. Install the Docker packages:
>
>```bash
> user@machine ~
> $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
>```
>
> 3. Verify that the installation is successful by running the hello-world image:
>
>```bash
> user@machine ~
> $ sudo docker run hello-world
>```

<br />

Some extra steps are required to fully configure Docker Engine, such as [enabling Docker to be managed with a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user):

> 1. Create the docker group:
>
>```bash
> user@machine ~
> $ sudo groupadd docker
>```
>
> 2. Add your user to the docker group:
>
>```bash
> user@machine ~
> $ sudo usermod -aG docker $USER
>```
>
> 3. Activate the changes to groups. This command is necessary again once the shell is closed:
>
>```bash
> user@machine ~
> $ newgrp docker
>```
>
> 4. Verify that you can run docker commands without `sudo`:
>
>```bash
> user@machine ~
> $ docker run hello-world
>```

<br /> 

The Docker Compose is also required. Following its [appropriate tutorial](https://docs.docker.com/compose/install/linux/#install-using-the-repository):

> 1. Update the package index and install the latest version:
>
>```bash
> user@machine ~
> $ sudo apt-get update
> $ sudo apt-get install docker-compose-plugin
> $ sudo apt-get install docker-compose
>```
>
> 2. Verify the installation:
>
>```bash
> user@machine ~
> $ docker-compose --version
>```

<br /> 

### COSMOS

Following the [COSMOS installation guide](https://docs.openc3.com/docs/getting-started/installation):

> 1. Download the COSMOS project template to get started:
>
> ```bash
> user@machine ~
> $ git clone https://github.com/OpenC3/cosmos-project.git
> ```

Alternatively, this repo can be also be cloned, as it is a `cosmos-project` fork.

> 2. Add the locally cloned project directory to your PATH:
>
> ```bash
> user@machine ~
> $ export PATH=~/openc3-cosmos-gs:$PATH
> ```
>
> 3. Verify if COSMOS services are running smoothly:
>
> ```bash
> user@machine ~
> $ ./openc3.sh run 
> ```
>
> 4. Connect a web browser to `http://localhost:2900` and the COSMOS' GUI should appear. 

<br /> 

### Hamlib

Hamlib provides programs with a consistent API for controlling the myriad of radios and rotators available to amateur radio and communications users. This package is particularly required to establish a connection between Gpredict, COSMOS and our rotators.

Following its [installation guide](https://hamlib.sourceforge.net/manuals/1.2.15/_i_n_s_t_a_l_l.html):

>1. Download the latest package from [SourceForge](https://sourceforge.net/projects/hamlib/);
>
>2. Extract the .tar.gz file and open a shell in that folder;
>
>3. Run the following commands:
>
>```bash
>user@machine ~/hamlib
>$ /configure
>$ make
>$ sudo make install
>$ sudo ldconfig
>```
>
>4. Confirm the installation success:
>
>```bash
>user@machine ~/hamlib
>$ rotctld --version
>```

<br /> 

## Setting up a new COSMOS project

After installing OpenC3 COSMOS and launching the GUI, a demo plugin comes already installed in the project template to help the user get accomodated to the platform capabilities. We will leverage the project template for our application, however, a clean start is desired, so before implementing any developments, the demo plugin should be disabled:

1. Go to `/openc3-cosmos-gs` folder and open `.env` file;

2. Comment `OPENC3_DEMO` variable on line 6:
```bash
# OPENC3_DEMO=1
```

3. On COSMOS GUI, go to Admin Console > Plugins, and uninstall `openc3-cosmos-demo` plugin if present.

Next, we can start implementing our first plugin to obtain the satellite position, as it is the initial and main driver in our operation pipeline. All other steps, such as orientating the antennas or communicating with the satellite, are dependent on its position, since they only begin once it starts appearing in our visible sky. Several programs track satellites, but we'll be using Gpredict to achieve this purpose.

Following the [documentation](https://docs.openc3.com/docs/getting-started/gettingstarted):

> 1. Use the COSMOS plugin generator to create the correct structure:
>
>```bash
>user@machine ~/openc3-cosmos-gs
>$ openc3.sh cli generate plugin gpredict --python
>```

This generates `openc3-cosmos-gpredict` plugin folder, where we'll implement all the information needed to communicate with Gpredict application. In this plugin, there is only one target: the Gpredict application itself, or more specifically, its network interface. The same plugin can have multiple targets with different configurations, but will be not necessary for now.

> 2. Generate a new target in the plugin folder:
>
>```bash
>user@machine ~/openc3-cosmos-gpredict
>$ openc3.sh cli generate target GPREDICT --python
>```

A new `GPREDICT` folder with be created unded `/targets`, where a scaffolding of the remaining concepts (commands, telemetry, conversions) will be implemented, obviously specific to this target. Before proceeding, we must discover how Gpredict communicates to prepare the COSMOS connection.


<br /> 

## Retrieve satellite position from Gpredict

This method basically uses Gpredict compatibility with `rotctld` as a data pass-thru. Based on [Joshua Guthrie's tutorial](http://westmouthbay.com/2020/01/10/getting-pointing-information-from-gpredict-for-use-in-an-external-program/):

> 1. Start Gpredict and configure the ground station details and satellite to track;
>
> 2. Setup a dummy rotator interface in Gpredict, on Edit > Preferences > Interfaces > Rotators;
>
> 3. Define a host and port (localhost:4533 will do);
>
> 4. Enable a 'rotctld' service instance on a new shell:
>
> ```bash
> user@machine ~
> $ rotctld &
> ```
>
> 5. Go to Menu > Antenna Control, and select the desired satellite;
>
> 6. Press 'Engage', then 'Track';
>
> 7. Confirm if the interface is running on the defined host and port:
> 
> ```bash
> user@machine ~
> $ echo "-p" | nc -w 1 localhost 4533
> get_pos:-Azimuth: 294.51-Elevation: 26.09-RPRT 0
>```

<br /> 

## Request satellite position on COSMOS

With this previous knowledge, we just have to configure COSMOS plugin to send a string (command) `"-p"` to the defined `localhost:4533` via TCP/IP (interface), where a `get_pos` string (telemetry) will be responded with the desired azimuth and elevation angles. 

<br /> 

### Create the command packet structure

The described command was then added to the `cmd.txt` file of `GPREDICT` target, following [commands documentation](https://docs.openc3.com/docs/configuration/command):

```ruby
COMMAND GPREDICT SAT_POS_AZEL_CMD BIG_ENDIAN "Request satellite position"
    # Keyword           Name  BitSize Type   Min Max  Default  Description
    APPEND_ID_PARAMETER ID    0       STRING          "-p"     "Position argument"
```

<br /> 

### Create the telemetry packet structure

Similarly, the telemetry packet was configured so that the incoming data can be parsed to extract the intended azimuth and elevation. As such, the following code was added to the respective `tlm.txt` file of the same target, following [telemetry documentation](https://docs.openc3.com/docs/configuration/telemetry):
```ruby
TELEMETRY GPREDICT SAT_POS_AZEL BIG_ENDIAN "Satellite position"
    # Keyword       Name    BitSize Type    Default     Description
    APPEND_ID_ITEM  ID      64      STRING  "get_pos:"  "Position packet identifier"
    APPEND_ITEM     AZ_STR  128     STRING              "Azimuth string data"    
    APPEND_ITEM     EL_STR  0       STRING              "Elevation string data"
    ITEM            AZ      0 0     DERIVED             "Azimuth"
        READ_CONVERSION azimuth_conversion.py
    ITEM            EL      0 0     DERIVED             "Elevation"
        READ_CONVERSION elevation_conversion.py
```

This way, the incoming data is first divided into three strings: 
1. the packet identifier `get_pos:`, with 8 characters (or 8*8=64 bits), for validating purposes;
2. the azimuth information `-Azimuth: ***.**`, with 16 characters at max (or 128 bits);
3. the elevation information `-Elevation: **.**`, with the remaining characters, which include the return flag.

Then, the azimuth and elevation are searched on the respective defined string and converted to floats (therefore considered derived datatypes), with the functions developed for that purpose following the [conversions documentation](https://docs.openc3.com/docs/configuration/conversions). For example, here's the main code snippet of the `azimuth_conversion.py` implementation:
```python
match = re.search(r'Azimuth:\s*([\d.]+)', packet.read("AZ_STR"))
return float(match.group(1))
```

<br /> 

### Configure the interface

Lastly, the `gpredict` plugin interface was configured on `plugin.txt` file, following the [interfaces documentation](https://docs.openc3.com/docs/configuration/interfaces):

```ruby
# Set VARIABLEs to allow variation in your plugin
VARIABLE gpredict_target_name GPREDICT
VARIABLE gpredict_host host.docker.internal
VARIABLE gpredict_port 4533

# Set target interface
TARGET GPREDICT <%= gpredict_target_name %>
INTERFACE <%= gpredict_target_name %>_INT openc3/interfaces/tcpip_client_interface.py <%= gpredict_host %> <%= gpredict_port %> <%= gpredict_port %> 5.0 5.0 BURST
  MAP_TARGET <%= gpredict_target_name %>
```

The target name, host, and port were defined as variables to allow customization in web GUI, if intended. Consequently, the TCP/IP client interface setup was done with respect to the host and port variables. Three arguments are required on the `INTERFACE` after the port number: 

1. Write timeout: set to `5.0` seconds;
2. Read timeout: set to `5.0` seconds;
3. Protocol: set to `BURST`, as default, so that it reads as much data as it can from the interface before returning the data.

The host was defaulted to `host.docker.internal`, instead of `localhost`, as it is containerized.

<br /> 

### Build the plugin

Finally, we can build our plugin and upload it to COSMOS. First, the `.gemspec` and `LICENSE` files should be updated. Then, following the [documentation](https://docs.openc3.com/docs/getting-started/gettingstarted):

> 1. Build the plugin, specifying its version: 
>
>```bash
> user@machine ~/openc3-cosmos-gs/openc3-cosmos-gpredict
> $ openc3.sh cli rake build VERSION=1.0.0
>```
>
> 2. Once built, open the web GUI and return to Admin Console > Plugins;
>
> 3. Click on "Install new plugin", select the generated  `openc3-cosmos-gpredict-1.0.0.gem` file and press "Upload";
 
The `VARIABLES` pop-up should appear for customization, but it is not mandatory to modify anything.

> 4. If changes are made to the plugin source code, rebuild the plugin with a new `VERSION` number, following step 1 and 2;
> 
> 5. Instead of installing a new plugin, this time click the clock icon next to `openc3-cosmos-gpredict-1.0.0` to upgrade it.

<br /> 

### Communicate with the target

Once the plugin is loaded to COSMOS, we shall obtain the satellite position from Gpredict.

1. On the web GUI, go to CmdTlmServer side tab > Interfaces, and confirm that the interface `GPREDICT_INT` is connected and ready for communication;

2. Then, go to Command Sender side tab, select the `GPREDICT` target and `SAT_POS_AZEL_CMD` command packet, and hit "Send";

3. Finally, go to Packet Viewer side tab, select the `GPREDICT` target and `SAT_POS_AZEL` telemetry packet, where all items should be successfully parsed and displayed;

4. These will be very similar to the ones on Gpredict, with the exception of the delay offset of transmission and the defined time and step thresholds.

This process can be improved by automatizing the sending of commands, and by plotting the received telemetry.

5. Go to the Script Runner, create a loop to send the command, and hit Run.

```python
while True:
  cmd("GPREDICT SAT_POS_AZEL_CMD with ID '-p'")
  wait(5)
```
6. Then, go to Telemetry Grapher, select the converted `AZ` and `EL` items and add each  to the plot. A new data point should be drawn at a 5 seconds interval.