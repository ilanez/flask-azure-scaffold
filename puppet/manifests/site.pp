node default {

    $ENVIRONMENT = "DEVELOPMENT"

    exec { 'apt-update':
      command => '/usr/bin/apt-get update',
    }


    Exec["apt-update"] -> class{'python':} #-> Package <| |>
    include users
    include nginx
    include uwsgi
    include utils
}
