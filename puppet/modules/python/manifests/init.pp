class python {
    include python::packages
}



class python::packages::pip_install($requirements_file){

    require python::packages
    exec{ "pip_requirements_install":
        command => "/usr/local/bin/pip install -r /var/www/${hostname}.${domain}/${requirements_file}",
        user => root,
    }

}


  class python::packages {

      notify {"Installing python related packages.":
          loglevel => info
      }

    $apt = ['python3.4-dev', 'build-essential', 'python3-setuptools' ]


    package { $apt:
        require => Class['python'],
        ensure  => installed,
    }->
      exec{ 'pip_easy':
        command=> "/usr/bin/easy_install3 pip",
        path => "/",
        user => root,
        require => Package[$apt],
    }->class{'python::packages::pip_install':requirements_file => 'requirements.txt'}

}







