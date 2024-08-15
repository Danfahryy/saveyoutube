from pytube import YouTube

def get_available_resolutions(url):
    yt = YouTube(url)
    streams = yt.streams.filter(file_extension='mp4').order_by('resolution')
    available_resolutions = [stream.resolution for stream in streams]
    return available_resolutions, yt

def savevidyt(url, resolution, output_path='.'):
    try:
        # Mendapatkan resolusi yang tersedia dan objek YouTube
        available_resolutions, yt = get_available_resolutions(url)
        
        # Memeriksa apakah resolusi yang diminta tersedia
        if resolution not in available_resolutions:
            print(f"Resolution {resolution} not available. Available resolutions are: {', '.join(available_resolutions)}")
            return
        
        # Mengambil stream video dengan format mp4 dan resolusi yang dipilih
        video_stream = yt.streams.filter(file_extension='mp4', resolution=resolution).first()
        
        # Mengunduh video ke path yang ditentukan
        print(f"Downloading: {yt.title} at resolution {resolution}")
        video_stream.download(output_path)
        
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Masukkan URL video YouTube yang ingin diunduh
    video_url = input("Enter YouTube video URL: ")
    
    # Mendapatkan resolusi yang tersedia
    available_resolutions, _ = get_available_resolutions(video_url)
    
    # Menampilkan opsi resolusi kepada pengguna
    print("Available resolutions:")
    for res in available_resolutions:
        print(f"- {res}")
    
    # Memilih resolusi dari pengguna
    selected_resolution = input("Enter the desired resolution (e.g., 360p, 480p, 720p, 1080p): ")
    
    # Path folder tempat video akan diunduh
    output_folder = input("Enter download directory (default is current directory): ")
    
    # Jika folder kosong, gunakan direktori saat ini
    if not output_folder.strip():
        output_folder = '.'
    
    savevidyt(video_url, selected_resolution, output_folder)

