import os.path


class FileSaver:
    """
    Klasa zapisujaca odpowiednio sformatowane dane do pliku
    format danych : [time,Longitude,Latitude,Altitude,Roll,Pitch,Heading]
    """
    def __init__(self, file_name):
        self.file_name = file_name
        while os.path.isfile(self.file_name):
            temp_str = self.file_name.split(".")
            temp_str = temp_str[0]+"copy.txt"
            self.file_name = temp_str

    def save_data(self, data):
        with open(self.file_name, "a") as f:
            #funkcja map zamienia wszystko na stringi a cale wyrazenie powoduje zapisanie wartosci z tablicy jako ciag
            # stringow oddzielony ","
            text_to_save = ','.join(map(str, data))+"\n"
            f.write(text_to_save)
