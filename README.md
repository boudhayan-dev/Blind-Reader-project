Readme

Blind Reader

Developers [![](images/dev1.png)](https://github.com/boudhayan-dev) [![](images/dev2.png)](https://github.com/chinmay4382)

\[!\[Ask Me Anything !\](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg?longCache=true&style=plastic)\](https://GitHub.com/Naereen/ama) \[!\[made-with-python\](https://img.shields.io/badge/Made%20with-Python-blue.svg?longCache=true&style=plastic)\](https://www.python.org/) \[!\[GitHub license\](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?longCache=true&style=plastic)\](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) !\[PyPI - Status\](https://img.shields.io/pypi/status/Django.svg?style=plastic) !\[Contributor\](https://img.shields.io/badge/Contributors-2-orange.svg?longCache=true&style=plastic)

Welcome to the Blind Reader project !  
  

Blind Reader is a portable, low-cost, reading device made for the blind people. The Braille machines are expensive and as a result are not accessible to many. **Blind Reader** overcomes the limitation of conventional Braille machine by making it affordable for the common masses. The system uses OCR technology to convert images into text and reads out the text by using Text-to-Speech conversion.The system supports audio output via Speakers as well as headphone. The user also has the ability to pause the audio output whenever he desires. It also has the facility to store the images in their respective book folder, thereby creating digital backup simultaneously. With this system, the blind user does not require the complexity of Braille machine to read a book. All it takes is a button to control the entire system !

Dependency

  
Hardware Requirements:  

*   Raspberry Pi 3B.
*   Pi Camera.
*   Speakers / Headphones.
*   Push buttons - 2.
*   LDR - 1.
*   LED - 4.
*   Power supply - 5V,2A.

Software Requirements:  

*   Python 3.
*   Python Dependencies:

*   Rpi.GPIO
*   Pygame library.
*   picamera library.
*   google-cloud.
*   time.
*   os.
*   datetime.

*   Google Cloud API - Vision , Text-to-Speech

Usage

  

*   Use the following code to install the Google cloud python dependency.  
      
    `pip3 install --upgrade google-api-python-client  
    pip3 install --upgrade google-cloud-vision  
    pip3 install --upgrade google-cloud`  
      
    Use : [Google CLoud Vision API](https://developers.google.com/api-client-library/python/apis/vision/v1) for further Details.  
      
    
*   Activate **Cloud Vision API** and **Google Cloud Text-to-Speech API** by visiting the dashboard and download the Service account credentials (Json file).
  
*   Connect the hardware as follows:
    
    *   Pi Camera --> Camera Slot in Raspberry Pi 3.
    *   Pair Bluetooth Speaker / Insert headphone into Raspberry Pi 3 audio jack.
    *   LDR --> GPIO 37.
    *   4 LEDs - GPIO 29 , 31 , 33 , 35 respectively.
    *   Push Button 1 ( Camera capture ) --> GPIO 16.
    *   Push Button 2 ( Play/Pause audio ) --> GPIO 18.
    
      
    
*   Use the following code to start the system:  
    `python3 //path/to/your/final.py/file`
  
*   Place the image to be read under the camera and press `Button 1` to read out a page.

Demonstration

![](images/system1.jpg)

![](images/system2.jpg)

Resources

  
*   [Google Cloud Platform.](https://cloud.google.com/python/docs/reference/)
*   [Pygame python library.](https://www.pygame.org/news)
*   [Raspberry Pi.](https://www.raspberrypi.org/)
*   [Python.](https://www.python.org/)
