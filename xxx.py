import requests
import random
from tkinter import *
from bs4 import BeautifulSoup


def createlink():
	root =Tk()
	root.geometry("640x640+0+0")
	root.title("Grub Changer Tool")
	heading=Label(root, text="Enter your image to download:", font=("chiller", 30, "italic"), fg="brown").pack()
	def work():
		global n
		inputValue=textBox.get("1.0","end-1c")
		print(inputValue)
		x=requests.get("https://alpha.wallhaven.cc/search?q="+inputValue+"&categories=100&purity=100&sorting=date_added&order=desc&page=2")
		soup=BeautifulSoup(x.content,"lxml")
		mylinks=soup.find_all("a",class_="preview")
		i=len(mylinks)
		if(i==0):
			print("Wrong choice entered !")
		else:
			rand_i=random.randrange(0,i)
			l=mylinks[rand_i].get("href")
			id=l[37:43]
			fst='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
			url = fst+id+'.jpg'
			n=url
			

	textBox=Text(root,height=4,width=10)
	textBox.pack()
	work=Button(root, text="Download", width=30, height=3,bg="lightblue",command=lambda:work()).place(x=250, y=300)
	root.mainloop()
	return(n)

	# now fetching image data from url.

def fetch_image(url):
	x = requests.get(url)
	with open('/home/suman/Downloads/py/grub_image.jpg', 'wb') as f:  
		f.write(x.content)

	 #Retrieve HTTP meta-data
	print(x.status_code)  
	print(x.headers['content-type'])  
	print(x.encoding)  
	
n=" "
fetch_url=createlink()
if(fetch_url!=0):
	fetch_image(fetch_url) 