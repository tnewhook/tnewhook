#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install requests beautifulsoup4


# In[97]:


import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import time


# In[98]:


def get_page_content(url, head):
  """
  Function to get the page content
  """
  req = Request(url, headers=head)
  return urlopen(req)

#url = 'https://www.sweetmarias.com/green-coffee.html?product_list_limit=all'
url='https://www.sweetmarias.com/green-coffee.html?product_list_limit=all&sm_status=1'
head = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive',
  'refere': 'https://example.com',
  'cookie': """your cookie value ( you can get that from your web page) """
}


response = get_page_content(url, head).read()
# print(response)


# In[99]:


# Parse the HTML content
soup = BeautifulSoup(response, 'html.parser')


# In[100]:


# Find all product links in the 'Name' column
product_links = soup.find_all('a', class_='product-item-link')
urls=[]


# In[101]:


product_links


# In[102]:


for link in product_links:
    product_url = link['href']
    product_name = link.text.strip()
    print("URL: " + product_url+" Name: "+ product_name)
#     names.append(product_name)
    urls.append(product_url)


# In[104]:


product_info = []
for link in product_links:
    product_url = link['href']
    product_name = link.text.strip()
    
    # Send a GET request to the product page
    product_response = get_page_content(product_url, head).read()
    print("URL: " + product_url)
    # print(product_response)
    # Parse the product page HTML content
    product_soup = BeautifulSoup(product_response, 'html.parser')
    
    #add product info to array
    product_info.append(product_soup)
    time.sleep(5)


# In[169]:


#define lists
# Initialize lists to store the data
names = []
descriptions = []
prices=[]
cupping_notes=[]
process_methods = []
cultivars = []
farm_gates = []
regions = []
processings = []
drying_methods = []
arrival_dates = []
lot_sizes = []
bag_sizes = []
packagings = []
cultivars = []
cultivar_details = []
grades = []
appearances = []
roast_recommendations = []
types = []
# flavor_charts = []
# cupping_charts = []
total_scores = []

#CuppingNotes
DryFragrances = []
WetAromas = []
Brightnesses = []
Flavors = []
CupBodies = []
Finishes = []
Sweetnesses = []
CleanCups = []
Complexities = []
Uniformities = []

#Flavor Chart
Florals = []
Honeys = []
Sugars = []
Caramels = []
Fruits = []
Citruss = []
Berries = []
Cocoas = []
Nuts = []
Rustics = []
Spices = []
FlavorBodies = []


# In[170]:


# Extract the product info
for product in product_info:
#     if name=='Burundi Dry Process Gahahe':
# #         print(product)
#         break
        
    print("\n\n----------------------------------------------")
    
    name='N/A'
    price='N/A'
    total_score='N/A'
    description = 'N/A'
    region='N/A'
    processing='N/A'
    process_method='N/A'
    drying_method='N/A'
    arrival_date='N/A'
    lot_size='N/A'
    bag_size='N/A'
    packaging='N/A'
    cultivar='N/A'
    cultivar_detail='N/A'
    farm_gate='N/A'
    grade='N/A'
    estate='N/A'
    appearance='N/A'
    roast_recommendation='N/A'
    type_='N/A'
    appearance='N/A'
#     cuppingNotes='N/A'
#     flavor_chart='N/A'

#     cupping_chart
    DryFragrance=0
    WetAroma=0
    Brightness=0
    Flavor=0
    CupBody=0
    Finish=0
    Sweetness=0
    CleanCup=0
    Complexity=0
    Uniformity=0


#     Flavor_chart
    Floral=0
    Honey=0
    Sugar=0
    Caramel=0
    Fruit=0
    Citrus=0
    Berry=0
    Cocoa=0
    Nut=0
    Rustic=0
    Spice=0
    FlavorBody=0
 
    #Cupping Notes
    
    name_span = product.find('span', class_='base')
    if name_span!= None:
        name = name_span.text.strip()
        print("Name:" + name)
        
    
    
    price_wrapper = product.find('span',class_='price-wrapper')
    if price_wrapper!=None:
        price = price_wrapper.text.strip() 
        price = price.replace('$','')
        print("Price: " + price)
        
    

    # Extract the product description
    description_span = product.find('div', class_='value') 
    if description_span != None:
        description_p = description_span.find('p')
        description = description_p.text.strip()
        print("Description: " + description)
        
    
    
    cupping_notes_div =  product.find('div',class_='product attribute cupping-notes')
    if cupping_notes_div != None:   
        cuppingNotes=cupping_notes_div.find('div',class_='value')
        cuppingNotes = cuppingNotes.text.strip()
   

    
    scoreInfo = product.find('div',class_='score-value')
    if scoreInfo !=None:
        total_score =scoreInfo.text.strip()
        print('Total Score: ' + total_score)
        
    
        

    list_info = product.find('div', class_='list-info')
    if list_info:
        items = list_info.find_all('li')
        for item in items:
            strong_text = item.find('strong').text.strip() if item.find('strong') else ''
            span_text = item.find('span').text.strip() if item.find('span') else ''
            if strong_text == 'Process Method':
                process_method = span_text
                print('Process Method: ' + process_method)

            elif strong_text == 'Cultivar':
                cultivar = span_text
                print('Cultivar: ' + cultivar)

            elif strong_text == 'Farm Gate':
                farm_gate = span_text
                print('Farm Gate: ' + farm_gate)

    attributes_table = product.find('table', id='product-attribute-specs-table')
    if attributes_table:
        rows = attributes_table.find_all('tr')
        for row in rows:
            th_text = row.find('th').text.strip() if row.find('th') else ''
            td_text = row.find('td').text.strip() if row.find('td') else ''

            if th_text == 'Region':
                region = td_text
                print('Region: ' + region)
                
            
                
            elif th_text == 'Processing':
                processing = td_text
                print('Processing: ' + processing)
                
            
                
            elif th_text == 'Drying Method':
                drying_method = td_text
                print('Drying: ' + drying_method)
                
            elif th_text == 'Arrival date':
                arrival_date = td_text
                print('Arrival date: ' + arrival_date)
                
            elif th_text == 'Lot size':
                lot_size = td_text
                print('Lot size: ' + lot_size)
                
            elif th_text == 'Bag size':
                bag_size = td_text
                print('Bag size: ' + bag_size)

            elif th_text == 'Packaging':
                packaging = td_text
                print('Packaging: ' + packaging)

            elif th_text == 'Cultivar Detail':
                cultivar_detail = td_text
                print('Cultivar Detail: ' + cultivar_detail)
                
            elif th_text == 'Grade':
                grade = td_text
                print('Grade: ' + grade)
                
            elif th_text == "Appearance":
                appearance = td_text
                print('Appearance: ' + appearance)
                
            elif th_text == 'Roast Recommendations':
                roast_recommendation = td_text
                print('Roast Recommendations: ' + roast_recommendation)
                
            elif th_text == 'Type':
                type_ = td_text
                print('Type: ' + type_)
                
    # Extract cupping chart information
    
    cupping_chart_div = product.find('div', {'data-chart-id': 'cupping-chart'})
    if cupping_chart_div:
        cupping_chart_values = cupping_chart_div.get('data-chart-value', 'N/A')
        cupping_chart = {k: float(v) for k, v in (item.split(':') for item in cupping_chart_values.split(','))}
        print('Cupping chart: ')
        print(cupping_chart)
        DryFragrance=cupping_chart['Dry Fragrance']
        WetAroma=cupping_chart['Wet Aroma']
        Brightness=cupping_chart['Brightness']
        Flavor=cupping_chart['Flavor']
        CupBody=cupping_chart['Body']
        Finish=cupping_chart['Finish']
        Sweetness=cupping_chart['Sweetness']
        CleanCup=cupping_chart['Clean Cup']
        Complexity=cupping_chart['Complexity']
        Uniformity=cupping_chart['Uniformity']
        print("Dry Fragrance" + str(DryFragrance))
        print("Wet Aroma: " + str(WetAroma))
        print("Brightness: " + str(Brightness))
        print("Flavor: " + str(Flavor))
        print("Cup Body: " + str(CupBody))
        print("Finish: " + str(Finish))
        print("Sweetness: " + str(Sweetness))
        print("CleanCup: " + str(CleanCup))
        print("Complexity: " + str(Complexity))
        print("Uniformity: " + str(Uniformity))
        
    flavor_chart_div = product.find('div', {'data-chart-id': 'flavor-chart'})
    if flavor_chart_div:
        flavor_chart_values = flavor_chart_div.get('data-chart-value', 'N/A')
        flavor_chart = {k: float(v) for k, v in (item.split(':') for item in flavor_chart_values.split(','))}
        print('Flavor chart: ')
        print(flavor_chart)
        Floral=flavor_chart["Floral"]
        Honey=flavor_chart["Honey"]
        Sugar=flavor_chart["Sugars"]
        Caramel=flavor_chart["Caramel"]
        Fruit=flavor_chart["Fruits"]
        Citrus=flavor_chart["Citrus"]
        Berry=flavor_chart["Berry"]
        Cocoa=flavor_chart["Cocoa"]
        Nut=flavor_chart["Nuts"]
        Rustic=flavor_chart["Rustic"]
        Spice=flavor_chart["Spice"]
        FlavorBody=flavor_chart["Body"]
        print("Floral: " + str(Floral))
        print("Honey: " + str(Honey))
        print("Sugar: " + str(Sugar))
        print("Caramel: " + str(Caramel))
        print("Fruit: " + str(Fruit))
        print("Citrus: " + str(Citrus))
        print("Berry: " + str(Berry))
        print("Cocoa: " + str(Cocoa))
        print("Nut: " + str(Nut))
        print("Rustic: " + str(Rustic))
        print("Spice: " + str(Spice))
        print("Flavor Body: " + str(Body))
        
    names.append(name)
    prices.append(price)
    descriptions.append(description) 
#     cupping_notes.append(cuppingNotes)
    total_scores.append(total_score)
    process_methods.append(process_method)
    cultivars.append(cultivar)
    farm_gates.append(farm_gate)
    regions.append(region)
    processings.append(processing)
    drying_methods.append(drying_method)
    arrival_dates.append(arrival_date)
    lot_sizes.append(lot_size)
    bag_sizes.append(bag_size)
    packagings.append(packaging)
    cultivar_details.append(cultivar_detail)
    grades.append(grade)
    appearances.append(appearance)
    roast_recommendations.append(roast_recommendation)
    types.append(type_)

#CuppingNotes
    DryFragrances.append(DryFragrance)
    WetAromas.append(WetAroma)
    Brightnesses.append(Brightness)
    Flavors.append(Flavor)
    CupBodies.append(CupBody)
    Finishes.append(Finish)
    Sweetnesses.append(Sweetness)
    CleanCups.append(CleanCup)
    Complexities.append(Complexity)
    Uniformities.append(Uniformity)

#FlavorChart
    Florals.append(Floral)
    Honeys.append(Honey)
    Sugars.append(Sugar)
    Caramels.append(Caramel)
    Fruits.append(Fruit)
    Citruss.append(Citrus)
    Berries.append(Berry)
    Cocoas.append(Cocoa)
    Nuts.append(Nut)
    Rustics.append(Rustic)
    Spices.append(Spice)
    FlavorBodies.append(FlavorBody)
              
#     cupping_charts.append(cupping_chart)
#     flavor_charts.append(flavor_chart)


# In[119]:





# In[171]:


#error checking
print(f'names length: {len(names)}')
print(f'Prices length: {len(prices)}')
print(f'descriptions length: {len(descriptions)}')
print(f'total_scores length: {len(total_scores)}')
print(f'process_methods length: {len(process_methods)}')
print(f'cultivars length: {len(cultivars)}')
print(f'Farm gates length: {len(farm_gates)}')
print(f'regions length: {len(regions)}')
print(f'processings length: {len(processings)}')
print(f'drying_methods length: {len(drying_methods)}')
print(f'arrival_dates length: {len(arrival_dates)}')
print(f'lot_sizes length: {len(lot_sizes)}')
print(f'bag_sizes length: {len(bag_sizes)}')
print(f'packagings length: {len(packagings)}')
print(f'cultivar_details length: {len(cultivar_details)}')
print(f'grades length: {len(grades)}')
print(f'appearances length: {len(appearances)}')
print(f'roast_recommendations length: {len(roast_recommendations)}')
print(f'types length: {len(types)}')
# print(f'flavor_charts length: {len(flavor_charts)}')
# print(f'cupping_charts length: {len(cupping_charts)}')

print('\nCuppingNotes')
print(f'DryFragrance length: {len(DryFragrances)}')
print(f'WetAroma length: {len(WetAromas)}')
print(f'Brightness length: {len(Brightnesses)}')
print(f'Flavor length: {len(Flavors)}')
print(f'CupBody length: {len(CupBodies)}')
print(f'Finish length: {len(Finishes)}')
print(f'Sweetness length: {len(Sweetnesses)}')
print(f'CleanCup length: {len(CleanCups)}')
print(f'Complexity length: {len(Complexities)}')
print(f'Uniformity length: {len(Uniformities)}')

print("\nFlavorChart")
print(f'Floral length: {len(Florals)}')
print(f'Honey length: {len(Honeys)}')
print(f'Sugar length: {len(Sugars)}')
print(f'Caramel length: {len(Caramels)}')
print(f'Fruit length: {len(Fruits)}')
print(f'Citrus length: {len(Citruss)}')
print(f'Berry length: {len(Berries)}')
print(f'Cocoa length: {len(Cocoas)}')
print(f'Nuts length: {len(Nuts)}')
print(f'Rustic length: {len(Rustics)}')
print(f'Spice length: {len(Spices)}')
print(f'FlavorBody length: {len(FlavorBodies)}')
print(f'cuppingNotes length: {len(cuppingNotes)}')


# In[182]:


#add to dataframe
df = pd.DataFrame({
    'Name': names,
    'Description': descriptions,
    'Process Method': process_methods,
    'Total Score': total_scores,
    'Cultivar': cultivars,
    'Farm Gate': farm_gates,
    'Region': regions,
    'Processing': processings,
    'Drying Method': drying_methods,
    'Arrival Date': arrival_dates,
    'Lot Size': lot_sizes,
    'Bag Size': bag_sizes,
    'Packaging': packagings,
    'Cultivar Detail': cultivar_details,
    'Grade': grades,
    'Appearance': appearances,
    'Roast Recommendations': roast_recommendations,
    'Type': types,
#     'Flavor Chart': flavor_charts,
#     'Cupping Chart': cupping_charts,
    
# #Cupping Chart
     'DryFragrance': DryFragrances,
     'WetAroma': WetAromas,
     'Brightness': Brightness,
     'Flavor': Flavors,
     'CupBody': CupBodies,
     'Finish': Finishes,
     'Sweetness': Sweetnesses,
     'CleanCup': CleanCups,
     'Complexity': Complexities,
     'Uniformity': Uniformities,

#FlavorChart': ,
    'Floral': Florals,
    'Honey': Honeys,
    'Sugar': Sugars,
    'Caramel': Caramels,
    'Fruit': Fruits,
    'Citrus': Citruss,
    'Berry': Berries,
    'Cocoa': Cocoas,
    'Nuts': Nuts,
    'Rustic': Rustics,
    'Spice': Spices,
    'FlavorBody': FlavorBodies
})

df
#df.to_csv('sweet_marias_green_coffee.csv', index=False)


# In[183]:


df

