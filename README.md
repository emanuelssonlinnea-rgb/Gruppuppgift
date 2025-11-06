# E-handel analys

## Introduction
Projektet analyserar en fiktiv e-handelsplattform och ger en snabb beslutsunderlag inför nästa kampanjperiod.
I report.ipynb svarar vi på frågor:
1. Vad säljer? – vilka kategorier driver mest intäkt?
2. Var säljer vi? – vilka städer står för störst intäkt?
3. När säljer vi? – finns tidsmönster/säsong i försäljningen?
4. Hur ser en typisk order ut? – AOV (Average Order Value) 
5. Hur ser en typisk order ut? - Totalt sålda enheter och typisk orderstorlek.

## Team
- Abdullahi Sheek Elmi
- Irene Grisenti
- Isabel Holm
- Linnéa Emanuelsson
- Mårten Jakob Ali Ohlsén Salahshour

## Vad vi har gjort / ansvar
Gruppen träffades dagligen i stand-up möten för att gå över ändringar, pull requests,mm.
Vi hade även ett längre möte tisdagar för att samarbeta på projektet.

**Arbetsindelningen såg ut som sådant:** 
 - Abdullahi: Skapade funktionen som beräknar det totala antalet sålda enheter och visualiserar resultatet i ett stapeldiagram. Syftet var att visa vilka produktkategorier som säljer mest och minst.
 - Irene: Förberedde data, beräknade intäkter per stad och tog fram topp 3-städer baserat på intäkter. Skapade ett stapeldiagram som visualiserar intäkterna per stad.
 - Isabel: Skapade AOV metrics och relaterade uträkningar. Visade spridningen för enheter sålda per kategori. Arbetar med struktur och formattering av rapporten.
 - Jakob: Skapat statistiken och grafer för totala intäkter och antal enheter, samt intäkt per kategori.
 - Linnéa: Skapade github repository. Beräknade totala intäkter och intäkter över tid. Skapade ett stapeldiagram och boxplot som visualiserar intäkterna över tid. Skrivit avvikelser + rekommendationer. 

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

