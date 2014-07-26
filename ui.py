import pafy
import os
import errno
from Tkinter import *
import tkMessageBox

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

urlArray = []
def add_url():
	currentContent = urlList.get('1.0', 'end')
	userEntry = urlEntry.get()
	urlArray.append(userEntry)
	urlList.configure(state='normal')
	urlList.insert('end', userEntry + '\n')
	urlList.configure(state='disabled')
	
	urlEntry.delete(0, END)
	return

def clear_dl_list():
	urlList.configure(state='normal')
	urlList.delete("1.0", END)
	urlList.configure(state='disabled')
	del urlArray[:]

def get_download_list(musicfile):
	musicFile = open(musicfile, "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

def download_audio(files):
	for url in files:
		audio = pafy.new(url)

		audiofile = audio.getbestaudio(preftype="m4a")
		myfilename = "YTDownloads/Audio/" + audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)
		
def download_video(files):
	for url in files:
		video = pafy.new(url)

		videofile = video.getbest(preftype="mp4")
		myfilename = "YTDownloads/Video/" + videofile.title + "." + videofile.extension

		videofile.download(filepath=myfilename)

def download():
	mode = relStatus.get()
	if mode == "Audio":
		make_sure_path_exists("YTDownloads/Audio/")
		download_audio(urlArray)
	else:
		make_sure_path_exists("YTDownloads/Video/")
		download_video(urlArray)
		
	tkMessageBox.showinfo("Done", "Your download is completed. You can find the downloaded files in the YTDownloads folder in the directory of this program.")
	clear_dl_list()
	print("")
	
	return

#url = "https://www.youtube.com/watch?v=W9he6KN4Aqk"

# =========================================================================== #

make_sure_path_exists("YTDownloads")

app = Tk()
app.title("Python Youtube Downloader")
Scrollbar(app)

instructionText0 = StringVar()
instructionText0.set("Select download mode")
instructionLabel = Label(app, textvariable=instructionText0, height=2).grid(row=0, column=0, pady=5, padx=15)

instructionText1 = StringVar()
instructionText1.set("Enter your Youtube URL(s) below")
instructionLabel = Label(app, textvariable=instructionText1, height=2).grid(row=0, column=1, pady=5)

relStatus = StringVar()
relStatus.set("Audio")
modeSelect = Radiobutton(app, text="Audio", value="Audio", variable=relStatus).grid(row=1, column=0, sticky=W, padx=15)
modeSelect = Radiobutton(app, text="Video", value="Video", variable=relStatus).grid(row=1, column=0, sticky=E, padx=15)

youtubeURL = StringVar(None)
urlEntry = Entry(app, textvariable=youtubeURL, width=43)
urlEntry.grid(row=1, column=1, sticky=N+E+W, padx=10)

urlList = Text(app, state='disabled', width=44, height=14)
urlList.grid(row=3, column=1, padx=10)

actionButtonFrame = Frame(app)
actionButtonFrame.grid(row=4, column=1)

addButton = Button(app, text="Add", command=add_url).grid(row=2, column=1)
clearButton = Button(actionButtonFrame, text="Clear", width=5, command=clear_dl_list)
clearButton.grid(row=0, column=0, sticky=W, padx=5, pady=5)
downloadButton = Button(actionButtonFrame, text="Download", width=10, command=download)
downloadButton.grid(row=0, column=1, sticky=E, padx=5, pady=5)

app.mainloop()