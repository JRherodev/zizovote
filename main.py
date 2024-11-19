import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

while True :
	

	r = requests.session() 
	
	params = {
	    'action': 'totalpoll',
	}
	
	data = MultipartEncoder({
	    'totalpoll[choices][b68a6b97-9977-41ed-bc39-9f847462fb34][]': (None, 'd0ed83a9-530d-4936-a148-55df1bac4397'),
	    'totalpoll[screen]': (None, 'vote'),
	    'totalpoll[pollId]': (None, '277'),
	    'totalpoll[action]': (None, 'vote'),
	})
	
	headers = {
	    'authority': 'thebestegypt.quest',
	    'accept': '*/*',
	    'accept-language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': data.content_type,
	    'origin': 'https://thebestegypt.quest',
	    'referer': 'https://thebestegypt.quest/ep-voting/%d9%84%d8%a7%d8%b9%d8%a8/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	response = r.post(
	    'https://thebestegypt.quest/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	   
	)
	stuts= response.status_code
	
	
	
	if ' لا يمكنك التصويت مجدداً' in response.text :
		print('FILED TO VOTING ❌',stuts)
		
	else :
		print(' VOTING SUCCESSFUL TO ZIZO ✅',stuts )	
		