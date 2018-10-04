bash 'install_python3pip' do
	  code <<-EOH
       sudo yum install yum-utils
       sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
       sudo yum install python36u
       sudo yum install python36u-pip
       yum install -y python36u-devel.x86_64
       pip install fabric
       pip install connexion
  	  EOH
end
