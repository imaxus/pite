import os.path


class FileSaver:
    """
    Klasa zapisujaca odpowiednio sformatowane dane do pliku
    format danych : [time,Longitude,Latitude,Altitude,Roll,Pitch,Heading]
    """

    @staticmethod
    def save_data(data, file_name):
        with open(file_name, "a") as f:
            #funkcja map zamienia wszystko na stringi a cale wyrazenie powoduje zapisanie wartosci z tablicy jako ciag
            # stringow oddzielony ","
            text_to_save = ','.join(map(str, data))+"\n"
            f.write(text_to_save)
