import requests
from bs4 import BeautifulSoup as bs
import json

def main():
    print("Programma per estrarre autori e titoli del 2024")

    # URL del sito web da cui estrarre i dati
    url = "https://www.mondadoristore.it/libri-da-leggere-novita-2024/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Richiedi il contenuto della pagina
    response = requests.get(url, headers=headers)

    # Controlla il codice di stato della risposta
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')

        # Dizionario per salvare i dati
        books_dict = {}

        # Trova i tag <h3 class="box-title"> per titoli e autori
        book_tags = soup.find_all("h3", class_="box-title")
        for book_tag in book_tags:
            full_text = book_tag.text.strip()
            
            # Tenta di dividere titolo e autore (ipotizzando "di" come separatore)
            if " di " in full_text:
                title, author = full_text.split(" di ", 1)
                books_dict[title.strip()] = author.strip()
            else:
                # In caso non ci sia un autore, salva solo il titolo
                books_dict[full_text] = "Autore non specificato"

        # Mostra il dizionario
        print("Libri del 2024:")
        print(json.dumps(books_dict, indent=4, ensure_ascii=False))

        # Salva il dizionario in un file JSON
        with open("books_2024.json", "w", encoding="utf-8") as file:
            json.dump(books_dict, file, indent=4, ensure_ascii=False)
    else:
        print(f"Errore nel caricamento della pagina: {response.status_code}")

if __name__ == "__main__":
    main()
