# 1. Prepairing the Raspberry

11. Configure OS
    - Download and install Raspberry Pi Imager.
    - Choose OS (Raspberry OS Lite)
    - Configure Username, Hostname, Password and WiFi Connection. Default username: pi, password: raspberry
    - Write the image to SD Card
    - Insert SD card into Raspberry, power on and wait until the image is written and Raspberry is connected to your WiFi Network.
    - check the IP Address of the Raspberry Pi on your local Network

12. Log in to Raspberry using ssh
    - Windows CMD:
        ssh "username"@"hostname" or ssh "username"@"hostname IP":
        >> ssh pi@raspberrypi
        - add raspberry to the list of known hosts:
        >> yes
        - enter Password
        >> raspberry

13. Expand the filesystem:
    >> sudo raspi-config
    - Choose "Advanced Options" -> "Expand Filesystem" -> Finish -> Yes
    - Wait until the system is rebooted and then connect again as described above (2.)

14. Update the system
    >> sudo apt-get update
    >> sudo apt-get dist-upgrade

15. Enable SPI and I2C
    >> sudo raspi-config
    -> Interface Options -> SPI -> Yes -> Ok
    -> Interface Options -> I2C -> Yes -> Ok -> Finish
    - Reboot
    >> sudo reboot now

16. Install necessary Tools, libraries and drivers
    >> sudo apt-get install dnsmasq hostapd mosquitto mosquitto-clients python3-pip
    >> sudo pip3 install smbus spidev wiringpi pyserial paho-mqtt
    - Optional install Midnight Commander and Screen:
        >> sudo apt-get install mc screen

17. Install Libraries for MotoPi. More about: https://joy-it.net/de/products/RB-Moto3
    - Download and install SCP-Client on your computer. WinSCP for Windows or CyberDuck for Mac.
    - Connect to the Raspberry:
        - Connection: SFTP
        - Address: "raspberrypi" or IP-Address of the raspberry on your local network
        - Port: 22
        - Password: password, configured in step 1.
    - Navigate to /home/pi
    - Copy and paste the folder RoboControl into this directory
    - Navigate to this folder on Raspberry using ssh
        >> cd RoboControl/
    - Install library:
        >> sudo python3 setup.py install
    - Reboot:
        >> sudo reboot now

18. Add the main Python Program to autostart on reboot. 
    - Edit .bashrc file:
        >> sudo nano .bashrc
    - Add to the end of the file:
		echo Running at boot
		python3 /home/pi/RoboControl/main.py
    - Save and exit:
        Ctrl+X -> Y -> Enter
    - Make the main.py executable
        >> chmod +x main.py
        - to run the script manually, just navigate to the folder where it is located and run:
            >> ./main.py
            - or from the home directory:
                >> ./RoboControl/main.py
        - to exit the program type:
            Ctrl+C
    - Do not reboot until MQTT and WiFi AP are configured (2. and 3.)

# 2. Configure MQTT

21. Log in to Raspberry over ssh.
22. Configure access:
    - Create a new file:
        >> sudo touch /etc/mosquitto/conf.d/listener-with-users.conf
    - Open it in nano editor:
        >> sudo nano /etc/mosquitto/conf.d/listener-with-users.conf
    - Copy and paste this lines:

    listener 1883
    password_file /etc/mosquitto/conf.d/accounts
    allow_anonymous false

    - Save and exit:
        Ctrl+X -> Y -> Enter
    - Add User and Password:
        >> sudo touch /etc/mosquitto/conf.d/accounts
        >> sudo mosquitto_passwd /etc/mosquitto/conf.d/accounts samor
        >> haw
    - Restart MQTT Broker:
        >> sudo systemctl restart mosquitto
	    >> sudo systemctl enable mosquitto

# 3. Configure WiFi Acces Point

31. Network Configuration:
    - Stop dns server and AP:
        >> sudo systemctl stop dnsmasq
        >> sudo systemctl stop hostapd
    - Edit DHCP configuration:
        >> sudo nano /etc/dhcpcd.conf
        - Copy and paste at the end of the file:
        denyinterfaces wlan0
        - Save and exit:
            Ctrl+X -> Y -> Enter

32. Set static IP address:
    >> sudo nano /etc/network/interfaces
    - Copy&Paste:
        allow-hotplug wlan0
        # iface wlan0 inet dhcp
        # wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
        iface wlan0 inet static
            address 192.168.0.1
            netmask 255.255.255.0
            network 192.168.0.0
        - Save and exit:
        Ctrl+X -> Y -> Enter

33. Configure DHCP server:
    >> sudo nano /etc/dnsmasq.conf
    - Copy&Paste at the end of the file:
        interface=wlan0
        dhcp-range=192.168.0.2,192.168.0.20,255.255.255.0,12h
    - Save and exit:
        Ctrl+X -> Y -> Enter
    - Restart dnsmasq:
        >> sudo systemctl restart dnsmasq.service

34. Configure AP:
    >> sudo nano /etc/hostapd/hostapd.conf
    - Copy&Paste:
        interface=wlan0
        ssid=SAMOR_AP
        hw_mode=g
        channel=1
        wpa=2
        wpa_passphrase=samorHAW
        wpa_key_mgmt=WPA-PSK
        wpa_pairwise=TKIP
        rsn_pairwise=CCMP
    - Save and exit:
        Ctrl+X -> Y -> Enter
- Tell the system the path to this file:
    >> sudo nano /etc/default/hostapd
    - Copy&Paste:
        DAEMON_CONF="/etc/hostapd/hostapd.conf"
    - Save and exit:
        Ctrl+X -> Y -> Enter
- Restart network and reboot:
    >> sudo systemctl unmask hostapd
    >> sudo systemctl enable hostapd
    >> sudo systemctl enable dnsmasq
    >> sudo reboot
- After reboot a new WiFi AP appears and main.py in /home/pi/RoboControl starts automatically
- Now the host IP address of raspberry is always 192.168.0.1 

# 4. Tipps

41. To connect to the Raspberry over ssh just connect to the WiFi AP first. The IP address is now always 192.168.0.1
42. After configuring the WiFi AP, the Raspberry will have no Internet Connection. If you want to install some additional packages you have 2 options:
    1. Connect the Raspberry to the local Network using LAN Cable and then check the new IP address on your Router configuration toll.
    2. Disable WiFi AP on raspberry, so it can connect to your WiFi Network:
        >> sudo nano /etc/network/interfaces
        - Comment this lines (add #-symbol at each line):
            # iface wlan0 inet static
            #    address 192.168.0.1
            #    netmask 255.255.255.0
            #    network 192.168.0.0
        - And comment this 2 lines out (remove #-symbol):
            iface wlan0 inet dhcp
		    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
        - Reboot:
            >> sudo reboot now
        - For enabling the AP again revert this changes and reboot
43. After configuring the WiFi AP, the MQTT Broker address is the same as IP address of raspberry: 192.168.0.1. MQTT Broker Port is 1883
44. Test MQTT Connection.
    441. Note: because we defined to run the main.py in .bashrc file (step 18.), each time you open a ssh connection, a new instance of the main program file is started (main.py in /home/pi/RoboControl). So if you want to debug it on raspberry, you have to close the first instance of the main.py file (which is started on boot). So after opening a new ssh connection after the raspberry is booted:
    -  you will se the main.py programm running, the serial output of the mecanum plattform may be corrupted, because there is two instances of main.py running at the same time, and the connection may be unstable. So we need to close all main.py instances. First type Ctrl+C to close the newly opened instance. Then:
        >> htop
    - you will see all processes running on the raspberry pi. Look for command named "python3 ./main.py". 
    - Select it using arrow keys and kill the process with F9 -> Enter.
    - After all main.py instances are closed, open a new one manually:
        >> ./RoboControl/main.py
    - You can also test the MQTT connection without running main.py:
        - subscribe:
            >> mosquitto_sub -t <topic_name> -u <user_name> -P <password>
            - for example: mosquitto_sub -t test -u samor -P haw
        - or publish:
            >> mosquitto_pub -t <topic_name> -u <user_name> -P <password> -m "message"
            - mosquitto_pub -t test -u samor -P haw -m 'Hello world!'

    442. Install a MQTT Client App on Smartphone (MQTT Dashboard for Android) or Windows (MQTT Explorer).
    - Connect to the raspberry WiFi AP
    - MQTT Dashboard:
        tcp://192.168.0.1
        Port: 1883
        Username: samor
        Password: haw
        - Add Toggles, Buttons and setup them:
            Topic: mecanum or manipulator
            Payload: "message to send"
    - Connect to the raspberry over ssh. Make shure only one instance of main.py is runnig.
    - run main.py to test the program output:
        >> ./RoboControl/main.py
    - or subscribe for a specified topic above:
        >> mosquitto_sub -t <topic_name> -u samor -P haw
    443. If testing the app on a pc without a camera, go to main.kv and comment the line 300:
        # resolution: (1920, 1080)