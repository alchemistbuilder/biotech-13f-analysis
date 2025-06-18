import requests
import pandas as pd
import time
from collections import defaultdict

def test_premium_endpoints():
    """Test premium FMP endpoints that should now be available"""
    
    api_key = "m1HzjYgss43pOkJZcWTr2tuKvRvOPM4W"
    
    print("Testing FMP Premium Endpoints...")
    
    # Test institutional ownership endpoints that were blocked before
    test_endpoints = [
        ("Institutional Holders", f"https://financialmodelingprep.com/api/v3/institutional-holder/AAPL?apikey={api_key}"),
        ("Form 13F", f"https://financialmodelingprep.com/api/v3/form-thirteen/AAPL?apikey={api_key}"),
        ("Institutional Portfolio by CIK", f"https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-holdings?cik=0001633313&apikey={api_key}"),
        ("Institutional Portfolio Dates", f"https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-date?cik=0001633313&apikey={api_key}"),
        ("Institutional List", f"https://financialmodelingprep.com/api/v4/institutional-ownership/list?apikey={api_key}"),
    ]
    
    working_endpoints = []
    
    for name, url in test_endpoints:
        try:
            print(f"\n🔍 Testing {name}:")
            response = requests.get(url, timeout=15)
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ SUCCESS! Data type: {type(data)}")
                
                if isinstance(data, list):
                    print(f"📊 Found {len(data)} records")
                    if len(data) > 0 and isinstance(data[0], dict):
                        print(f"🔑 Sample keys: {list(data[0].keys())[:10]}")
                elif isinstance(data, dict):
                    print(f"🔑 Data keys: {list(data.keys())}")
                
                working_endpoints.append((name, url, data))
                
                # Save sample data
                filename = f"fmp_premium_{name.lower().replace(' ', '_')}.csv"
                if isinstance(data, list) and len(data) > 0:
                    df = pd.DataFrame(data)
                    df.to_csv(filename, index=False)
                    print(f"💾 Saved sample to: {filename}")
                
            else:
                print(f"❌ Failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    return working_endpoints

def get_avoro_13f_data():
    """Get real Avoro Capital 13F data using premium endpoints"""
    
    api_key = "m1HzjYgss43pOkJZcWTr2tuKvRvOPM4W"
    
    print(f"\n" + "="*60)
    print("GETTING REAL AVORO CAPITAL 13F DATA")
    print("="*60)
    
    # Avoro Capital CIK
    cik = "0001633313"
    
    # Try the institutional portfolio endpoint
    try:
        print(f"🔍 Getting Avoro portfolio holdings (CIK: {cik})...")
        
        url = f"https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-holdings?cik={cik}&apikey={api_key}"
        
        response = requests.get(url, timeout=20)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS! Got Avoro holdings data")
            print(f"Data type: {type(data)}")
            
            if isinstance(data, list) and len(data) > 0:
                print(f"📊 Found {len(data)} holdings")
                
                # Process the holdings data
                holdings = []
                for item in data:
                    if isinstance(item, dict):
                        holding = {
                            'company': item.get('securityName', item.get('companyName', '')),
                            'ticker': item.get('symbol', ''),
                            'cusip': item.get('cusip', ''),
                            'shares': item.get('sharesNumber', 0),
                            'value': item.get('marketValue', 0),
                            'percentage': item.get('percentage', 0),
                            'date': item.get('date', ''),
                            'fund': 'Avoro Capital Advisors LLC',
                            'cik': cik
                        }
                        holdings.append(holding)
                
                if holdings:
                    # Create DataFrame and export
                    df = pd.DataFrame(holdings)
                    df = df.sort_values('value', ascending=False)  # Sort by value
                    
                    # Export to CSV and Excel
                    df.to_csv('avoro_real_13f_premium.csv', index=False)
                    df.to_excel('avoro_real_13f_premium.xlsx', index=False)
                    
                    print(f"✅ REAL DATA EXPORTED!")
                    print(f"Files created:")
                    print(f"- avoro_real_13f_premium.csv")
                    print(f"- avoro_real_13f_premium.xlsx")
                    
                    # Display summary
                    total_value = df['value'].sum()
                    print(f"\n📊 AVORO CAPITAL REAL 13F SUMMARY:")
                    print(f"Total Portfolio Value: ${total_value:,.0f}")
                    print(f"Number of Holdings: {len(df)}")
                    
                    print(f"\n🏆 TOP 10 HOLDINGS:")
                    top_10 = df.head(10)[['company', 'ticker', 'shares', 'value', 'percentage']]
                    print(top_10.to_string(index=False))
                    
                    return df
                
            else:
                print(f"📋 Data structure: {data}")
                
        else:
            print(f"❌ Failed to get Avoro data: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error getting Avoro data: {e}")
    
    return None

def get_institutional_ownership_approach():
    """Alternative approach: Check institutional ownership for biotech stocks"""
    
    api_key = "m1HzjYgss43pOkJZcWTr2tuKvRvOPM4W"
    
    print(f"\n" + "="*60)
    print("ALTERNATIVE: INSTITUTIONAL OWNERSHIP SEARCH")
    print("="*60)
    
    # Biotech stocks that Avoro likely holds
    biotech_stocks = [
        'MRNA', 'GILD', 'VRTX', 'BIIB', 'AMGN', 'REGN', 
        'ILMN', 'BMY', 'ABBV', 'LLY', 'MRK', 'PFE'
    ]
    
    avoro_holdings = []
    
    for stock in biotech_stocks:
        try:
            print(f"\n🔍 Checking institutional holders for {stock}...")
            
            url = f"https://financialmodelingprep.com/api/v3/institutional-holder/{stock}?apikey={api_key}"
            
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if isinstance(data, list):
                    print(f"   Found {len(data)} institutional holders")
                    
                    # Look for Avoro
                    for holder in data:
                        holder_name = holder.get('holder', '').lower()
                        
                        if 'avoro' in holder_name:
                            print(f"   ✅ FOUND AVORO in {stock}!")
                            
                            avoro_holdings.append({
                                'company': holder.get('holder', ''),
                                'ticker': stock,
                                'shares': holder.get('sharesNumber', 0),
                                'value': holder.get('marketValue', 0),
                                'percentage': holder.get('percentage', 0),
                                'date': holder.get('dateReported', ''),
                                'fund': 'Avoro Capital Advisors LLC'
                            })
                
            else:
                print(f"   ❌ Failed: {response.status_code}")
            
            # Rate limiting
            time.sleep(0.3)
            
        except Exception as e:
            print(f"   Error: {e}")
            continue
    
    if avoro_holdings:
        print(f"\n✅ FOUND {len(avoro_holdings)} AVORO HOLDINGS!")
        
        df = pd.DataFrame(avoro_holdings)
        df = df.sort_values('value', ascending=False)
        
        # Export
        df.to_csv('avoro_institutional_search.csv', index=False)
        df.to_excel('avoro_institutional_search.xlsx', index=False)
        
        print(f"Files created:")
        print(f"- avoro_institutional_search.csv")
        print(f"- avoro_institutional_search.xlsx")
        
        total_value = df['value'].sum()
        print(f"\nTotal Found Value: ${total_value:,.0f}")
        print(f"\nHoldings Found:")
        print(df[['ticker', 'shares', 'value', 'percentage']].to_string(index=False))
        
        return df
    
    return None

def main():
    print("FMP PREMIUM 13F DATA SCRAPER")
    print("="*40)
    print("Testing upgraded FMP account with institutional data access...")
    
    # Test what premium endpoints are now available
    working_endpoints = test_premium_endpoints()
    
    # Try to get real Avoro 13F data
    avoro_data = get_avoro_13f_data()
    
    # If direct approach doesn't work, try institutional search
    if avoro_data is None:
        print(f"\n🔄 Trying alternative institutional ownership search...")
        avoro_data = get_institutional_ownership_approach()
    
    # Final summary
    print(f"\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    
    if avoro_data is not None:
        print(f"🎉 SUCCESS! Retrieved real Avoro Capital 13F data")
        print(f"📊 Holdings found: {len(avoro_data)}")
        print(f"💰 Total value: ${avoro_data['value'].sum():,.0f}")
    else:
        print(f"❌ Could not retrieve Avoro 13F data")
        print(f"This could mean:")
        print(f"1. Q1 2025 data not yet available in FMP")
        print(f"2. Avoro holdings are in different stocks than tested")
        print(f"3. Data might be under different company name")
    
    print(f"\n✅ FMP Premium endpoints tested: {len(working_endpoints)} working")
    print(f"✅ Framework ready for all 16 hedge funds")

if __name__ == "__main__":
    main()