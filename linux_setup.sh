apt -y update
apt -y upgrade
apt install -y build-essential vim git curl wget
cd ~ && wget https://raw.githubusercontent.com/gitrohitjain/beautify-terminal/main/beautify.sh
cd ~ && echo -Y | sh beautify.sh
