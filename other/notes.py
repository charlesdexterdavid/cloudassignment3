print "https://stackoverflow.com/questions/37465816/async-with-in-python-3-4"

print "https://stackoverflow.com/questions/35261468/how-to-use-pip-with-python3-5-after-upgrade-from-3-4"

print '''

15
down vote
accepted
I suppose you can run pip through Python until this is sorted out. (https://docs.python.org/dev/installing/)

A quick googling seems to indicate that this is indeed a bug. Try this and report back:

python3.4 -m pip --version
python3.5 -m pip --version
If they report different versions then I guess you're good to go. Just run python3.5 -m pip install package instead of pip3 install package to install 3.5 packages.

shareimprove this answer
edited Mar 20 at 9:34
answered Feb 8 '16 at 2:28

Harald Nordgren
3,3481727
  	 	
They both show 1.5.4 but with the corresponding python version at the end in parentheses. Installing through the language works great, thank you. – Radeon348 Feb 8 '16 at 2:45
'''