class LegacyImageLibrary:
    def load_file(self, filename):
        print(f"Image loaded from file: {filename}")

    def display_image(self):
        print("Image displayed.")


class ModernImageLibrary:
    def load(self, file_path):
        print(f"Image loaded from path: {file_path}")

    def render(self):
        print("Image rendered.")


class ModernImageLibraryAdapter(LegacyImageLibrary):
    def __init__(self,modernLibrary:ModernImageLibrary):
        self.modernLibrary=modernLibrary
    def load_file(self, filename):
        self.modernLibrary.load(file_path=filename)
    def display_image(self):
        self.modernLibrary.render()

#legacyImage= LegacyImageLibrary()
legacyImage=ModernImageLibraryAdapter(ModernImageLibrary())
legacyImage.load_file("teste")
legacyImage.display_image()
