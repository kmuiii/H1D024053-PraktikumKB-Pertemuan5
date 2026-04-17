# kode & gejala penyakit THT
# format: "kode_gejala": "deskripsi gejala"
database_gejala = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}

# list penyakit & rules gejala
# format: "nama_penyakit": ["kode_gejala1", "kode_gejala2", ...]
database_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nasofaring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

print("=== SISTEM PAKAR DIAGNOSA PENYAKIT THT ===")
print("Jawab dengan 'y' untuk Ya dan 'n' untuk Tidak\n")

# input gejala
jawaban_user = {} # simpen jawaban user
for gejala in database_gejala:
    jawab = input(f"Apakah Anda mengalami {database_gejala[gejala]}? (Y/N): ").lower()
    jawaban_user[gejala] = True if jawab == 'y' else False

    # kondisi jawaban selain y/n
    while jawab not in ['y', 'n']:
        print("Input tidak valid. Silakan jawab dengan 'Y' untuk Ya atau 'N' untuk Tidak.")
        jawab = input(f"Apakah Anda mengalami {database_gejala[gejala]}? (Y/N): ").lower()
        jawaban_user[gejala] = True if jawab == 'y' else False

# proses diagnosa
hasil = {}
for penyakit, gejala_list in database_penyakit.items():
    skor = 0
    for gejala in gejala_list:
        if jawaban_user.get(gejala):
            skor += 1
    hasil[penyakit] = skor

# tampilkan hasil diagnosa
print("\n=== HASIL DIAGNOSA ===")
if skor > 0:
    for penyakit, skor in hasil.items():
        print(f"Anda menderita {penyakit}: {skor} gejala yang cocok")
        print(f"Gejala yang cocok: {[database_gejala[gejala] for gejala in database_penyakit[penyakit] if jawaban_user.get(gejala)]}\n")
else:
    print(f"Tidak ada penyakit yang cocok dengan gejala. {skor} gejala yang cocok ditemukan.")