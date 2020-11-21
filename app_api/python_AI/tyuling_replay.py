import json
import urllib.request
tuling_key='bc84fe730bc756e8a421051121343138'
api_url = "https://api.ownthink.com/bot"

class tyuling_replay:
    def __init__(self):
        print('开始构建DBUtil')
    def get_message(message,userid):
        req = {
         "spoken":message,
            "appid": tuling_key,
            "userid": userid
        # "perception":
        # {
        #     "inputText":
        #     {
        #         "text": message
        #     },
        #
        #     "selfInfo":
        #     {
        #         "location":
        #         {
        #             "city": "",
        #             "province": "",
        #             "street": ""
        #         }
        #     }
        # },
        # "userInfo":
        # {
        #     "appid": tuling_key,
        #     "userid": userid
        # }
        }
        req = json.dumps(req).encode('utf8')
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        response_dic = json.loads(response_str)
        results_code = response_dic['data']['type']
        print(results_code)
        if results_code == 5000:
            results_text =response_dic['data']['info']['text']
        else:
            results_text = "换个问问呢"
        return results_text