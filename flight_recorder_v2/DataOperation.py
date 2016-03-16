class DataOperation:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def change_time_relative(data_array):
        """
        Metoda zamieniajaca czas z zegarow samolotu na czas od poczatku lotu
        :param data_array: tablica z wszystkimi danymi z lotu
        :return: tablica z wszystkimi danymi z lotu
        """
        start_time = data_array[0, 0]
        data_array[:, 0] = data_array[:, 0] - start_time
        return data_array
