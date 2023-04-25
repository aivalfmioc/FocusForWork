import requests
import json
# Define the API endpoint URL
url = "https://website-categorization.whoisxmlapi.com/api/v2"

# Define the API parameters (apiKey and domainName)
api_key = "tsgsrgw534233#!"        #"at_gZJHNU0sr872TGAz2i0DIVBq4TsAG"
# domain_name = "https://www.youtube.com/watch?v=mJ3rP3S7h_c" // url
def getclassification(domain_name):
    params = {
        "apiKey": api_key,
        "domainName": domain_name
    }
    # Make the API request using the requests library
    response = requests.get(url, params=params)

    # Get the API response content as a JSON object
    response_json = response.json()
    #HERE
    # Convert the JSON string to a Python dictionary
    #data = json.loads(response_json)
    try:
        # Extract the categories list from the dictionary
        categories = response_json['categories']
        # Find the category with the maximum confidence value
        print(categories)
        max_confidence = 0
        result = None
        for category in categories:
            confidence_tier1 = category['tier1']['confidence']
            if confidence_tier1 > max_confidence:
                max_confidence = confidence_tier1
                result = category

        # get category with highest confidence rate
        max_category = max(categories, key=lambda x: x['tier1']['confidence'])

        # get max confidence rate
        max_confidence = max_category['tier1']['confidence']
        # Extract the tier1 and tier2 values of the category with the maximum confidence
        tier1 = result['tier1']['name']
        tier2 = result['tier2']['name']
        print(tier1)
        return tier1
    except:
        print("the domain is not valid")