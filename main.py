import csv
from csv import reader
from csv import DictReader

with open("C:\\Users\\Studentas\\Downloads\\sampleData.csv", "r", encoding='utf8') as file:
    csv_dictreader = DictReader(file)
    for eilute in csv_dictreader:
        print(eilute)

with open("C:\\Users\\Studentas\\Downloads\\sampleData.csv", "r", encoding='utf8') as file:
    read = file.readlines()
    for eilute in read:
        print(eilute)
def read_csv_file(file_path):
    data = []
    with open(file_path, "r", encoding='utf8') as file:
        csv_dictreader = DictReader(file)
        for eilute in csv_dictreader:
            data.append(eilute)
    return data

def save_data_to_python_file(data, output_file):
    with open(output_file, "w", encoding='utf8') as file:
        file.write("data = ")
        file.write(repr(data))

file_path = "C:\\Users\\Studentas\\Downloads\\sampleData.csv"
csv_data = read_csv_file(file_path)

# Save the data to a Python file
save_data_to_python_file(csv_data, "data.py")

# kokios valiutos buvo naudotos?
valiutos = set()
with open("C:\\Users\\Studentas\\Downloads\\sampleData.csv", "r", encoding='utf8') as file:
    reader = csv.reader(file)
    for eilute in reader:
        valiutos.add(eilute[-2])

print("Naudotos valiutos:", valiutos)

