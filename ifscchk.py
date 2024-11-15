import requests
from colorama import Fore, Style, init

init()

merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL

def get_ifsc_details(ifsc_code):
    url = f"https://ifsc.razorpay.com/{ifsc_code}" 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"{putih}Bank Details for IFSC Code {ifsc_code}:")
        print(f"{hijau}Bank Name:{putih} {data.get('BANK')}")
        print(f"{hijau}Branch:{putih} {data.get('BRANCH')}")
        print(f"{hijau}Address:{putih} {data.get('ADDRESS')}")
        print(f"{hijau}City:{putih} {data.get('CITY')}")
        print(f"{hijau}District:{putih} {data.get('DISTRICT')}")
        print(f"{hijau}State:{putih} {data.get('STATE')}")
        print(f"{hijau}MICR Code:{putih} {data.get('MICR')}")
        print(f"{hijau}RTGS Available:{putih} {data.get('RTGS')}")
        print(f"{hijau}NEFT Available:{putih} {data.get('NEFT')}")
        print(f"{hijau}IMPS Available:{putih} {data.get('IMPS')}")
        print(f"{hijau}UPI Available:{putih} {data.get('UPI')}")
        print(f"{hijau}Contact Number:{putih} {data.get('CONTACT')}")
    else:
        print(f"{merah}Failed to fetch IFSC details. Please check the IFSC code or try again later.{reset}")

def main():
    banner = f"""
{putih}███╗   ██╗ ██████╗  ██████╗ ██████╗   {putih}An IFSC Details {hijau}Finder
████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗  {hijau}Version: {putih}v 1.0.0
██╔██╗ ██║██║   ██║██║   ██║██████╔╝  {putih}Author: {hijau}Noob Pirate 
██║╚██╗██║██║   ██║██║   ██║██╔══██╗  {hijau}Note: {putih}Every Code Is Our Weapon
██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝  {putih}Join: {hijau}https://t.me/piratexcrew
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝   {hijau}Bored..? : {putih}http://bit.ly/3MTMHyU
______________________________________________________________________
    {reset}"""
    print(banner)

if __name__ == "__main__":
    main()
    ifsc_code = input(f"{putih}Please enter the IFSC code: {reset}")
    get_ifsc_details(ifsc_code)
