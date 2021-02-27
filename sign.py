# -- coding: utf-8 --
# @Time : 2021/2/27 14:02
# @Author : Los Angeles Clippers
# @Email: 229456906@qq.com
# @sinaemail: angelesclippers@sina.com


import execjs
import requests
import re
import json


def get_sign():
    with open('sign.js', 'r') as f:
        js = f.read()
        f.close()

    sign = execjs.compile(js).call('e', '兔子')
    print(sign)
    return sign


def get_token():
    url = 'https://fanyi.baidu.com/?aldtype=16047'
    headers = {
        'Cookie': 'BIDUPSID=6ED20C8A993C162F592CBBCACFB3BA60; PSTM=1614007307; BAIDUID=6ED20C8A993C162FA88B4C229F31B844:FG=1; __yjs_duid=1_17fddf46c44f2d2c3b304d20c30d4a101614176173764; BAIDUID_BFESS=6ED20C8A993C162FA88B4C229F31B844:FG=1; BDRCVFR[n9IS1zhFc9f]=mk3SLVN4HKm; delPer=0; PSINO=7; H_PS_PSSID=33516_33357_33273_31660_33570_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=7093079150575847613; BDSFRCVID=zqKOJexroG3VnU3eMoohEXw3ALweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJKJoDt-JKK3fP36qR6sMJ8thmT22-us35RT2hcH0KLKoxOhefJ8bDuzBN34Xnb8LJriLp6eWfb1MRjvWxQk2q533-DqLM5X2JAHWl5TtUJ6JKnTDMRh-lIeWtvyKMniQKT9-pny0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDTK2e55QjGAshRTLHDbhLnn_MCD_HnurbDcvXUI8LNDHXtc-bjRn0Ro45nopo-3yQ-_bX-DyXnO7ttoyJKbnLhn5MUccKJ7vWJJ45UL1Db0OhTvMtg3t3DQ6Lpooepvo3Poc3MkbLPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtRk8oK-atDvqKROkq4cE-t4hMMoXetJyaR3BBqOvWJ5WqR7jDpj-WbK8XfnraxQvbb7CXxOkMJbjShbXXMorQMCp-qbpQJbW3HcM2M373l02V-b3XxjVWxnDhp7LBPRMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCaePDyqx5Ka43tHD7yWCvL-lvcOR59K4nnDpKH3Hb-W4Ry2gTvLKOpBP3qsI3P3MOZXMLg5n7Tbb8eBgvZ2UQF5l8-sq0x0bO5DDuOQq_L0xvJ5IOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_tTD8tb6P; BCLID_BFESS=7093079150575847613; BDSFRCVID_BFESS=zqKOJexroG3VnU3eMoohEXw3ALweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJKJoDt-JKK3fP36qR6sMJ8thmT22-us35RT2hcH0KLKoxOhefJ8bDuzBN34Xnb8LJriLp6eWfb1MRjvWxQk2q533-DqLM5X2JAHWl5TtUJ6JKnTDMRh-lIeWtvyKMniQKT9-pny0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDTK2e55QjGAshRTLHDbhLnn_MCD_HnurbDcvXUI8LNDHXtc-bjRn0Ro45nopo-3yQ-_bX-DyXnO7ttoyJKbnLhn5MUccKJ7vWJJ45UL1Db0OhTvMtg3t3DQ6Lpooepvo3Poc3MkbLPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtRk8oK-atDvqKROkq4cE-t4hMMoXetJyaR3BBqOvWJ5WqR7jDpj-WbK8XfnraxQvbb7CXxOkMJbjShbXXMorQMCp-qbpQJbW3HcM2M373l02V-b3XxjVWxnDhp7LBPRMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCaePDyqx5Ka43tHD7yWCvL-lvcOR59K4nnDpKH3Hb-W4Ry2gTvLKOpBP3qsI3P3MOZXMLg5n7Tbb8eBgvZ2UQF5l8-sq0x0bO5DDuOQq_L0xvJ5IOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_tTD8tb6P; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1614404675; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1614405111; ab_sr=1.0.0_ZmYwNmMwYTMwOTY1ZjdiYWU5NjIzZDcxZDhiNDJlZGJiMTdiZDc3ZDIyYTkyZTIxODcxZWM1NjUyYmJmNzZhY2IwMGViYWE2NGY0M2Y4ZWQwM2FmNTViMDk0Zjk0ZTg2; __yjsv5_shitong=1.0_7_7761e7b1ad9072852af05b64edf30315e171_300_1614405112502_1.206.246.215_77aafa3d',
        'Host': 'fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    token = re.search(r"token: '(.*?)'", response).group(1)
    print(token)
    return token


def fanyi(sign, token):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    data = {
        'from': 'zh',
        'to': 'en',
        'query': '兔子',
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
        'domain': 'common',
    }
    headers = {
        'Cookie': 'BIDUPSID=6ED20C8A993C162F592CBBCACFB3BA60; PSTM=1614007307; BAIDUID=6ED20C8A993C162FA88B4C229F31B844:FG=1; __yjs_duid=1_17fddf46c44f2d2c3b304d20c30d4a101614176173764; BAIDUID_BFESS=6ED20C8A993C162FA88B4C229F31B844:FG=1; BDRCVFR[n9IS1zhFc9f]=mk3SLVN4HKm; delPer=0; PSINO=7; H_PS_PSSID=33516_33357_33273_31660_33570_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=7093079150575847613; BDSFRCVID=zqKOJexroG3VnU3eMoohEXw3ALweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJKJoDt-JKK3fP36qR6sMJ8thmT22-us35RT2hcH0KLKoxOhefJ8bDuzBN34Xnb8LJriLp6eWfb1MRjvWxQk2q533-DqLM5X2JAHWl5TtUJ6JKnTDMRh-lIeWtvyKMniQKT9-pny0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDTK2e55QjGAshRTLHDbhLnn_MCD_HnurbDcvXUI8LNDHXtc-bjRn0Ro45nopo-3yQ-_bX-DyXnO7ttoyJKbnLhn5MUccKJ7vWJJ45UL1Db0OhTvMtg3t3DQ6Lpooepvo3Poc3MkbLPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtRk8oK-atDvqKROkq4cE-t4hMMoXetJyaR3BBqOvWJ5WqR7jDpj-WbK8XfnraxQvbb7CXxOkMJbjShbXXMorQMCp-qbpQJbW3HcM2M373l02V-b3XxjVWxnDhp7LBPRMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCaePDyqx5Ka43tHD7yWCvL-lvcOR59K4nnDpKH3Hb-W4Ry2gTvLKOpBP3qsI3P3MOZXMLg5n7Tbb8eBgvZ2UQF5l8-sq0x0bO5DDuOQq_L0xvJ5IOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_tTD8tb6P; BCLID_BFESS=7093079150575847613; BDSFRCVID_BFESS=zqKOJexroG3VnU3eMoohEXw3ALweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJKJoDt-JKK3fP36qR6sMJ8thmT22-us35RT2hcH0KLKoxOhefJ8bDuzBN34Xnb8LJriLp6eWfb1MRjvWxQk2q533-DqLM5X2JAHWl5TtUJ6JKnTDMRh-lIeWtvyKMniQKT9-pny0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDTK2e55QjGAshRTLHDbhLnn_MCD_HnurbDcvXUI8LNDHXtc-bjRn0Ro45nopo-3yQ-_bX-DyXnO7ttoyJKbnLhn5MUccKJ7vWJJ45UL1Db0OhTvMtg3t3DQ6Lpooepvo3Poc3MkbLPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtRk8oK-atDvqKROkq4cE-t4hMMoXetJyaR3BBqOvWJ5WqR7jDpj-WbK8XfnraxQvbb7CXxOkMJbjShbXXMorQMCp-qbpQJbW3HcM2M373l02V-b3XxjVWxnDhp7LBPRMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCaePDyqx5Ka43tHD7yWCvL-lvcOR59K4nnDpKH3Hb-W4Ry2gTvLKOpBP3qsI3P3MOZXMLg5n7Tbb8eBgvZ2UQF5l8-sq0x0bO5DDuOQq_L0xvJ5IOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_tTD8tb6P; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1614404675; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1614405111; ab_sr=1.0.0_ZmYwNmMwYTMwOTY1ZjdiYWU5NjIzZDcxZDhiNDJlZGJiMTdiZDc3ZDIyYTkyZTIxODcxZWM1NjUyYmJmNzZhY2IwMGViYWE2NGY0M2Y4ZWQwM2FmNTViMDk0Zjk0ZTg2; __yjsv5_shitong=1.0_7_7761e7b1ad9072852af05b64edf30315e171_300_1614405112502_1.206.246.215_77aafa3d',
        'Host': 'fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    response = requests.post(url, data=data, headers=headers).text
    jsData = json.loads(response)
    print(jsData)


if __name__ == '__main__':
    sign = get_sign()
    token = get_token()
    fanyi(sign=sign, token=token)