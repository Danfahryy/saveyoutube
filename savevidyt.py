from pytube import YouTube

def download_youtube_video(url, output_path='.'):
    try:
        # Membuat objek YouTube
        yt = YouTube(url)
        
        # Mengambil stream video dengan format mp4 dan resolusi tertinggi
        video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        
        # Mengunduh video ke path yang ditentukan
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Masukkan URL video YouTube yang ingin diunduh
    print("Download Video Youtube")
    video_url = input("Enter YouTube video URL: ")
    
    # Path folder tempat video akan diunduh
    output_folder = input("Enter download directory (default is current directory): ")
    
    # Jika folder kosong, gunakan direktori saat ini
    if not output_folder.strip():
        output_folder = '.'
    
    download_youtube_video(video_url, output_folder)
