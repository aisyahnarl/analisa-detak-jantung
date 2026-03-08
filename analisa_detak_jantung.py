detak_jantung = [70, 110, 65, 120, 80, 140, 75]

def analisa_kondisi(bpm):
    if bpm > 100:
        return "Peringatan: Takikardia (Detak_Tinggi)"
    else:
        return "Kondisi: Normal"

print("Analisa Kondisi Detak Jantung:")
for i, nilai_bpm in enumerate(detak_jantung, start=1):
    status = analisa_kondisi(nilai_bpm)
    print(f"Data ke-{i}: {nilai_bpm} BPM -> {status}")