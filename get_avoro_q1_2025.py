import requests
import pandas as pd

def get_avoro_q1_2025_data():
    """Get Avoro Capital Q1 2025 13F data specifically"""
    
    api_key = "m1HzjYgss43pOkJZcWTr2tuKvRvOPM4W"
    cik = "0001633313"  # Avoro Capital CIK
    date = "2025-03-31"  # Q1 2025 date
    
    print("Getting Avoro Capital Q1 2025 13F Holdings...")
    print(f"CIK: {cik}")
    print(f"Date: {date}")
    
    # Try the portfolio holdings endpoint with specific date
    url = f"https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-holdings?cik={cik}&date={date}&apikey={api_key}"
    
    try:
        print(f"\nTrying: {url}")
        response = requests.get(url, timeout=20)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS! Data type: {type(data)}")
            print(f"Records: {len(data) if isinstance(data, list) else 'Not a list'}")
            
            if isinstance(data, list) and len(data) > 0:
                print(f"📊 Found {len(data)} holdings for Avoro Capital Q1 2025!")
                
                # Process holdings
                holdings = []
                for i, item in enumerate(data, 1):
                    if isinstance(item, dict):
                        # Print sample data structure
                        if i == 1:
                            print(f"\n🔍 Sample holding structure:")
                            for key, value in item.items():
                                print(f"  {key}: {value}")
                        
                        holding = {
                            'rank': i,
                            'company': item.get('securityName', item.get('companyName', item.get('name', ''))),
                            'ticker': item.get('symbol', ''),
                            'cusip': item.get('cusip', ''),
                            'shares': item.get('sharesNumber', item.get('shares', 0)),
                            'value': item.get('marketValue', item.get('value', 0)),
                            'percentage': item.get('percentage', item.get('percentPortfolio', 0)),
                            'date': date,
                            'fund': 'Avoro Capital Advisors LLC',
                            'cik': cik
                        }
                        holdings.append(holding)
                
                # Create DataFrame
                df = pd.DataFrame(holdings)
                
                # Sort by value (largest holdings first)
                df = df.sort_values('value', ascending=False)
                df['rank'] = range(1, len(df) + 1)
                
                # Export to CSV and Excel
                df.to_csv('avoro_capital_q1_2025_REAL.csv', index=False)
                df.to_excel('avoro_capital_q1_2025_REAL.xlsx', index=False)
                
                print(f"\n🎉 REAL AVORO Q1 2025 13F DATA EXPORTED!")
                print(f"Files created:")
                print(f"- avoro_capital_q1_2025_REAL.csv")
                print(f"- avoro_capital_q1_2025_REAL.xlsx")
                
                # Display summary
                total_value = df['value'].sum()
                print(f"\n📊 AVORO CAPITAL Q1 2025 SUMMARY:")
                print(f"Total Portfolio Value: ${total_value:,.0f}")
                print(f"Number of Holdings: {len(df)}")
                print(f"Largest Holding: {df.iloc[0]['company']} (${df.iloc[0]['value']:,.0f})")
                
                # Show top 10 holdings
                print(f"\n🏆 TOP 10 HOLDINGS:")
                top_10 = df.head(10)[['rank', 'company', 'ticker', 'shares', 'value', 'percentage']]
                print(top_10.to_string(index=False))
                
                return df
                
            else:
                print(f"📋 Empty data or different structure: {data}")
                
        else:
            print(f"❌ Failed: {response.status_code}")
            if response.text:
                print(f"Response: {response.text[:500]}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return None

def try_all_available_dates():
    """Try to get data for all available dates"""
    
    api_key = "m1HzjYgss43pOkJZcWTr2tuKvRvOPM4W"
    cik = "0001633313"
    
    # Try recent quarters
    dates_to_try = [
        "2025-03-31",  # Q1 2025
        "2024-12-31",  # Q4 2024
        "2024-09-30",  # Q3 2024
        "2024-06-30",  # Q2 2024
    ]
    
    print(f"\n" + "="*60)
    print("TRYING ALL RECENT QUARTERS")
    print("="*60)
    
    successful_data = []
    
    for date in dates_to_try:
        try:
            print(f"\n📅 Trying {date}...")
            
            url = f"https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-holdings?cik={cik}&date={date}&apikey={api_key}"
            
            response = requests.get(url, timeout=15)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                
                if isinstance(data, list) and len(data) > 0:
                    print(f"   ✅ SUCCESS! Found {len(data)} holdings for {date}")
                    
                    # Save this data
                    quarter_name = date.replace("-", "_")
                    df = pd.DataFrame(data)
                    df.to_csv(f'avoro_{quarter_name}.csv', index=False)
                    
                    successful_data.append((date, data))
                    
                    # Show summary
                    total_value = sum(item.get('marketValue', item.get('value', 0)) for item in data)
                    print(f"   💰 Total Value: ${total_value:,.0f}")
                    
                else:
                    print(f"   📋 No holdings found for {date}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    return successful_data

def main():
    print("GETTING REAL AVORO CAPITAL 13F DATA")
    print("="*50)
    
    # Try to get Q1 2025 data specifically
    avoro_data = get_avoro_q1_2025_data()
    
    # If Q1 2025 doesn't work, try other quarters
    if avoro_data is None:
        print(f"\n🔄 Q1 2025 data not available, trying other quarters...")
        successful_data = try_all_available_dates()
        
        if successful_data:
            # Use the most recent available data
            latest_date, latest_data = successful_data[0]
            print(f"\n✅ Using data from {latest_date}")
            
            df = pd.DataFrame(latest_data)
            df.to_csv('avoro_latest_available.csv', index=False)
            df.to_excel('avoro_latest_available.xlsx', index=False)
            
            print(f"📁 Files created:")
            print(f"- avoro_latest_available.csv")
            print(f"- avoro_latest_available.xlsx")
        
        else:
            print(f"❌ No data found for any recent quarters")
    
    print(f"\n✅ Process complete!")

if __name__ == "__main__":
    main()