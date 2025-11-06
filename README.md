# E-handel analys

## Introduction
Projektet analyserar en fiktiv e-handelsplattform och ger en snabb beslutsunderlag inför nästa kampanjperiod.

I report.ipynb svarar vi på frågor:
1. Vad säljer? – vilka kategorier driver mest intäkt?
2. Var säljer vi? – vilka städer står för störst intäkt?
3. När säljer vi? – finns tidsmönster/säsong 
4. försäljningen?
5. Hur ser en typisk order ut? – AOV (Average Order Value) och spridning.
6. Topp-listor – topp-3 kategorier efter intäkt.

## Team
- Abdullahi Sheek Elmi
- Irene Grisenti
- Isabel Caroline Holm
- Linnéa Zulmira Moreira Emanuelsson
- Mårten Jakob Ali Ohlsén Salahshour

## Vad vi har gjort / ansvar
Öppnat github repository
Skapat brancher
Börjat koda
Irene: förberedde data, beräknade intäkter per stad och tog fram topp 3-städer baserat på intäkter. Skapade ett stapeldiagram som visualiserar intäkterna per stad.
Linnéa: Beräknade totala intäkter och intäkter över tid. Skapade ett stapeldiagram och boxplot som visualiserar intäkterna över tid. Skriver eventuella avvikelser + rekommendationer. 


## Hur man kör projektet
# klona projetet
git clone https://github.com/emanuelssonlinnea-rgb/Gruppuppgift.git
# Skapa och aktivera virtuell miljö
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate
# macOS/Linux
source .venv/bin/activate 
# installera beroenden
python -m pip install -r requirements.txt

## Miljö
Python 3.13.7
Paket: Pandas, matplotlib (se requirements.txt)

