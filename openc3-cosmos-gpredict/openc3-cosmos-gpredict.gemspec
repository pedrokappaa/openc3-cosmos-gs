# encoding: ascii-8bit

# Create the overall gemspec
Gem::Specification.new do |s|
  s.name = 'openc3-cosmos-gpredict'
  s.summary = 'OpenC3 Plugin for Gpredict'
  s.description = <<-EOF
    OpenC3 plugin to communicate with Gpredict, enabling the request and retrieval of the tracking satellite position, in azimuth and elevation angles of the observable sky.
  EOF
  s.license = 'MIT'
  s.authors = ['Pedro Andrade']
  s.email = ['pg49855@alunos.uminho.pt']
  s.homepage = 'https://github.com/pedrokappaa/openc3-cosmos-gs'
  s.platform = Gem::Platform::RUBY

  if ENV['VERSION']
    s.version = ENV['VERSION'].dup
  else
    time = Time.now.strftime("%Y%m%d%H%M%S")
    s.version = '0.0.0' + ".#{time}"
  end
  s.files = Dir.glob("{targets,lib,tools,microservices}/**/*") + %w(Rakefile README.md LICENSE.txt plugin.txt requirements.txt requirements.txt requirements.txt requirements.txt requirements.txt)
end
