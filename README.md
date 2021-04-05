# Scammer Payback
Want to get payback at scammers? Read here to learn about how to spam then :)

## Step One:
To start this installation, you will need a code editor such as [Atom](https://atom.io/) or [VSCode](https://code.visualstudio.com/)<br><br>

After installing the code editor, you have to copy the code from scam.py. Since it's only one file, it should only take a few seconds.<br>
We will add a Git installation later on.

To install this repo, you will need to clone it via Git.<br>
Download the [latest](https://git-scm.com/download) version of Git. 

## Step Two:
If you dont want the scammers knowing information about you, I suggest using going in Icogneto to stay anonymous.<br>
Other web browsers may not work due to the feature we need to us in DevTools (Inspect Element)

## Step Three: 
On the scam website, you will need to look for Form Data and the Redirect, and it's easier than you think.<br>
- First, open your DevTools (Inspect Element)<br>
- Second, Go to Network, Header, then Doc.<br>
- Third, Log in to the scam website (Put random gibberish into the Log In details. It'll accept it.)
- Fourth, Under General, there should be a line called "Request URL" Keep that URL in mind because we'll be need to use that later on.
- Fifth, Look through all of the files until you see Form Data. It should be at the bottom of each Header.
- Sixth, look for the information you put into the site. The login/password (Not what you put in) may be a random string of letters and numbers. If so, that's what we're looking for. If it says username and password, then that'll work too.<br>
- Seventh, change the python script to the details that you found.<br>
- Eighth, Open CMD and go into the folder where your script is. Then write "py scam.py"<br>
Then it should spam the website.<br>
