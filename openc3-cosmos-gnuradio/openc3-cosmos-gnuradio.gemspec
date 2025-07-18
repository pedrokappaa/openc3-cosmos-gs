# encoding: ascii-8bit

# Create the overall gemspec
Gem::Specification.new do |s|
  s.name = 'openc3-cosmos-gnuradio'
  s.summary = 'OpenC3 Plugin for GNUradio'
  s.description = <<-EOF
    OpenC3 plugin to communicate with GNUradio, enabling the start and stop of recordings, and adjusting the communication frequencies during runtime.
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
