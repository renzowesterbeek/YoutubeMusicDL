import pafy

def getDownloadList():
	# Gets all the urls from musicfile
	musicFile = open("musicFile.txt", "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

def downloadMusic(files):
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

# There are 2 ways for passing url(s) in function
# 1) downloadMusic/Video(getDownloadList())
# 2) downloadMusic/Video(['https://www.youtube.com/watch?v=SYM-RJwSGQ8'])

downloadVideo(['https://www.youtube.com/watch?v=SYM-RJwSGQ8'])
	
print("")