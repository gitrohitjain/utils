apt -y update
apt -y upgrade
apt install -y build-essential vim git curl wget zip unzip cmake
cd ~ && wget https://raw.githubusercontent.com/gitrohitjain/beautify-terminal/main/beautify.sh
cd ~ && echo -Y | sh beautify.sh
