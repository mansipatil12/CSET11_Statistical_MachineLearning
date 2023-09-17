class File:
    def __init__(self, name, location, size, date_of_creation, file_encoding):
        self.name = name
        self.location = location
        self.size = size
        self.date_of_creation = date_of_creation
        self.file_encoding = file_encoding
    def create_file(self):
        print(f"Creating {self.name} file...")
    def update_file(self):
        print(f"Updating {self.name} file...")
    def delete_file(self):
        print(f"Deleting {self.name} file...")
class TextFile(File):
    def __init__(self, name, location, size, date_of_creation, file_encoding):
        super().__init__(name, location, size, date_of_creation, file_encoding)
class AudioFile(File):
    def __init__(self, name, location, size, date_of_creation, file_encoding, length, bit_rate):
        super().__init__(name, location, size, date_of_creation, file_encoding)
        self.length = length
        self.bit_rate = bit_rate
    def create_file(self):
        print(f"Creating {self.name} audio file...")
    def delete_file(self):
        print("Audio files cannot be deleted.")
class VideoFile(File):
    def __init__(self, name, location, size, date_of_creation, file_encoding, length, video_quality):
        super().__init__(name, location, size, date_of_creation, file_encoding)
        self.length = length
        self.video_quality = video_quality
    def create_file(self):
        print(f"Creating {self.name} video file...")
    def delete_file(self):
        print("Video files cannot be deleted.")
def main():
    print("File Creation Program")
    print("1. Create Text File")
    print("2. Create Audio File")
    print("3. Create Video File")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        location = input("Enter location: ")
        size = int(input("Enter size: "))
        date_of_creation = input("Enter date of creation: ")
        file_encoding = input("Enter file encoding: ")
        text_file = TextFile(name, location, size, date_of_creation, file_encoding)
        text_file.create_file()
    elif choice == 2:
        name = input("Enter name: ")
        location = input("Enter location: ")
        size = int(input("Enter size: "))
        date_of_creation = input("Enter date of creation: ")
        file_encoding = input("Enter file encoding: ")
        length = int(input("Enter audio length: "))
        bit_rate = int(input("Enter bit rate: "))
        audio_file = AudioFile(name, location, size, date_of_creation, file_encoding, length, bit_rate)
        audio_file.create_file()
    elif choice == 3:
        name = input("Enter name: ")
        location = input("Enter location: ")
        size = int(input("Enter size: "))
        date_of_creation = input("Enter date of creation: ")
        file_encoding = input("Enter file encoding: ")
        length = int(input("Enter video length: "))
        video_quality = input("Enter video quality: ")
        video_file = VideoFile(name, location, size, date_of_creation, file_encoding, length, video_quality)
        video_file.create_file()
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
