# Python-Keylogger
A keylogger written in Python that sends log information remotely through mail. Example for it being used and diguised as a photo

Requires an email for sending and recieveing as well as a google web app password for SMTP authorization

## Demonstration with diguise

### Creating executable
Using pyinstaller you can turn the script into an executable with the command **pyinstaller --onefile --noconsole keylog.py**. 

Adding "--noconsole" make the process run in the background so that it is less conspicuous. Otherwise the console would pop up when opened.

### Hiding with WinRAR
When trying to find ways to disguise executables I found [this one that uses winrar](https://www.youtube.com/watch?v=9QF3SS60rJ4) to disguise it by packaging it with another file, I used a jpg of a cat 😼. This could work with other files too if named accordingly and using an icon that makes sense.

In the self extracting options make the image open and also run the malicous file.

![compres](https://github.com/user-attachments/assets/c65f7525-3cb0-41dd-a27a-127593b0aab2)

### Running the file
Now when the victim sees the file, if they are not paying close attention, it will seems like an ordinary image.

![hiddencat](https://github.com/user-attachments/assets/48680769-2858-480e-8b96-f431e2fa6587)

When they click on the file it will open the photo but the program will be running as a background progress viewable in task manager. This could easily be made less obvious by changing its name and icon.

![image and file2](https://github.com/user-attachments/assets/cd456154-9a91-40cd-8d1b-ec715456e887)

The log information is hidden in the folder that is disguised as the cat image, which can be seen if opened.

![inside file](https://github.com/user-attachments/assets/2fa513b2-abec-4aeb-9e72-3a6fcd777cff)

Then when the file size reaches 300 bytes the content of the log file will be sent by email. This condition can be changed as needed, I set it to this for testing.

![email notficitaion](https://github.com/user-attachments/assets/6e27bab3-b54d-4be9-be34-b1f32bd4e377)

