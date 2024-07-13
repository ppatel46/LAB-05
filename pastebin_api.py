import requests

def create_paste(title, body, expiration='1M', listed=False):
    """
    Create a new PasteBin paste.
    
    Parameters:
        title (str): Title of the paste
        body (str): Body text of the paste
        expiration (str): Expiration time of the paste (default: 1M)
        listed (bool): Whether the paste is publicly listed (default: False)
    
    Returns:
        str: URL of the newly created paste, or None if unsuccessful
    """
    pastebin_api_key = '9F4Nl6yPjt4X5WmruyS1daTiJXMwsBPA'
    pastebin_url = 'https://pastebin.com/api/api_post.php'

    data = {
        'api_dev_key': pastebin_api_key,
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }

    response = requests.post(pastebin_url, data=data)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Test function (you can remove or comment this part for final submission)
if __name__ == '__main__':
    url = create_paste("Test Paste", "This is a test paste.", '10M', False)
    if url:
        print(f"Paste created: {url}")
    else:
        print("Failed to create paste.")
