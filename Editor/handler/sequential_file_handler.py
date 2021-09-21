from handler.data_handler import DataHandler
import json
import pickle


class SequentialFileHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = {}
        self.load_data()

    def load_data(self):
        try:
            with open((self.filepath), 'rb') as dfile:
                self.data = pickle.load(dfile)
            # učitavanje metapodataka
            with open(self.meta_filepath) as meta_file:
                self.metadata = json.load(meta_file)
        except EOFError:
            pass

    def save_to_file(self):
        with open(self.filepath, "wb") as sfile:
            pickle.dump(self.data, sfile)

    def binary_search(self, id, start, end):
        try:
            while start <= end:
                mid = start + (end - start)//2
            # Check if x is present at mid
                if getattr(self.data[mid], (self.metadata["key"])) == id:
                    return mid
            # If x is greater, ignore left hal
                elif getattr(self.data[mid], (self.metadata["key"])) < id:
                    start = mid + 1
            # If x is smaller, ignore right half
                else:
                    end = mid - 1
            return None   # nismo pronasli
        except Exception as e:
            print(e)

    def get_one(self, id):
        try:
            return self.data[self.binary_search(id, 0, (len(self.data)))]
        except Exception as e:
            print(e)

    def find_location_for_insert(self, obj):
        for i in range(len(self.data)):
            if getattr(self.data[i], (self.metadata["key"])) > getattr(obj, (self.metadata["key"])):
                return i
        return None

    def insert(self, obj):
        # trazimo indeks koji je poslednji manji od naseg
        location = self.find_location_for_insert(obj)
        if(location is None):
            self.data.append(obj)
        else:
            self.data.insert(location-1, obj)
        self.save_to_file()

    def get_all(self):
        return self.data

    def edit(self, id, new_value):
        # for d in self.data:
        d = self.data[self.binary_search(id, 0, (len(self.data)))]
        if getattr(d, (self.metadata["key"])) == id:
            index_elementa = self.data.index(d)
            self.data[index_elementa] = new_value
        self.save_to_file()

    def delete_one(self, id):
        d = self.data[self.binary_search(id, 0, (len(self.data)))]
        if getattr(d, (self.metadata["key"])) == id:
            self.data.remove(d)
        self.save_to_file()
