# Coin Determiner

##See it in action: [Coin Determiner by Prranit Vaswani](http://prranit.pythonanywhere.com)

##Problem:
####Using the Python language, have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an integer output that will specify the least number of coins, that when added, equal the input integer. Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: if num is 16, then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins. 

##Assumptions:
#### 1. Solution must be provided in the form of a web application
#### 2. The application must allow for test files to be uploaded
#### 3. Application must run on any machine
#### 4. Run the application on any web server I want
#### 5. There are no design constraints
#### 6. User will follow instructions provided in readme file
#### 7. User is capable of setting up proper environment before running application

##Design:
#### I first started by working on the coin determiner algorithm. I found it similar to the make bricks algorithm I have worked on in the past. Next, I needed to use the algorithm and put it into a web application. I decided to use Flask as it is a very minimal web framework based on Python. For creating a small web application such as this, it was the obvious choice. However, for more complicated apps, I would lean towards Pyramid or Django. The first functionality I implemented in the web app was input to output. It would take a user input and run it through the coin algorithm and pump out how many coins were needed. Next I implemented a test file upload solution. Here, the user would be able to upload a .txt file with numbers and I would test all of them with my algorithm to see if it works. Once the file was uploaded, I saved it to a local directory as it would have better scalability. Then I proceeded to run each number and ensure it worked. Then, I pushed out the test results in a table format on the web app. Lastly, I added some CSS style sheets to make the web app look simple, yet sophisticated.

##Requirements:
#### Python version: 2.7.6
######[Instructions for setting up Python can be found here](https://www.python.org/downloads/)
#### Flask version: 0.10.1
######[Instructions for setting up Flask can be found here](http://flask.pocoo.org/docs/0.10/installation/)

##Instructions:
#### 1. Make sure you have both Python and Flask installed on your machine.
#### 2. Save the 'fs' folder (with all its contents) onto your machine.
#### 3. Open up the terminal.
#### 4. Change your directory to inside the 'fs' folder
#### 5. Inside the terminal, type: **"python routes.py"**
#### 6. The default address for the web app is: **127.0.0.1:5000** 
####		* Might differ on your machine
#### 7. Once the web app opens, feel free to type in any number in the range 1 to 250 to see how many coins it needs.
#### 8. If you would like to test the app with multiple values, go ahead and click on **Test App**
#### 9. Here, you can upload a **.txt** file to test the app. For convenience, I have provided the "test.txt" file. You can change the values inside the file to try different numbers.
#### 		* Note: To work properly, the test file must list each number on a seperate line. *Otherwise it will fail.*
