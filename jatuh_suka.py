import sys
import time
import os
def get_gradient_color(index, total):
    """Menghitung warna gradasi RGB (Pink/Peach -> Ungu Romantis) untuk tiap karakter."""
    if total <= 1:
        return "\033[95m"
    factor = index / (total - 1)
    # Interpolasi dari (255, 140, 160) [Pink Peach] ke (180, 100, 255) [Ungu]
    r = int(255 - factor * 75)
    g = int(140 - factor * 40)
    b = int(160 + factor * 95)
    return f"\033[38;2;{r};{g};{b}m"
def main():
    # Mengaktifkan ANSI escape codes di Windows & encoding UTF-8
    if sys.platform == "win32":
        os.system("")
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass
    print("\033[96m🎵 JATUH SUKA - TULUS 🎵\033[0m")
    print("\033[90m-------------------------\033[0m\n")
    time.sleep(1.5)  # Jeda awal sebelum masuk lirik
    
    # List lirik format: (teks, delay per karakter, jeda di akhir baris)
    lirik = [
        ("Sungguh ku tidak memiliki daya", 0.08, 1.2),
        ("Di depan harummu", 0.09, 1.5),
        ("Sungguh terkunci kata yang tertata", 0.08, 1.2),
        ("Di depan ragamu, uuh-uhh", 0.09, 3.5),
        
        ("Bila kau lihat ku tanpa sengaja", 0.08, 1.2),
        ("Beginikah surga", 0.09, 1.5),
        ("Bayangkan bila kau ajakku bicara", 0.08, 3.5),
        
        ("Ini semua bukan salahmu", 0.08, 1.0),
        ("Punya magis perekat yang sekuat itu", 0.07, 1.0),
        ("Dari lahir sudah begitu", 0.08, 1.0),
        ("Maafkan, aku jatuh suka", 0.09, 5.0),
        
        ("[Instrumental Interlude]", 0.08, 4.0),
        
        ("Bila kau lihat ku tanpa sengaja", 0.08, 1.2),
        ("Beginikah surga", 0.09, 1.5),
        ("Bayangkan bila kau ajakku bicara", 0.08, 3.5),
        
        ("Ini semua bukan salahmu", 0.08, 1.0),
        ("Punya magis perekat yang sekuat itu", 0.07, 1.0),
        ("Dari lahir sudah begitu", 0.08, 1.0),
        ("Maafkan, aku jatuh suka", 0.09, 5.0),
        
        ("[Solo Gitar Melodi]", 0.08, 8.0),
        
        ("Bila kau berkenan", 0.08, 1.5),
        ("Biarkanku di sampingmu", 0.08, 2.0),
        ("Berkuranglah satu jiwa yang sepi", 0.09, 6.0),
        
        ("Ini semua bukan salahmu", 0.08, 1.0),
        ("Punya magis perekat yang sekuat itu", 0.07, 1.0),
        ("Dari lahir sudah begitu", 0.08, 1.0),
        ("Maafkan, ohh-uhh", 0.09, 4.0),
        
        ("Ini semua bukan salahmu", 0.08, 1.0),
        ("Punya magis perekat yang sekuat itu", 0.07, 1.0),
        ("Dari lahir sudah begitu", 0.08, 1.0),
        ("Maafkan", 0.09, 1.5),
        
        ("Aku jatuh suka, hmm", 0.08, 3.0),
        ("Aku jatuh suka", 0.09, 4.0)
    ]
    
    try:
        for teks, delay_karakter, jeda_baris in lirik:
            # Jika baris adalah penanda instrumen musik
            if teks.startswith("["):
                sys.stdout.write("\033[90m🎵 ") # Ikon musik abu-abu
                for huruf in teks:
                    sys.stdout.write(huruf)
                    sys.stdout.flush()
                    time.sleep(delay_karakter)
                sys.stdout.write("\033[0m\n")
            else:
                # Ikon hati berdenyut merah sebelum lirik dimulai
                sys.stdout.write("\033[38;2;255;50;100m❤️  \033[0m")
                total_huruf = len(teks)
                
                # Efek mesin ketik dengan gradasi warna RGB karakter demi karakter
                for i, huruf in enumerate(teks):
                    warna = get_gradient_color(i, total_huruf)
                    sys.stdout.write(f"{warna}{huruf}\033[0m")
                    sys.stdout.flush()
                    time.sleep(delay_karakter)
                sys.stdout.write("\n")
                
            time.sleep(jeda_baris)
            
    except KeyboardInterrupt:
        print("\033[0m\n\nSelesai bernyanyi! 🎤")
        
    print("\nTerima kasih telah bernyanyi bersama! 🎶")
if __name__ == "__main__":
    main()
