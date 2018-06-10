<!DOCTYPE html>
<div class="header" style="width: 100%; display: flex;">
	<div style="font-size: 50px; font-family: arial; width: 50%;"> Blind Reader</div> 
	<div style="width: 50%; text-align: right; display: table; ">
		<span style=" letter-spacing: 5px; padding-left: 150px; font-family: verdana; font-size: 11px;  display: table-cell;vertical-align: middle ;  width: 20px;"> Developers </span>
		<a href="https://github.com/boudhayan-dev" style=" padding-right: 17px;"><img src="images/dev1.png" style="height: 60px; width: 60px;"></a>
		<a href="https://github.com/chinmay4382" style=" padding-right: 17px;"><img src="images/dev2.png" style="height: 60px; width: 60px;"></a>
	</div>
</div>

 <div class="badges-container">
 	<div class="badges-body"> 
 		[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg?longCache=true&style=plastic)](https://GitHub.com/Naereen/ama) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue.svg?longCache=true&style=plastic)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?longCache=true&style=plastic)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)  ![PyPI - Status](https://img.shields.io/pypi/status/Django.svg?style=plastic) ![Contributor](https://img.shields.io/badge/Contributors-2-orange.svg?longCache=true&style=plastic) 
 	</div>
 </div>


<div class="body-content"> 
	<span style="font-size: 25px; font-family: verdana; color: #64686d;"> Welcome to the <span style="color: #18529b;">Blind Reader</span> project !</span>
	<br>
	<br>
	<div style="font-size: 18px; font-family: verdana; text-align: justify;" class="introduction">Blind Reader is a portable, low-cost, reading device made for the blind people. The Braille machines are expensive and as a result are not accessible to many. <strong>Blind Reader </strong>overcomes the limitation of conventional Braille machine by making it affordable for the common masses. The system uses OCR technology to convert images into text and reads out the text by using Text-to-Speech conversion.The system supports audio output via Speakers as well as headphone. The user also has the ability to pause the audio output whenever he desires. It also has the facility to store the images in their respective book folder, thereby creating digital backup simultaneously. With this system, the blind user does not require the complexity of Braille machine to read a book. All it takes is a button to control the entire system !
	</div>
	<div class="dependency" style="font-family: verdana; font-size: 18px; padding-top: 30px;">
		<span style="font-size: 30px; font-family: verdana; font-weight: 500;">Dependency</span>
		<div style="background:#757a79;height: 1.2px; width: 100%"></div><br>
		<span style="font-size: 18px; font-family: verdana; font-weight: 600;">Hardware Requirements:</span><br>
			<ul>
				<li>Raspberry Pi 3B.</li>
				<li>Pi Camera.</li>
				<li>Speakers / Headphones.</li>
				<li>Push buttons - 2.</li>
				<li>LDR - 1.</li>
				<li>LED - 4.</li>
				<li>Power supply - 5V,2A.</li>
			</ul>
		<span style="font-size: 18px; font-family: verdana; font-weight: 600;">Software Requirements:</span><br>
		<ul>
				<li>Python 3.</li>
				<li>Python Dependencies:</li>
				<ul>
					<li>Rpi.GPIO</li>
					<li>Pygame library.</li>
					<li>picamera library.</li>
					<li>google-cloud.</li>
					<li>time.</li>
					<li>os.</li>
					<li>datetime.</li>
				</ul>
				<li>Google Cloud API - Vision , Text-to-Speech</li>
			</ul>
	</div>
	<div class="code"  style="font-family: verdana; font-size: 18px; padding-top: 30px;">
		<span style="font-size: 30px; font-family: verdana; font-weight: 500;">Usage</span>
		<div style="background:#757a79;height: 1.2px; width: 100%"></div><br>
	</div>
	<div class="usage-content" style="font-size: 18px; font-family: verdana; text-align: justify;">
		<ul>
			<li>
				Use the following code to install the Google cloud python dependency.<br><br><code>pip3 install --upgrade google-api-python-client<br>pip3 install --upgrade google-cloud-vision<br>pip3 install --upgrade google-cloud
				</code><br><br>
				Use : <a href="https://developers.google.com/api-client-library/python/apis/vision/v1">Google CLoud Vision API </a> for further Details.<br><br>
			</li>
			<li> Activate <strong>Cloud Vision API</strong> and <strong>Google Cloud Text-to-Speech API</strong> by visiting the dashboard and download the Service account credentials (Json file).</li>
			<br>
			<li>
				Connect the hardware as follows:
				<ul>
					<li>
						Pi Camera --> Camera Slot in Raspberry Pi 3.
					</li>
					<li>
						Pair Bluetooth Speaker / Insert headphone into Raspberry Pi 3 audio jack.
					</li>
					<li>
						LDR --> GPIO 37.
					</li>
					<li>
						4 LEDs - GPIO 29 , 31 , 33 , 35 respectively.
					</li>
					<li>
						Push Button 1 ( Camera capture ) --> GPIO 16.
					</li>
					<li>
						Push Button 2 ( Play/Pause audio ) --> GPIO 18.
					</li>
				</ul>
				<br>
			<li>
				Use the following code to start the system:
				<br>
				<code>
					python3 //path/to/your/final.py/file
				</code>
			</li>
			<br>
			<li>
				Place the image to be read under the camera and press <code> Button 1 </code> to read out a page.
			</li>
		</ul>
	</div>
	<div class="system-images" style="font-family: verdana; font-size: 18px; padding-top: 30px;">
		<span style="font-size: 30px; font-family: verdana; font-weight: 500;">Demonstration</span>
		<div style="background:#757a79;height: 1.2px; width: 100%"></div>
	</div>
	<div class="image-cotainer" style="display: flex;">
		<div class="image1" style="width: 50%"> <img src="images/system1.jpg" style="width: 80%;"></div>
		<div class="image2" style="width: 50%"> <img src="images/system2.jpg" style=" width: 80%; height: 80%; padding-top: 40px;"></div>
	</div>
	<div class="resources-section" style="font-family: verdana; font-size: 18px;">
		<span style="font-size: 30px; font-family: verdana; font-weight: 500;">Resources</span>
		<div style="background:#757a79;height: 1.2px; width: 100%"></div>
	</div>
	<div class="resources-container" style="font-family: verdana; font-size: 18px;">
		<ul><br>
			<li>
				<a href="https://cloud.google.com/python/docs/reference/">Google Cloud Platform.</a>
			</li>
			<li>
				<a href="https://www.pygame.org/news">Pygame python library.</a>
			</li>
			<li>
				<a href="https://www.raspberrypi.org/">Raspberry Pi.</a>
			</li>
			<li>
				<a href="https://www.python.org/">Python.</a>
			</li>
		</ul>
	</div>


</div>
