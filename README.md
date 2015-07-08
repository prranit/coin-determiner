# Coin Determiner

##See it in action: [Coin Determiner by Prranit Vaswani](http://prranit.pythonanywhere.com)

##Problem:
####Using the Python language, have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an integer output that will specify the least number of coins, that when added, equal the input integer. Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: if num is 16, then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins. 

##Requirements:
#### * Python version: 2.7.6
###### 	* [Instructions for setting up Python can be found here](https://www.python.org/downloads/)
#### * Flask version: 0.10.1
###### 	* [Instructions for setting up Flask can be found here](http://flask.pocoo.org/docs/0.10/installation/)

##Instructions:
#### 1. Make sure you have both Python and Flask installed on your machine.
#### 2. Save the 'fs' folder (with all its contents) onto your machine.
#### 3. Open up the terminal.
#### 4. Change your directory to inside the 'fs' folder
#### 5. Inside the terminal, type: **"python routes.py"**
#### 6. The default address for the web app is: **127.0.0.1:5000** *Might differ on your machine*
#### 7. Once the web app opens, feel free to type in any number in the range 1 to 250 to see how many coins it needs.
#### 8. If you would like to test the app with multiple values, go ahead and click on **Test App**
#### 9. Here, you can upload a **.txt** file to test the app. You can provide your own test files or you can use the ones I have provided in the **'testdoc'** folder: **test.txt** and **fail.txt**. To work properly, the test file must list each number on a seperate line. **Otherwise it will fail.** You can also change the values inside **test.txt** to try different values.