# 13F Biotech Hedge Fund Analysis - Q1 2025

A comprehensive analysis of Q1 2025 13F SEC filings from 16 major biotech-focused hedge funds, analyzing over $45 billion in holdings across 903 positions.

## 📊 Overview

This project scrapes and analyzes 13F filings (quarterly institutional holdings reports) from biotech hedge funds to identify:
- Most frequently held stocks across funds
- Largest positions by total market value
- Portfolio concentration analysis

## 🏢 Funds Analyzed

1. **Avoro Capital Advisors LLC** - $6.41B
2. **Baker Bros. Advisors LP** - $9.04B  
3. **BVF Inc** - $1.52B
4. **Checkpoint Capital L.P.** - $0.79B
5. **Commodore Capital LP** - $0.59B
6. **Cormorant Asset Management, LP** - $2.14B
7. **Darwin Global Management, Ltd.** - $0.42B
8. **Frazier Life Sciences Management, L.P.** - $1.26B
9. **Logos Global Management LP** - $3.05B
10. **Lynx1 Capital Management LP** - $0.43B
11. **Paradigm Biocapital Advisors LP** - $4.38B
12. **Perceptive Advisors LLC** - $4.28B
13. **Ra Capital Management, L.P.** - $4.42B
14. **Rock Springs Capital Management LP** - $2.79B
15. **Rtw Investments, LP** - $2.08B
16. **Vivo Capital, LLC** - $1.68B

**Total Assets Under Management: $45.3 Billion**

## 🎯 Key Findings

### Most Frequently Held Stocks (Top 10)
1. **MERUS N V (MRUS)** - 9 funds
2. **VAXCYTE INC (PCVX)** - 8 funds
3. **EDGEWISE THERAPEUTICS INC (EWTX)** - 8 funds
4. **INSMED INC (INSM)** - 8 funds
5. **89BIO INC (ETNB)** - 7 funds
6. **JANUX THERAPEUTICS INC (JANX)** - 7 funds
7. **CENTESSA PHARMACEUTICALS PLC (CNTA)** - 6 funds
8. **AXSOME THERAPEUTICS INC (AXSM)** - 6 funds
9. **REVOLUTION MEDICINES INC (RVMD)** - 6 funds
10. **PLIANT THERAPEUTICS INC (PLRX)** - 6 funds

### Largest Holdings by Value (Top 10)
1. **BeiGene Ltd (BGNE)** - $2.39B (5.29%)
2. **Incyte Corporation (INCY)** - $1.86B (4.11%)
3. **Ascendis Pharma ADR (ASND)** - $1.60B (3.54%)
4. **Insmed Inc (INSM)** - $1.60B (3.53%)
5. **Madrigal Pharmaceuticals (MDGL)** - $1.35B (2.97%)
6. **Argenx SE (ARGX)** - $1.27B (2.80%)
7. **Moonlake Immunotherapeutics (MLTX)** - $1.24B (2.73%)
8. **Verona Pharma PLC (VRNA)** - $1.06B (2.35%)
9. **United Therapeutics Corp (UTHR)** - $825M (1.82%)
10. **Ascendis Pharma (ASND)** - $813M (1.79%)

## 📁 Files

### Analysis Reports
- **`1Q 2025 Biotech 13F Analysis.xlsx`** - Comprehensive Excel report with 5 sheets
- **`1Q 2025 Biotech 13F Analysis - Most Frequent.csv`** - Top 25 most held stocks
- **`1Q 2025 Biotech 13F Analysis - Top Values.csv`** - Top 25 by market value

### Raw Data
- **`ALL_HEDGE_FUNDS_13F_Q1_2025.csv`** - Complete dataset (903 holdings)
- **`ALL_HEDGE_FUNDS_13F_Q1_2025.xlsx`** - Excel version with analysis

### Scripts
- **`all_funds_scraper.py`** - Main scraper using Financial Modeling Prep API
- **`create_final_report.py`** - Generates comprehensive analysis reports  
- **`csv_analyzer.py`** - Fallback analyzer for manual CSV files
- **`get_avoro_q1_2025.py`** - Single fund example scraper

### Legacy/Test Files
- **`fmp_premium_scraper.py`** - API testing script
- **`13f_scraper_dynamic.py`** - JavaScript-enabled scraper attempt
- **`sec_scraper.py`** - Direct SEC.gov scraper attempt

## 🛠️ Technical Approach

### Data Source
Uses **Financial Modeling Prep (FMP) Premium API** to access institutional ownership data:
- Endpoint: `/api/v4/institutional-ownership/portfolio-holdings`
- Requires premium subscription for 13F data access
- Rate limited to prevent API abuse

### Analysis Methods
1. **Frequency Analysis** - Counts holdings across all funds
2. **Value Aggregation** - Sums total market values by stock
3. **Portfolio Weight** - Calculates percentage of total AUM

### Technologies Used
- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **requests** - API calls and HTTP requests
- **openpyxl** - Excel file generation
- **collections** - Counter and defaultdict for analysis

## 📊 Data Quality

- **Coverage**: 16/16 target funds successfully scraped (100%)
- **Holdings**: 903 total positions analyzed
- **Data Date**: March 31, 2025 (Q1 2025 filing period)
- **Filing Dates**: May 2025 (standard 45-day filing window)

## 🚀 Usage

### Prerequisites
```bash
pip install pandas requests openpyxl
```

### Run Analysis
```bash
python all_funds_scraper.py
python create_final_report.py
```

### API Setup
1. Sign up for Financial Modeling Prep Premium account
2. Replace API key in scripts
3. Ensure sufficient API quota for 16 fund requests

## 📈 Investment Insights

### Sector Focus
- **Pharmaceutical Preparations** - Dominant category
- **Biological Products** - High representation  
- **Medical Laboratories** - Emerging focus

### Market Dynamics
- Strong consensus on mid-cap biotech names
- Diversification across therapeutic areas
- Focus on companies with significant institutional backing

### Risk Considerations
- High concentration in speculative biotech stocks
- Regulatory approval risks for pipeline companies
- Market volatility in biotech sector

## 📄 Compliance Note

This analysis is for educational and research purposes only. All data is sourced from public SEC filings through legitimate API services. Not investment advice.

## 🔄 Updates

- **Last Updated**: June 2025
- **Next Update**: Q2 2025 filings (August 2025)
- **Data Refresh**: Quarterly following SEC filing deadlines

---

*Generated using Claude Code - Advanced 13F analysis and institutional holdings research*