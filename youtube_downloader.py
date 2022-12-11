from pytube import YouTube

link = input("Enter")
yt = YouTube(link)

downloader = yt.streams.get_highest_resolution()
print("downloading")

downloader.download(filename="Magnus_Karlsen_match.mp4")
print("finished")