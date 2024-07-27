import requests
from colorama import Fore, init


print(f"{Fore.GREEN}\n███████╗███████╗███╗   ██╗██████╗ ██╗   ██╗███████╗{Fore.RESET}")
print(f"{Fore.GREEN}██╔════╝██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝██╔════╝{Fore.RESET}")
print(f"{Fore.GREEN}███████╗█████╗  ██╔██╗ ██║██║  ██║ ╚████╔╝ ███████╗{Fore.RESET}")
print(f"{Fore.GREEN}╚════██║██╔══╝  ██║╚██╗██║██║  ██║  ╚██╔╝  ╚════██║{Fore.RESET}")
print(f"{Fore.GREEN}███████║███████╗██║ ╚████║██████╔╝   ██║   ███████║{Fore.RESET}")
print(f"{Fore.GREEN}╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚══════╝{Fore.RESET}")
print(f"{Fore.YELLOW}Desenvolvido Por @WandrewTischler            {Fore.BLUE}v0.1{Fore.RESET}")




# Códigos ANSI para cores
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def detect_waf(target):
    if not target.startswith("http"):
        target = "http://" + target

    try:
        # Realizar várias requisições HTTP para detectar WAFs
        responses = [
            requests.get(target),
            requests.post(target, data={'test': 'test'}),
            requests.head(target)
        ]
        
        print(f"{GREEN}Conexão bem-sucedida com {target}{RESET}")

        for response in responses:
            headers = response.headers

            print("\nCabeçalhos:")
            for key, value in headers.items():
                print(f"{key}: {GREEN}{value}{RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{RED}Erro ao conectar-se ao alvo: {e}{RESET}")

if __name__ == "__main__":
    target = input("\nDigite o IP ou o site (com ou sem http/https): ")
    detect_waf(target)
