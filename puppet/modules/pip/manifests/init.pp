class pip {

  if versioncmp($::puppetversion,'3.6.1') >= 0 {
    Package {
      allow_virtual => true,
    }
  }

  package { 'curl':
        ensure => installed,
  }

  pip::installation{
    'python3':
    python_version => '3',
  }
}