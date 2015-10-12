class uwsgi {

    $params = {
        "uid" => "www-data",
        "gid" => "www-data",
        "socket" => "/tmp/uwsgi.sock",
        "logdate" => "",
        "processes" => 2,
        "master" => "",
        "die-on-term" => "",
        "logto" => "/var/log/uwsgi.log",
        "chdir" => "/var/www/${hostname}.${domain}",
        "plugin" => "python3",
        "module" => "runserver",
        "callable" => "app",
    }

  $env = $ENVIRONMENT

    package { "upstart":
        ensure => installed,
    }
    package { "uwsgi":
        ensure => installed,
        require => [Class["python::packages"], Package["upstart"]],
    }

    package { "uwsgi-plugin-python3":
        ensure => installed,
        require => Package["uwsgi"],
    }


#      exec{
#      'update-uwsgi':
#      require => Package["uwsgi-plugin-python3"],
#      command => "/usr/bin/update-alternatives --install /usr/local/bin/uwsgi uwsgi /usr/bin/uwsgi_python3 100 && /sbin/initctl reload-configuration",
#      path => "/",
#    }


    file { "/etc/init/uwsgi.conf":
        ensure => present,
        owner => "root",
        group => "root",
        mode => "0644",
        content => template("uwsgi/uwsgi.conf.erb"),
        require => Package["uwsgi"],
    }
    file { "/var/log/uwsgi.log":
        ensure => present,
        owner => "www-data",
        group => "www-data",
        mode => "0755",
        require => User["www-data"],
    }
    service { "uwsgi":
        ensure => running,
        provider => upstart,
        enable => true,
        hasrestart => false,
        hasstatus => false,
        require => [File["/etc/init/uwsgi.conf"], File["/var/log/uwsgi.log"]],
    }
}
