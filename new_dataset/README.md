# Expanded bank sample: annual reports 2020–2025

121 annual reports for 38 banks that are **not** in the original 101-bank sample.
The files are in `reports/<Country>/` and named `Country_BankName_Year.pdf`, where the year is the
financial year the report covers. FY2026 reports are not published yet.
`sources.csv` lists the URL each file was downloaded from.

The folder holds annual reports only. Integrated reports, Moroccan "rapport financier annuel" filings and
Tunisian board/activity reports to the general assembly count as annual reports. Standalone financial
statements, sustainability reports and quarterly results were left out.
Some reports are in French or Arabic when that is the only version the bank publishes (mainly Tunisia and Algeria).

## Coverage

| Country | Bank | Years |
|---|---|---|
| Algeria | BNP Paribas El Djazair | 2021, 2022, 2023, 2024 |
| Algeria | Trust Bank Algeria | 2021 |
| Bahrain | Bahrain Development Bank | 2020–2025 |
| Bahrain | Eskan Bank | 2020–2025 |
| Bahrain | GFH Financial Group | 2020–2025 |
| Bahrain | United Gulf Bank | 2020–2025 |
| Egypt | Al Baraka Bank Egypt | 2020, 2022 |
| Egypt | Bank of Alexandria | 2021 |
| Jordan | Bank al Etihad | 2020–2025 |
| Jordan | Bank of Jordan | 2024 |
| Jordan | Invest Bank (Jordan) | 2024 |
| Jordan | Jordan Commercial Bank | 2023, 2024 |
| Kuwait | Industrial Bank of Kuwait | 2020–2024 |
| Morocco | CDG Capital | 2020–2025 |
| Morocco | CIH Bank | 2020–2025 |
| Oman | Oman Housing Bank | 2020–2024 |
| Qatar | Lesha Bank (formerly Qatar First Bank) | 2021–2025 |
| Qatar | Qatar Development Bank | 2023, 2024 |
| Tunisia | Al Baraka Bank Tunisia | 2024 |
| Tunisia | BFPME | 2022, 2023 |
| Tunisia | BTK Bank | 2023, 2024 |
| Tunisia | Banque de Tunisie et des Emirats (BTE) | 2020–2025 |
| Tunisia | Banque Tunisienne de Solidarité (BTS) | 2020, 2022, 2023, 2024 |
| Tunisia | Banque Tuniso-Libyenne (BTL) | 2020 |
| Tunisia | QNB Tunis | 2023, 2024, 2025 |
| Tunisia | Tunisian Saudi Bank (TSB) | 2023, 2024 |
| Tunisia | UBCI | 2021–2025 |
| Tunisia | Wifak International Bank | 2020, 2021, 2023, 2024, 2025 |
| UAE | Ajman Bank | 2022–2025 |
| UAE | Al Masraf | 2020–2025 |
| UAE | Bank of Sharjah | 2021, 2022 |
| UAE | Commercial Bank International (CBI) | 2021, 2023, 2024, 2025 |
| UAE | Emirates Investment Bank | 2023 |
| UAE | National Bank of Umm Al Qaiwain (NBQ) | 2025 |
| UAE | United Arab Bank (UAB) | 2024 |

Notes:
- UBCI 2023–2025 are the versions filed with Tunisia's market regulator (CMF); the 2024 one is marked "provisoire".
- CIH Bank 2022 and BFPME 2022–2023 are scanned (image-only) PDFs.
- Three files over GitHub's size limit were compressed with Ghostscript (Ajman Bank 2023, NBQ 2025, and others over 90 MB).

## Not found / not available
- **Saudi Arabia:** every listed Saudi bank is already in the original sample. Gulf International Bank Saudi Arabia's
  site blocks automated downloads (Cloudflare), Samba's site is gone after its 2021 merger, and STC Bank and D360 publish no standalone annual report.
- **Kuwait:** every listed Kuwaiti bank is already in the sample; Ahli United Bank Kuwait's own reports were not found.
- **Egypt:** most remaining Egyptian banks (Credit Agricole Egypt, Suez Canal Bank, EG Bank, Emirates NBD Egypt, NBK Egypt, SAIB…)
  publish only audited financial statements, not annual reports.
- **Morocco:** Bank Assafa, Umnia Bank, Al Akhdar Bank, Bank Al Yousr and Arab Bank Maroc publish only short financial notices.
- **Algeria:** Al Baraka Bank Algeria and Al Salam Bank Algeria refuse connections from the download server; others (AGB, SGA, Natixis Algérie,
  BADR, Housing Bank) do not post annual reports online.
- Gaps in years above are years the bank's website and the stock-exchange/regulator sites did not have, or blocked.

## Copy to your Mac
```
git clone -b claude/annual-bank-dataset-4i1d0c https://github.com/sarahsabry/saradbm.git
mkdir -p "/Users/home/Documents/My Research/SaraHanan/New dataset"
cp saradbm/new_dataset/reports/*/*.pdf "/Users/home/Documents/My Research/SaraHanan/New dataset/"
```
