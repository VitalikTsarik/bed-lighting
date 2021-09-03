sudo apt install python3-venv
sudo apt-get install nginx
sudo apt-get install build-essential python-dev
sudo python3 -m venv venv
sudo chown -R pi:pi venv
. venv/bin/activate
pip install -r requirements.txt
