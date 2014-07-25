import pafy
from Tkinter import *

# input.get()
# output.set()

def getDownloadList(musicfile):
	# Gets all the urls from musicfile
	musicFile = open(musicfile, "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

def downloadAudio(files):
	for url in files:
		audio = pafy.new(url)

		audiofile = audio.getbestaudio(preftype="m4a")
		myfilename = audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)
		
def downloadVideo(files):
	for url in files:
		video = pafy.new(url)

		videofile = video.getbest(preftype="mp4")
		myfilename = videofile.title + "." + videofile.extension

		videofile.download(filepath=myfilename)

def switchType():
	type = typeSelect.get()
	return type

urlList = []
def addURL():
	url = urlInput.get()
	urlList.append(url)
	writeToLog(url)
	urlInput.delete(0, END)
	print urlList

def download():
	if switchType() == "Video":
		downloadVideo(urlList)
	else:
		downloadAudio(urlList)
	status.set("Done")
	del urlList[:]

def writeToLog(msg):
    numlines = log.index('end - 1 line').split('.')[0]
    log['state'] = 'normal'
    if numlines==24:
        log.delete(1.0, 2.0)
    if log.index('end-1c')!='1.0':
        log.insert('end', '\n')
    log.insert('end', msg)
    log['state'] = 'disabled'

# Basic window configuration #
app = Tk()
app.geometry("400x400")
app.title("Python Youtube Downloader")
Scrollbar(app)

# Instructions text #
welcomeText = IntVar()
welcomeText.set("Input YouTube url(s) 1 by 1")
welcome = Label(app, textvariable=welcomeText)
welcome.pack()

# Radiobutton #
typeSelect = StringVar()
R1 = Radiobutton(app, text="Video", variable=typeSelect, value="Video", command=switchType)
R1.pack(anchor=CENTER)
R1.deselect()
R2 = Radiobutton(app, text="Audio", variable=typeSelect, value="Audio", command=switchType)
R2.pack(anchor=CENTER)
R2.select()

# User input #
urlInput = Entry(app)
urlInput.pack()

# Button #
addButton = Button(app, text="Add", command=addURL)
addButton.pack()

# Output Labels #
log = Text(app, state='disabled', width=60, height=10, wrap='none')
log.pack()

# Button #
downloadButton = Button(app, text="Download", command=download)
downloadButton.pack()

# Status Labels #
status = StringVar()
status.set("")
statusLabel = Label(app, textvariable=status)
statusLabel.pack()

app.mainloop()