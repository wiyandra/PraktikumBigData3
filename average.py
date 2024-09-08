import csv
from functools import reduce

# Fungsi mapper
def mapper(namafile):
    with open(namafile, 'r') as file:
        reader = csv.DictReader(file)
        mapped_values = []
        for row in reader:
            nilai = float(row["nilai"])
            mapped_values.append((nilai, 1))
    return mapped_values

# Fungsi reducer untuk penjumlahan nilai dan penghitungan jumlah
def reducer_sum(values):
    total_sum = reduce(lambda x, y: x + y[0], values, 0)
    total_count = reduce(lambda x, y: x + y[1], values, 0)
    return total_sum, total_count

# Fungsi reducer untuk menghitung rata2
def reducer_rata2(sum_count_pair):
    total_sum, total_count = sum_count_pair
    rata2 = total_sum / total_count
    return rata2

# Menggunakan fungsi-fungsi di atas
def main():
    # Menggunakan mapper
    mapped_values = mapper('C:/Users/Wiyandra/OneDrive/Documents/datahitung/datanilai1.csv')
    
    # Menggunakan reducer pertama untuk menghitung total sum dan count
    sum_count_pair = reducer_sum(mapped_values)
    print(f"Total Nilai dari {sum_count_pair[1]} mahasiswa : {sum_count_pair[0]}")
    
    # Menggunakan reducer kedua untuk menghitung rata2
    rata2 = reducer_rata2(sum_count_pair)
    print(f"Rata - Rata Nilai yang di dapat dari {sum_count_pair[1]}: {rata2}")

if __name__ == "__main__":
    main()
