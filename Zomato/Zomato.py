import json
with open('data-2026216105652.json','r') as f:
    data = json.load(f)

result = []
All_data=data.get('page_data').get('sections')
res_url=data.get('page_info').get('canonicalUrl')
final_menu={}

if All_data:
    rest_id = All_data.get('SECTION_BASIC_INFO').get('res_id')
    name = All_data.get('SECTION_BASIC_INFO').get('name')
    res_cont = All_data.get('SECTION_RES_CONTACT').get('phoneDetails').get('phoneStr')

    address={
        'full_addr' :All_data.get('SECTION_RES_CONTACT').get('address'),
        'region' :All_data.get('SECTION_RES_CONTACT').get('country_name'),
        'city' : All_data.get('SECTION_RES_CONTACT').get('city_name'),
        'pincode':All_data.get('SECTION_RES_CONTACT').get('zipcode'),

    },
    cui= All_data.get('SECTION_RES_HEADER_DETAILS').get('CUISINES')
    cuisines=[
        {
            'name':c.get('name'),
            'url':c.get('url')
        }
        for c in cui
    ],
    time = All_data.get('SECTION_BASIC_INFO').get('timing').get('customised_timings').get('opening_hours')

    for t in time:
        timings ={
            'timimgs': t.get('timing'),
            'days':t.get('days')
        }
menu = data.get('page_data').get('order').get('menuList').get('menus')
menu_categories = []

for item in menu:
    categories = item.get('menu').get('categories')
    
    items = []
    
    for category in categories:
        for subitem in category.get('category').get('items'):
            nesteditem = subitem.get('item')
            
            temp = {
                "item_id": nesteditem.get('id'),
                "item_name": nesteditem.get('name'),
                "item_slugs": nesteditem.get('tag_slugs'),
                "item_url": '',
                "item_description": nesteditem.get('desc'),     
                "item_price": '',
                "is_veg": True if nesteditem.get('dietary_slugs')[0] == True else False
            }
            
            items.append(temp)
    
    category_data = {
        "category_name": item.get('menu').get('name'),
        "items": items
    }

    menu_categories.append(category_data)

output={
    'rest_id':rest_id,
    'name':name,
    'res_url' :res_url,
    'res_cont':res_cont,
    'address':address,
    'cuisines':cuisines,
    'timings':timings,
    'menu_categories':menu_categories

}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2,ensure_ascii=False)


