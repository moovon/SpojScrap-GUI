SPOJSCRAPPER(GUI VERSION)


-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------



SpojScrapper scraps the details of a username(provided), namely:


>Full Name of the User(if provided by the user)
>World Rank and Total Points
>Number of Problems solved
>Number of Solutions submitted




The entire GUI application is build in python using the GUI library TKINTER.
Some additional librares have been used like beautifulsoup4, requests.
-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

INSTALLATION:: (NOT REQUIRED FOR .EXE (executable file), only for .py file directly(source code))


LINUX:

	  1)Linux usually has python3, if not, install it by using  : $ sudo apt-get python3
	  2)You will need to install certain libraries using pip3 , usually available with python3 itself.
	  3)Run these commands:
	      $ pip3 install beautifulsoup4
	      $ pip3 install requests
	  4)Tkinter library is usually comes with python3.
	  5)After installing all the libraries, go the directory where you kept the "main.py" file.
	  6)In the terminal , run : $ python main.py
	  							 (or $python3 main.py or $ python3.4 main.py whatever supports)

	  							and You are ready to use it.



WINDOWS: You can use Cygwin to get the things done in exact same way like linux: You will have to download cywgin.
			
		(using CMD)
		In windows using CMD, You will need to do a bit more to run the program and but trust me you will learn a lot in the process. So hop on.
		1)You have to install python as in windows python in not installed by default.
		   Head over to https://www.python.org/downloads/ and install the python3+.
		   and do add it the environment variables
		   (my computer->properties->advanced system settings->advanced->Environment Variables->variable path-> add "python path after the ';' like   		   		    xyzwhatever ; C:\python34;"		
		   2)Now , its always good to get libraries of python get installed through pip. But since pip is not a default action in cmd , first we need to get                     		    that first


				Step 1) download and save it as get-pip.py         https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
				Step 2) python get-pip.py
				Step 3)add the "C:/python34/scripts" to the environment variable as in '1'.  add "C:python34/scripts"
				Step 4) Now you are ready to use pip on windows.
		3)Run these commands:
	      > pip3 install beautifulsoup4
	      > pip3 install requests
	  4)Tkinter library is usually comes with python3 itself.
	  5)After installing all the libraries, go the directory where you kept the "main.py" file using cd command.
	  6)In the cmd , run : $ python main.py
	  If you have done everything correctly, the program should run now!


----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------


HOW TO USE:

1)Enter the username in the field provided.
2) Press "Enter" or click "Scrap details"
and you are done! 


----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
mail me : moovonjkm@gmail.com ,incase, you face any problem or want to share anything.

THANK YOU FOR USING SPOJSCRAP