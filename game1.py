import random
import time

# Fungsi untuk menampilkan teks per huruf dengan delay
def tampilkan_teks_per_huruf(teks, delay=0.05):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print()

# Daftar teka-teki dan jawabannya
puzzle = [
    {"question": "Apa yang selalu datang tetapi tidak pernah tiba?", "answer": "besok"},
    {"question": "Saya punya kota, tapi tanpa rumah. Saya punya gunung, tapi tanpa pohon. Saya punya air, tapi tidak ada ikan. Apa saya?", "answer": "peta"},
    {"question": "Apa yang lebih besar dari gunung, lebih ringan dari udara, dan bisa diterbangkan oleh angin?", "answer": "balon"},
    {"question": "Code apa yang kita gunakan untuk menampilkan sebuah kalimat yang kita buat?", "answer": "print"},
    {"question": "Apa lawan dari dingin ?", "answer": "panas"},
    {"question": "Semakin banyak yang kamu ambil semakin jauh ?", "answer": "langkah"},
    {"question": "apa yang selalu kita lihat dan kita pertanyakan kepada seorang benda ini ada di rumahbahkan bisa dipakai di pergelangan apakah saya?", "answer": "jan"},
]

# Fungsi untuk lempar dadu dengan bobot
def lempar_dadu(bonus=0):
    bobot = [1] * 16 + [3] * 4
    hasil = random.choices(range(1, 21), weights=bobot, k=1)[0]
    return min(hasil + bonus, 20)

# Fungsi untuk menentukan item yang didapatkan setelah pertarungan
def drop_item():
    items = [
        {"name": "Pedang Tajam", "effect": "menambah serangan 5", "bonus_attack": 5, "price": 50},
        {"name": "Perisai Baja", "effect": "menambah pertahanan 5", "bonus_defense": 5, "price": 50},
        {"name": "Potion Kesehatan", "effect": "menambah 10 HP", "bonus_hp": 10, "price": 30},
        {"name": "Cincin Magis", "effect": "menambah kekuatan dadu +2", "bonus_dice": 2, "price": 70},
        {"name": "Blasphemous Blade", "effect": "menambah serangan 30",  "bonus_attack":30,  "price": 100},
        {"name": "Boodkatana ", "effect": "menambah serangan 45","bonus_attack":45, "price": 150}
    ]
    if random.random() < 0.5:
        return random.choice(items)
    return None

# Fungsi untuk menampilkan status pemain
def tampilkan_status(player):
    tampilkan_teks_per_huruf("\n==== STATUS KARAKTER ====")
    tampilkan_teks_per_huruf(f"Nama: {player['name']}")
    tampilkan_teks_per_huruf(f"Kelas: {player['class_name']}")
    tampilkan_teks_per_huruf(f"Level: {player['level']} (EXP: {player['exp']}/{player['level'] * 50})")
    tampilkan_teks_per_huruf(f"HP: {player['hp']} / {player['max_hp']}")
    tampilkan_teks_per_huruf(f"Serangan: {player['attack']}")
    tampilkan_teks_per_huruf(f"Pertahanan: {player['defense']}")
    tampilkan_teks_per_huruf(f"Bonus Dadu: {player['bonus_dice']}")
    tampilkan_teks_per_huruf(f"Gold: {player['gold']}")
    tampilkan_teks_per_huruf(f"Inventori: {', '.join([item['name'] for item in player['inventory']]) if player['inventory'] else 'Kosong'}")

# Fungsi untuk pertarungan dengan monster
def pertarungan(monster, player, round_count):
    monster['hp'] = monster['max_hp']
    tampilkan_teks_per_huruf(f"\nRound {round_count}: Pertarungan dimulai melawan {monster['name']}!")
    tampilkan_teks_per_huruf(f"{monster['description']}")
    tampilkan_teks_per_huruf(f"HP Monster: {monster['hp']} / {monster['max_hp']}\n")
    
    while player['hp'] > 0 and monster['hp'] > 0:
        tampilkan_teks_per_huruf(f"\nSerangan Pemain (HP: {player['hp']} / {player['max_hp']})")
        
        hasil_dadu_player = lempar_dadu(player['bonus_dice'])
        serangan_pemain = hasil_dadu_player + player['attack']
        tampilkan_teks_per_huruf(f"Hasil lemparan dadu: {hasil_dadu_player} (Serangan: {serangan_pemain})")
        
        if serangan_pemain >= monster['defense']:
            damage = serangan_pemain - monster['defense']
            monster['hp'] -= damage
            tampilkan_teks_per_huruf(f"Anda menyerang! Monster terkena {damage} damage. HP monster sekarang: {monster['hp']}")
        else:
            tampilkan_teks_per_huruf(f"Serangan Anda gagal. Monster bertahan!")
        
        if monster['hp'] > 0:
            hasil_dadu_monster = lempar_dadu()
            serangan_monster = hasil_dadu_monster + monster['attack']
            tampilkan_teks_per_huruf(f"\nMonster menyerang! Hasil lemparan dadu: {hasil_dadu_monster} (Serangan: {serangan_monster})")
            
            if serangan_monster >= player['defense']:
                damage = serangan_monster - player['defense']
                player['hp'] -= damage
                tampilkan_teks_per_huruf(f"Monster menyerang! Anda terkena {damage} damage. HP Anda sekarang: {player['hp']}")
            else:
                tampilkan_teks_per_huruf(f"Serangan monster gagal. Anda bertahan!")
    
    if monster['hp'] <= 0:
        tampilkan_teks_per_huruf(f"\nAnda mengalahkan {monster['name']}!")
        item = drop_item()
        if item:
            tampilkan_teks_per_huruf(f"Anda mendapatkan item: {item['name']} ({item['effect']})")
            player['inventory'].append(item)
        
        player['gold'] += 20
        player['exp'] += 25
        tampilkan_teks_per_huruf(f"Gold Anda sekarang: {player['gold']}")
        tampilkan_teks_per_huruf(f"EXP Anda sekarang: {player['exp']}")
        
        if player['exp'] >= player['level'] * 50:
            player['level'] += 1
            player['exp'] = 0
            player['max_hp'] += 15
            player['attack'] += 3
            player['defense'] += 5
            tampilkan_teks_per_huruf(f"Selamat! Anda naik level ke {player['level']}!")

# Fungsi untuk teka-teki
def teka_teki(player):
    puzzle_terpilih = random.choice(puzzle)
    tampilkan_teks_per_huruf(f"\nTeka-teki: {puzzle_terpilih['question']}")
    jawaban = input("Jawaban Anda: ").lower()
    
    if jawaban == puzzle_terpilih['answer']:
        tampilkan_teks_per_huruf("Jawaban Anda benar!")
        return True
    else:
        tampilkan_teks_per_huruf("Jawaban Anda salah!")
        return False

# Fungsi Kota
def kota(player):
    while True:
        tampilkan_teks_per_huruf("\nSelamat datang di Kota!")
        tampilkan_teks_per_huruf("1. Tampilkan Status Karakter")
        tampilkan_teks_per_huruf("2. Toko Barang")
        tampilkan_teks_per_huruf("3. Gereja (Heal)")
        tampilkan_teks_per_huruf("4. Lanjutkan Petualangan")
        pilihan = input("Pilih aksi (1/2/3/4): ")
        
        if pilihan == '1':
            tampilkan_status(player)
        elif pilihan == '2':
            toko(player)
        elif pilihan == '3':
            heal(player)
        elif pilihan == '4':
            break
        else:
            tampilkan_teks_per_huruf("Pilihan tidak valid.")

# Fungsi untuk toko barang
def toko(player):
    while True:
        tampilkan_teks_per_huruf("\nSelamat datang di Toko!")
        tampilkan_teks_per_huruf("Barang yang tersedia:")
        for idx, item in enumerate([
            {"name": "Pedang Tajam", "price": 50},
            {"name": "Perisai Baja", "price": 50},
            {"name": "Potion Kesehatan", "price": 30},
            {"name": "Cincin Magis", "price": 70},
            {"name": "Blasphemous Blade", "price": 100},
            {"name": "Boodkatana ", "price": 150}
        ], 1):
            tampilkan_teks_per_huruf(f"{idx}. {item['name']} - {item['price']} Gold")
        
        tampilkan_teks_per_huruf(f"Gold Anda: {player['gold']}")
        pilihan = input("Pilih barang (1-6) atau 0 untuk keluar: ")
        
        if pilihan == '0':
            break
        try:
            pilihan = int(pilihan) - 1
            if 0 <= pilihan < 4:
                item = [
                    {"name": "Pedang Tajam", "price": 10},
                    {"name": "Perisai Baja", "price": 30},
                    {"name": "Potion Kesehatan", "price": 20},
                    {"name": "Cincin Magis", "price": 50},
                    {"name": "Blasphemous Blade", "price": 100},
                    {"name": "Boodkatana ", "price": 150}
                    
                ][pilihan]
                if player['gold'] >= item['price']:
                    player['gold'] -= item['price']
                    player['inventory'].append(item)
                    tampilkan_teks_per_huruf(f"Anda membeli {item['name']}!")
                else:
                    tampilkan_teks_per_huruf("Gold Anda tidak cukup!")
            else:
                tampilkan_teks_per_huruf("Pilihan tidak valid.")
        except ValueError:
            tampilkan_teks_per_huruf("Pilihan tidak valid.")

# Fungsi untuk penyembuhan di gereja
def heal(player):
    if player['gold'] >= 20:
        player['gold'] -= 20
        player['hp'] = player['max_hp']
        tampilkan_teks_per_huruf(f"Anda telah sembuh sepenuhnya! Gold Anda sekarang: {player['gold']}")
    else:
        tampilkan_teks_per_huruf("Gold Anda tidak cukup untuk menyembuhkan!")

# Fungsi Pemilihan Kelas
def pilih_class():
    tampilkan_teks_per_huruf("\nMasukkan nama karakter Anda: ")
    nama = input("Nama Anda: ")
    tampilkan_teks_per_huruf("\nPilih kelas karakter:")
    tampilkan_teks_per_huruf("1. Warrior - Serangan tinggi, Pertahanan menengah")
    tampilkan_teks_per_huruf("2. Mage - Serangan sihir tinggi, Pertahanan rendah")
    tampilkan_teks_per_huruf("3. Archer - Serangan jarak jauh, Pertahanan rendah")
    pilihan = input("Pilih kelas (1/2/3): ")
    
    if pilihan == '1':
        return {"name": nama, "class_name": "Warrior", "hp": 100, "max_hp": 100, "attack": 16, "defense": 17, "bonus_dice": 0, "inventory": [], "gold": 50, "level": 1, "exp": 0}
    elif pilihan == '2':
        return {"name": nama, "class_name": "Mage", "hp": 100, "max_hp": 100, "attack": 20, "defense": 8, "bonus_dice": 0, "inventory": [], "gold": 50, "level": 1, "exp": 0}
    elif pilihan == '3':
        return {"name": nama, "class_name": "Archer", "hp": 100, "max_hp": 100, "attack": 18, "defense": 8, "bonus_dice": 0, "inventory": [], "gold": 50, "level": 1, "exp": 0}
    else:
        tampilkan_teks_per_huruf("Pilihan tidak valid. Memilih Warrior secara default.")
        return {"name": nama, "class_name": "Warrior", "hp": 100, "max_hp": 100, "attack": 15, "defense": 10, "bonus_dice": 0, "inventory": [], "gold": 50, "level": 1, "exp": 0}

# Fungsi Utama
def main():
    player = pilih_class()
    monster_list = [
        {"name": "Goblin", "description": "Makhluk kecil dengan pedang tajam.", "hp": 50, "max_hp": 50, "attack": 14, "defense": 5},
        {"name": "Troll", "description": "Makhluk besar dengan kekuatan brutal.", "hp": 100, "max_hp": 100, "attack": 20, "defense": 10},
        {"name": "Naga", "description": "Makhluk legendaris dengan napas api.", "hp": 110, "max_hp": 110, "attack": 30, "defense": 15},
        {"name": "shawdow creatur", "description": "Makhluk legendaris yang menunggu dibayangan.", "hp": 100, "max_hp": 100, "attack": 15, "defense": 15 },
        {"name": "Tree sentinel", "description": "Seorang giant yang kuat yang manaiki kuda.", "hp": 120, "max_hp": 120, "attack": 9, "defense": 15},
        {"name": "Elder Beast", "description": "Sebuah mahluk interdimensional yang datang dari dunia lain .", "hp": 200, "max_hp": 200, "attack": 10, "defense": 15},
    ]
    round_count = 1
    
    while player['hp'] > 0:
        if teka_teki(player):
            monster = random.choice(monster_list)
            pertarungan(monster, player, round_count)
            kota(player)
            round_count += 1
        else:
            tampilkan_teks_per_huruf("\nGame Over! Anda gagal.")
            break
    tampilkan_teks_per_huruf("\nPermainan selesai! Terima kasih telah bermain.")

if __name__ == "__main__":
    main()
