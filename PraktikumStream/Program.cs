using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Xml.Serialization;
using PraktikumStream;

// ===== SISI PENGIRIM =====
var mhsAsli = new Mahasiswa(
    2024001, "Rans", "Teknologi Informasi",
    new List<string> { "Pemrograman Jaringan", "Basis Data", "Algoritma" });

Console.WriteLine("=== OBJEK ASLI (Memori Pengirim) ===");
mhsAsli.TampilkanInfo();

// Serialisasi JSON -> simpan ke file fisik
string jsonString = JsonSerializer.Serialize(mhsAsli, new JsonSerializerOptions { WriteIndented = true });
File.WriteAllText("mahasiswa.json", jsonString);
Console.WriteLine("[OK] mahasiswa.json berhasil disimpan.");

// Serialisasi XML -> simpan ke file fisik
var xmlSerializer = new XmlSerializer(typeof(Mahasiswa));
string xmlString;
using (var sw = new Utf8StringWriter())
{
    xmlSerializer.Serialize(sw, mhsAsli);
    xmlString = sw.ToString();
}
File.WriteAllText("mahasiswa.xml", xmlString);
Console.WriteLine("[OK] mahasiswa.xml berhasil disimpan.\n");

// ===== SISI PENERIMA =====
// Baca kembali isi file (File.ReadAllText) lalu deserialisasi
string jsonDibaca = File.ReadAllText("mahasiswa.json");
Mahasiswa? mhsDariJson = JsonSerializer.Deserialize<Mahasiswa>(jsonDibaca);
Console.WriteLine("=== HASIL DESERIALISASI DARI mahasiswa.json ===");
mhsDariJson?.TampilkanInfo();

string xmlDibaca = File.ReadAllText("mahasiswa.xml");
Mahasiswa? mhsDariXml;
using (var sr = new StringReader(xmlDibaca))
{
    mhsDariXml = (Mahasiswa?)xmlSerializer.Deserialize(sr);
}
Console.WriteLine("=== HASIL DESERIALISASI DARI mahasiswa.xml ===");
mhsDariXml?.TampilkanInfo();

// ===== VERIFIKASI: sama dengan objek asli? =====
bool jsonSama = mhsDariJson != null && mhsDariJson.NIM == mhsAsli.NIM && mhsDariJson.Nama == mhsAsli.Nama
    && mhsDariJson.Jurusan == mhsAsli.Jurusan && mhsDariJson.MataKuliah.SequenceEqual(mhsAsli.MataKuliah);
bool xmlSama = mhsDariXml != null && mhsDariXml.NIM == mhsAsli.NIM && mhsDariXml.Nama == mhsAsli.Nama
    && mhsDariXml.Jurusan == mhsAsli.Jurusan && mhsDariXml.MataKuliah.SequenceEqual(mhsAsli.MataKuliah);
Console.WriteLine($"Verifikasi JSON sama dengan objek asli : {(jsonSama ? "YA" : "TIDAK")}");
Console.WriteLine($"Verifikasi XML  sama dengan objek asli : {(xmlSama ? "YA" : "TIDAK")}");

// Agar deklarasi XML tertulis encoding="utf-8" saat disimpan ke file
class Utf8StringWriter : StringWriter
{
    public override Encoding Encoding => Encoding.UTF8;
}