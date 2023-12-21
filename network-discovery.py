    def netdiscover_tool():
        print(Fore.YELLOW + " network discovery !" + Style.RESET_ALL)
        print()

        print("Ağ taraması yapılıyor...")

        process = subprocess.Popen(['netdiscover', '-r', '192.168.1.0/24'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()

        output = output.decode()

        if output:
            print(Fore.GREEN + "Tarama Sonuçları:")
            results = output.splitlines()[2:-1] 
            for result in results:
                print(result)
        else:
            print(Fore.RED + "Cihaz bulunamadı.")

    netdiscover_tool()