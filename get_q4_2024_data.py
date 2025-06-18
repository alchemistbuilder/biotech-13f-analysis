import requests
import pandas as pd
import time

def get_all_hedge_funds_q4_2024():
    """Get Q4 2024 13F data for all 16 hedge funds for comparison"""
    
    api_key = "m1HzjYgss43pOkJZcWTr2tuKvRvOPM4W"
    date = "2024-12-31"  # Q4 2024
    
    # All 16 hedge funds with their CIKs
    hedge_funds = {
        "Avoro Capital Advisors LLC": "0001633313",
        "Baker Bros. Advisors LP": "0001263508", 
        "BVF Inc": "0001056807",
        "Checkpoint Capital L.P.": "0001977548",
        "Commodore Capital LP": "0001831942",
        "Cormorant Asset Management, LP": "0001583977",
        "Darwin Global Management, Ltd.": "0001839209",
        "Frazier Life Sciences Management, L.P.": "0001892134",
        "Logos Global Management LP": "0001792126",
        "Lynx1 Capital Management LP": "0001910456", 
        "Paradigm Biocapital Advisors LP": "0001855655",
        "Perceptive Advisors LLC": "0001224962",
        "Ra Capital Management, L.P.": "0001346824",
        "Rock Springs Capital Management LP": "0001595725",
        "Rtw Investments, LP": "0001493215",
        "Vivo Capital, LLC": "0001674712"
    }
    
    print(f"Getting Q4 2024 13F data for all {len(hedge_funds)} hedge funds...")
    print("="*70)
    
    all_holdings = []
    successful_funds = []
    
    for fund_name, cik in hedge_funds.items():
        try:
            print(f"\n📊 Processing {fund_name} (CIK: {cik})...")
            
            url = f"https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-holdings?cik={cik}&date={date}&apikey={api_key}"
            
            response = requests.get(url, timeout=20)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                
                if isinstance(data, list) and len(data) > 0:
                    print(f"   ✅ SUCCESS! Found {len(data)} holdings")
                    
                    # Process holdings for this fund
                    fund_holdings = []
                    total_value = 0
                    
                    for item in data:
                        if isinstance(item, dict):
                            holding = {
                                'fund_name': fund_name,
                                'cik': cik,
                                'company': item.get('securityName', ''),
                                'ticker': item.get('symbol', ''),
                                'cusip': item.get('securityCusip', ''),
                                'shares': item.get('sharesNumber', 0),
                                'value': item.get('marketValue', 0),
                                'weight': item.get('weight', 0),
                                'ownership': item.get('ownership', 0),
                                'date': date,
                                'filing_date': item.get('filingDate', ''),
                                'industry': item.get('industryTitle', '')
                            }
                            fund_holdings.append(holding)
                            total_value += holding['value']
                    
                    # Sort by value
                    fund_holdings.sort(key=lambda x: x['value'], reverse=True)
                    
                    # Add to overall list
                    all_holdings.extend(fund_holdings)
                    successful_funds.append((fund_name, len(fund_holdings), total_value))
                    
                    print(f"   💰 Total Portfolio Value: ${total_value:,.0f}")
                    if fund_holdings:
                        print(f"   🏆 Top Holding: {fund_holdings[0]['company']} (${fund_holdings[0]['value']:,.0f})")
                    
                else:
                    print(f"   📋 No holdings found")
            
            else:
                print(f"   ❌ Failed: {response.status_code}")
            
            # Rate limiting
            time.sleep(1)
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue
    
    return all_holdings, successful_funds

def save_q4_data():
    """Save Q4 2024 data for comparison analysis"""
    
    all_holdings, successful_funds = get_all_hedge_funds_q4_2024()
    
    print(f"\n" + "="*70)
    print("Q4 2024 PROCESSING RESULTS")
    print("="*70)
    
    print(f"✅ Successfully processed {len(successful_funds)} funds:")
    for fund_name, holdings_count, total_value in successful_funds:
        print(f"   📊 {fund_name}: {holdings_count} holdings, ${total_value:,.0f}")
    
    if all_holdings:
        # Save raw data
        df = pd.DataFrame(all_holdings)
        df.to_csv('ALL_HEDGE_FUNDS_13F_Q4_2024.csv', index=False)
        
        print(f"\n🎉 Q4 2024 DATA SAVED:")
        print(f"- ALL_HEDGE_FUNDS_13F_Q4_2024.csv")
        print(f"- Total holdings: {len(all_holdings)}")
        print(f"- Total value: ${df['value'].sum():,.0f}")
        
        return df
    else:
        print(f"❌ No Q4 2024 holdings data retrieved")
        return None

if __name__ == "__main__":
    save_q4_data()