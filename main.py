# [X] Получить все именя файлов из папки Prefetch
# [X] Завести список имен потенциально опасных файлов
# [X] Сравнить то, что в Prefetch и в списке => вывести

from pathlib import Path
from rich import print

# Путь к каталогу Prefetch на исследуемом образе
PREFETCH_DIR_PATH = Path(r"E:\Windows\Prefetch")
# Набор имен файлов, которые будут детектироваться
MALICIOUS_NAMES = (
    "mimikatz", 
    "anydesk", 
    "nmap",
    # и ... список расширяемый
)
for filepath in PREFETCH_DIR_PATH.iterdir():
    
    for malicious_name in MALICIOUS_NAMES:
  
        if malicious_name.lower() in filepath.name.lower():
            print (filepath)
