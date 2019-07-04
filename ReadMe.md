# MotionPy 
### Utilization
MotionPy is a small script, which have to be used with MotionEye together. The Scripts are optimized for the MotionEye-Installation on DietPi-Machines. Once the Scripts are placed in their Directories, they should work properly.
When the System detects motion by camera sensors, you'll get Notifications on Telegram. You'll also be able to interact with the system.

### First Steps
1. Install MotionEye on your DietPi-Machine. Use ```dietpi-software``` to install the Package.
2. Clone this Repository in your Home-Directory. Place both Python-Scripts in the following location: ```/mnt/dietpi_userdata/_data/motioneye```.
3. Create a new Bot and Paste the Token in both files on the top. Use the Variable ```accessToken```.
4. Create a new Group on Telegram and get the Chat-ID. Paste the Value to the Variable ```chat_id```.
5. Create a Service on your local Machine, which will start the ```camera.py```-Script when booting up.
6. Set in the Settings from MotionEye under Motion Notifications -> Run A Command -> Command following Command: ```python3 /mnt/dietpi_userdata/_data/motioneye/camera.py```.
7. Restart your System and check the functions.

### Security
Take note, that you shouldn't make your camera accessible from outside of your local network. If you would like to access the User-Interface from Outside, install ```OPENVPN``` with ```dietpi-software```.

### Purpose of Use.
This software has been written for security reasons. For example, if you are in Holidays and you want to keep your House safe.<br><br> Take note, that surveillance of other people and spying on them will bring problems for you. In this case, i will not be responsible for these actions.

#### Disclaimer
This Software is OpenSource. The Usage of the provided Services (e.g. Telegram) is mandatory. Please read these Informations about security and privacy from these Services too.