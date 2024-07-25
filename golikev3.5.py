
try :
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from tabulate import tabulate
    import re
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'VUI LONG CHO : {:02d}'.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
def TIKTOKINFO():
    url1_2 = 'https://gateway.golike.net/api/tiktok-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_tiktok1 = []
    account_id1 = []
    STT = []
    STATUS =[]
    print('CAC TAI KHOAN DANG HOAT DONG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    # LIST=Fore.RED+tabulate(mydata, headers=head, tablefmt="grid",)
    for data in checkurl1_2['data'] :
        usernametk = data['nickname']
        # print(str(i)+'.'+usernametk)
        user_tiktok1.append(data['nickname'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN+"DANG HOAT DONG"+Fore.RED)
    # create header
        i=i+1
    table = zip(STT,user_tiktok1,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHAP TAI KHOAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_tiktok1) :
        user_tiktok1 = user_tiktok1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_tiktok1[0] 
        account_id = account_id1[0]
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        choose = int(input(Fore.RED+'NHAP SO LUONG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        DELAY = int(input(Fore.RED+'NHAP DELAY : '))
        for i in range(choose):
            url2 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id='+str(account_id)+'&data=null'
            checkurl2 = ses.get(url2,headers=headers).json()
            if checkurl2['status'] ==200:
                linkjob = []
                linkjob = str(checkurl2['data']['link'])
                lenjob = len(checkurl2['data']['link'])
                ads_id = checkurl2['data']['id']
                object_id = checkurl2['data']['object_id']
                type = checkurl2['data']['type']
                # os.system("start "+linkjob+"")
                os.system("termux-open-url "+str(linkjob[0:lenjob])+"")
                PARAMS = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
                countdown(DELAY)
                url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                time.sleep(1)
                checkurl3 = ses.post(url3,params=PARAMS).json()
                if checkurl3['status'] == 400 :

                        time.sleep(2)

                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                        checkurl3 = ses.post(url3,params=PARAMS).json()
                        if checkurl3['status'] == 200:
                                prices = checkurl3['data']['prices']
                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                        else:

                                    time.sleep(2)

                                    url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                    checkurl3 = ses.post(url3,params=PARAMS).json()
                                    if checkurl3['status'] == 200:
                                            prices = checkurl3['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                        time.sleep(2)

                                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                        checkurl3 = ses.post(url3,params=PARAMS).json()
                                        if checkurl3['status'] == 200:
                                                prices = checkurl3['data']['prices']
                                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    'async': 'true',
                                                    'data': 'null',
                                                    'type': type,
                                                    }
                elif checkurl3['status'] == 200:
                    prices = checkurl3['data']['prices']
                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                else :
                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                    if checkskipjob['status'] == 200:
                        message = checkskipjob['message']
                        print(Fore.RED+str(message))
                        PARAMSr = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
            else : 
                countdown(15)
                print(checkurl2['message'])
                skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                if checkskipjob['status'] == 200:
                    message = checkskipjob['message']
                    print(Fore.RED+str(message))
                    PARAMSr = {
                    'ads_id' : ads_id,
                    'account_id' : account_id,
                    'object_id' : object_id ,
                    'async': 'true',
                    'data': 'null',
                    'type': type,
                    }        
def TWITTER():
    url1_2 = 'https://gateway.golike.net/api/twitter-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_twitter1 = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    print('CAC TAI KHOAN DANG HOAT DONG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkurl1_2['data'] :
        usernametk = data['screen_name']
        user_twitter1.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        account.append(usernametk)
        STATUS.append(Fore.GREEN+"DANG HOAT DONG"+Fore.RED)
        i=i+1
    table = zip(STT,account,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHAP TAI KHOAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_twitter1) :
        user_twitter1 = user_twitter1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_twitter1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('AUTH'+str(account_id)+'.txt')
        if checkfile == False:
            AUTHURX = input(Fore.GREEN+'[+]''AUTH : ')
            createfile = open('AUTH'+str(account_id)+'.txt','w')
            createfile.write(AUTHURX)
            createfile.close()
            readfile = open('AUTH'+str(account_id)+'.txt','r')
            AUTHURX = readfile.read()
            readfile.close()
        else:
            readfile = open('AUTH'+str(account_id)+'.txt','r')
            AUTHURX = readfile.read()
            readfile.close()
        checkfile2 = os.path.isfile('COOKIE'+str(account_id)+'.txt')
        if checkfile2 == False:
            cookieX = input(Fore.GREEN+'[+]''COOKIE : ')
            createfile = open('COOKIE'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIE'+str(account_id)+'.txt','r')
            cookieX = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIE'+str(account_id)+'.txt','r')
            cookieX = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        print('[*] COOKIE : ',cookieX)
        print('[*] AUTH : ',AUTHURX)
        print(Fore.RED+'[+] 1 . SU DUNG DU LIEU CU')
        print(Fore.RED+'[+] 2 . XOA DU LIEU')
        URchoose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
        if URchoose == 2:
             os.remove('COOKIE'+str(account_id)+'.txt')
             os.remove('AUTH'+str(account_id)+'.txt')
             return 0
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        choose = int(input(Fore.RED+'NHAP SO LUONG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        DELAY = int(input(Fore.RED+'NHAP DELAY : '))
        for i in range(choose):
                    job = 'https://gateway.golike.net/api/advertising/publishers/twitter/jobs?account_id='+str(account_id)
                    nos = ses.get(job,headers=headers).json()
                    if nos['status'] ==200:
                        ads_id = nos['data']['id']
                        object_id = nos['data']['object_id']
                        type = nos['data']['type']
                        if type=='like':
                            url = 'https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet'
                            headersX = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/json',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': User_Agent,
                            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                                    }
                            json_data = {
                                'variables': {
                                    'tweet_id': object_id,
                                },
                                'queryId': 'lI07N6Otwv1PhnEgXILM7A',
                            }

                            node = requests.post(url,headers=headersX,json=json_data,proxies=proxyy).json()
                            countdown(DELAY)
                            if 'data' or 'has already favorited tweet' in str(node):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response3 = requests.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()       
                                if response3['success']==True:
                                    prices =response3['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(node):
                                print("HET HAN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
                            else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        elif type == 'follow':
                            url = 'https://x.com/i/api/1.1/friendships/create.json'
                            headersY = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
                            'x-client-transaction-id': 'MPwo7xERotqe3xFS4oEGGDju3YMFR9v2gW2dSTZ/c2S4KYhQfp5ZmZYR/KcwzeyIYp3GBjKulQYFzsWftgEm6c7v0StkMw',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                        }

                            data = {
                            'include_profile_interstitial_type': '1',
                            'include_blocking': '1',
                            'include_blocked_by': '1',
                            'include_followed_by': '1',
                            'include_want_retweets': '1',
                            'include_mute_edge': '1',
                            'include_can_dm': '1',
                            'include_can_media_tag': '1',
                            'include_ext_is_blue_verified': '1',
                            'include_ext_verified_type': '1',
                            'include_ext_profile_image_shape': '1',
                            'skip_status': '1',
                            'user_id': object_id,
                        }

                            response2 = requests.post('https://x.com/i/api/1.1/friendships/create.json', headers=headersY, data=data,proxies=proxyy).json()
                            countdown(DELAY)
                            if 'id' in response2:
                                # DELAY
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(response2):
                                print("HET HAN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
                            else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        elif type=='comment':
                            comment = nos['lock']["message"]
                            url = 'https://x.com/i/api/graphql/oB-5XsHNAbjvARJEc8CZFw/CreateTweet'
                            headersZ = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/json',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': User_Agent,
                            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                                    }
                            json_data = {
                                'variables': {
                                    'tweet_text': comment,
                                    'reply': {
                                        'in_reply_to_tweet_id': object_id,
                                        'exclude_reply_user_ids': [],
                                    },
                                    'dark_request': False,
                                    'media': {
                                        'media_entities': [],
                                        'possibly_sensitive': False,
                                    },
                                    'semantic_annotation_ids': [],
                                },
                                'features': {
                                    'communities_web_enable_tweet_community_results_fetch': True,
                                    'c9s_tweet_anatomy_moderator_badge_enabled': True,
                                    'tweetypie_unmention_optimization_enabled': True,
                                    'responsive_web_edit_tweet_api_enabled': True,
                                    'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                                    'view_counts_everywhere_api_enabled': True,
                                    'longform_notetweets_consumption_enabled': True,
                                    'responsive_web_twitter_article_tweet_consumption_enabled': True,
                                    'tweet_awards_web_tipping_enabled': False,
                                    'creator_subscriptions_quote_tweet_preview_enabled': False,
                                    'longform_notetweets_rich_text_read_enabled': True,
                                    'longform_notetweets_inline_media_enabled': True,
                                    'articles_preview_enabled': True,
                                    'rweb_video_timestamps_enabled': True,
                                    'rweb_tipjar_consumption_enabled': True,
                                    'responsive_web_graphql_exclude_directive_enabled': True,
                                    'verified_phone_label_enabled': False,
                                    'freedom_of_speech_not_reach_fetch_enabled': True,
                                    'standardized_nudges_misinfo': True,
                                    'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                                    'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                                    'responsive_web_graphql_timeline_navigation_enabled': True,
                                    'responsive_web_enhance_cards_enabled': False,
                                },
                                'queryId': 'oB-5XsHNAbjvARJEc8CZFw',
                            }
                            cf = requests.post(url,headers=headersZ,json=json_data,proxies=proxyy).json()
                            countdown(DELAY)  
                            if 'create_tweet' or 'Authorization: Status is a duplicate.' in str(cf):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                'comment_id':nos['lock']['comment_id'],
                                'message':comment,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(cf):
                                print("HET HAN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                            else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                    else:
                        print(nos['message'])
                        countdown(15)
def INSTAGRAM():
    url1_2 = 'https://gateway.golike.net/api/instagram-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_INS = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    print('CAC TAI KHOAN DANG HOAT DONG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkurl1_2['data'] :
        usernametk = data['instagram_username']
        user_INS.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN+"DANG HOAT DONG"+Fore.RED)
        account.append(usernametk)
        i=i+1
    table = zip(STT,account,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHAP TAI KHOAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_INS) :
        user_INS = user_INS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_INS[0] 
        account_id = account_id1[0]
        checkfile2 = os.path.isfile('COOKIEINS'+str(account_id)+'.txt')
        if checkfile2 == False:
            cookieX = input(Fore.GREEN+'[+]''COOKIE : ')
            createfile = open('COOKIEINS'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        print('[*] COOKIE : ',cookieINS)
        print(Fore.RED+'[+] 1 . SU DUNG DU LIEU CU')
        print(Fore.RED+'[+] 2 . XOA DU LIEU')
        URchoose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
        if URchoose == 2:
             os.remove('COOKIEINS'+str(account_id)+'.txt')
             return 0
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        choose = int(input(Fore.RED+'NHAP SO LUONG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        headerINS = {
                'accept': '*/*',
                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                # 'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookieINS,
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/p/C9RAZEJNjPC/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                'x-asbd-id': '129477',
                'x-csrftoken': cookieINS.split('csrftoken=')[1].split(';')[0],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR1Jw2LrciyrzAQskwSVGREElPZZJZjW74y38oTjDnNHOu9e',
                'x-instagram-ajax': '1014868636',
                'x-requested-with': 'XMLHttpRequest',
            }
        param = {
            'instagram_account_id': account_id,
            'data': 'null',
        }
        DELAY = int(input(Fore.RED+'NHAP DELAY : '))
        for i in range(choose):
                job = 'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id='+str(account_id)+'&data=null'
                nos = ses.get(job,headers=headers,params=param).json()
                if nos['status'] ==200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    type = nos['data']['type']
                    if type == 'follow':
                        url = 'https://www.instagram.com/api/v1/friendships/create/'+object_id+'/'
                        data = {
                            'container_module': 'profile',
                            'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
                            'user_id': object_id,
                        }
                        respone = requests.post(url,headers=headerINS,data=data,proxies=proxyy).text
                        countdown(DELAY)
                        if '"status":"ok"' in respone:
                                url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                                json_data = {
                                'instagram_account_id': account_id,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data':'null',
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        elif '"status":"fail' and '"spam":true':
                             print(Fore.RED+"TAI KHOAN BI HAN CHE")
                        else:
                            print('Cookie HET HAN')
                            os.remove('COOKIEINS'+str(account_id)+'.txt')
                            return 0
                    elif type=='like':
                        like_id = nos['data']['description']
                        url = 'https://www.instagram.com/api/v1/web/likes/'+str(like_id)+'/like/'
                        response = requests.post(url,headers=headerINS,proxies=proxyy).text
                        countdown(DELAY)
                        if '"status":"ok"' in response:
                                url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                                json_data = {
                                'instagram_account_id': account_id,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data':'null',
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        elif '"status":"fail' and '"spam":true':
                             print(Fore.RED+"TAI KHOAN BI HAN CHE")
                        else:
                            print('Cookie HET HAN')
                            os.remove('COOKIEINS'+str(account_id)+'.txt')
                            return 0
                else:
                        print(nos['message'])
                        countdown(15)
def LINKEDIN():
    checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account',headers=headers).json()
    user_linkedin1 = []
    account_id1 = []
    STT = []
    STATUS =[]
    print('CAC TAI KHOAN DANG HOAT DONG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkaccount['data'] :
            usernametk = data['name']
            # print(str(i)+'.'+usernametk)
            user_linkedin1.append(data['name'])
            account_id1.append(data['id'])
            STT.append(i)
            STATUS.append(Fore.GREEN+"DANG HOAT DONG"+Fore.RED)
        # create header
            i=i+1
    table = zip(STT,user_linkedin1,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHAP TAI KHOAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_linkedin1) :
        user_tiktok1 = user_linkedin1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_linkedin1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('COOKIELINKEDIN'+str(account_id)+'.txt')
        if checkfile == False:
            COOKIELINK = input(Fore.GREEN+'[+] COOKIE : ')
            createfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','w')
            createfile.write(COOKIELINK)
            createfile.close()
            readfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        print('[*] COOKIE : ',COOKIELINK)
        print(Fore.RED+'[+] 1 . SU DUNG DU LIEU CU')
        print(Fore.RED+'[+] 2 . XOA DU LIEU')
        URchoose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
        if URchoose == 2:
             os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
             return 0
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        choose = int(input(Fore.RED+'NHAP SO LUONG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        DELAY = int(input(Fore.RED+'NHAP DELAY : '))
        for i in range(choose):
                url2 = 'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id='+str(account_id)+'&data=null'
                checkurl2 = ses.get(url2,headers=headers).json()
                if checkurl2['status'] ==200:
                    linkjob = []
                    linkjob = str(checkurl2['data']['link'])
                    lenjob = len(checkurl2['data']['link'])
                    ads_id = checkurl2['data']['id']
                    object_id = checkurl2['data']['object_id']
                    type = checkurl2['data']['type']
                    countdown(DELAY)
                    if type == 'follow':
                        haeaders = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'cache-control': 'max-age=0',
                            'cookie':COOKIELINK ,
                            'priority': 'u=0, i',
                            'referer': 'https://app.golike.net/',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                            }

                        response = requests.get(str(linkjob),  headers=haeaders).text
                        if 'li:fsd_company' not in response and 'identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:' not in response:
                                    json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                     }
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                        else:
                            json_data = {
                            'patch': {
                                '$set': {
                                    'following': True,
                                },
                            },
                            }
                            json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                }
                            try:
                                crft =  COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data,proxies=proxyy)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    time.sleep(2)
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                            print(check)
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data,proxies=proxyy) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success']==True:
                                                prices =check['data']['prices']
                                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                                print(check)
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
                                        return 0
                            except IndexError:
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data,proxies=proxyy)
                                    time.sleep(2)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data,proxies=proxyy) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success']==True:
                                                prices =check['data']['prices']
                                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                                print(check)
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                            
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
                                        return 0
                    elif type == 'like':
                        try:
                            crft =  COOKIELINK.split('JSESSIONID')[1].split(';')[0],

                            headersL = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersL,
                                json=json_data,
                                proxies=proxyy
                            )
                        except IndexError:
                            headersN = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersN,
                                json=json_data,
                                proxies=proxyy
                            )
                        json_data2 = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                            }
                        time.sleep(2)
                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                        check = requests.post(url,headers=headers,json=json_data2).json()
                        if check['success']==True:
                                prices =check['data']['prices']
                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                        else:
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                PARAMS = {
                                'ads_id' : ads_id,
                                'account_id' : account_id,
                                'object_id' : object_id ,
                                }
                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                                    PARAMSr = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }   
                else:        
                    print(checkurl2['message'])
                    countdown(5*60)
def THREADS():
    checkaccount = requests.get('https://gateway.golike.net/api/threads-account',headers=headers).json()
    user_THREADS = []
    account_id1 = []
    STT = []
    STATUS =[]
    print('CAC TAI KHOAN DANG HOAT DONG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkaccount['data'] :
            usernametk = data['name']
            # print(str(i)+'.'+usernametk)
            user_THREADS.append(data['name'])
            account_id1.append(data['id'])
            STT.append(i)
            STATUS.append(Fore.GREEN+"DANG HOAT DONG"+Fore.RED)
        # create header
            i=i+1
    table = zip(STT,user_THREADS,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHAP TAI KHOAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_THREADS) :
        user_THREADS = user_THREADS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_THREADS[0] 
        account_id = account_id1[0]
        checkfile2 = os.path.isfile('COOKIETHR'+str(account_id)+'.txt')
        if checkfile2 == False:
            cookieX = input(Fore.GREEN+'[+]''COOKIE : ')
            createfile = open('COOKIETHR'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIETHR'+str(account_id)+'.txt','r')
            cookieTHR = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIETHR'+str(account_id)+'.txt','r')
            cookieTHR = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        print('[*] COOKIE : ',cookieTHR)
        print(Fore.RED+'[+] 1 . SU DUNG DU LIEU CU')
        print(Fore.RED+'[+] 2 . XOA DU LIEU')
        URchoose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
        if URchoose == 2:
             os.remove('COOKIETHR'+str(account_id)+'.txt')
             return 0
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        choose = int(input(Fore.RED+'NHAP SO LUONG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("DENO","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY DENO')
        print('EMAIL : VINHYTB3010@gmail.com')
        print('ZALO : 0961442667')
        print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
        print('WEBSITE : https://profiledeno.netlify.app/')
        headersTHR = {
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookieTHR,
            'origin': 'https://www.threads.net',
            'priority': 'u=1, i',
            'referer': 'https://www.threads.net/@dreyt041',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Pixel 5"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': '129477',
            'x-csrftoken': cookieTHR.split('csrftoken=')[1].split(';')[0],
            'x-fb-friendly-name': 'useBarcelonaFollowMutationFollowMutation',
            'x-fb-lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
            'x-ig-app-id': '238260118697367',
        }
        param = {
             'account_id':str(account_id)
        }
        DELAY = int(input(Fore.RED+'NHAP DELAY : '))
        for i in range(choose):
                job = 'https://gateway.golike.net/api/advertising/publishers/threads/jobs?account_id='+str(account_id)
                nos = ses.get(job,headers=headers,params=param).json()
                if nos['status'] ==200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    type = nos['data']['type']
                    link = nos['data']['link']
                    if type == 'follow':
                        try :
                            url = link
                            check = requests.get(url,headers=headersTHR).text
                            fb_dtsg = check.split('"f":"')[1].split('",')[0]
                            user_id = check.split('"props":{"user_id":"')[1].split('",')[0]
                            data = {
                            # 'av': '17841461328267610',
                            '__user': '0',
                            '__a': '1',
                            '__req': 'c',
                            '__hs': '19925.HYP:barcelona_web_pkg.2.1..0.1',
                            'dpr': '1',
                            '__ccg': 'UNKNOWN',
                            '__rev': '1015041514',
                            '__s': '4oqz5z:tfv4jd:iv92im',
                            '__hsi': '7394241910778378470',
                            '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lx-0iS2S3qazo7u0zE2ZwrUdUbGw4mwr86C2q1iwiQ1mwLwHxW17y9UjgdE-19w',
                            '__csr': 'gV2QPfHkGNcIQZFAjlqvap8lbc9qyBByp99O96y9o01J73a4A5hlwQSaxshDk9a4Ujgakph3DS7o6K0_A0hvc2p1afwk41jx7OhM1SmEiglwqcM4d01vhx22t0FhYg0QFA',
                            '__comet_req': '29',
                            'fb_dtsg': fb_dtsg,
                            'jazoest': '26086',
                            'lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
                            '__spin_r': '1015041514',
                            '__spin_b': 'trunk',
                            '__spin_t': '1721606103',
                            'fb_api_caller_class': 'RelayModern',
                            'fb_api_req_friendly_name': 'useBarcelonaFollowMutationFollowMutation',
                            'variables': '{"target_user_id":'+user_id+',"media_id_attribution":null,"container_module":"ig_text_feed_profile"}',
                            'server_timestamps': 'true',
                            'doc_id': '7812622502155806',
                        }
                            response = requests.post('https://www.threads.net/api/graphql', headers=headersTHR, data=data,proxies=proxyy).text
                            countdown(DELAY)
                            if '"following":true' in response:
                                url = 'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs'
                                json_data = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        except IndexError:
                            print('COOKIE DIE') 
                            os.remove('COOKIETHR'+str(account_id)+'.txt')
                            return 0 
                    elif type == 'like':
                        try :
                            check = requests.get(link,headers=headersTHR).text
                            fb_dtsg = check.split('"f":"')[1].split('",')[0]
                            post_id = check.split('"props":{"post_id":"')[1].split('",')[0]
                            data = {
                                'av': '17841465195438651',
                                '__user': '0',
                                '__a': '1',
                                '__req': '13',
                                '__hs': '19926.HYP:barcelona_web_pkg.2.1..0.1',
                                'dpr': '1',
                                '__ccg': 'UNKNOWN',
                                '__rev': '1015041902',
                                '__s': 'gmmbni:g1innv:0tm2do',
                                '__hsi': '7394261959223963838',
                                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lx-0iS2S3qazo7u0zE2ZwrUdUbGw4mwr86C2q6oe84J0lEbUaUuwhUyu4Q3qfwio',
                                '__csr': 'gV2QP9mJiHkTYQZFAjlqvap8lbc9qKpqG9AAD8Cm8Bw06QscEigl5m3joG5N6tgAEjxd0FhB4evotwqU3-g15YM9A4E-1gg5e4v9706Gy89mEiglwqcM4d01vhx22t0FhYg0QFA58',
                                '__comet_req': '29',
                                'fb_dtsg': fb_dtsg,
                                'jazoest': '26398',
                                'lsd': 'cQ5UmUjtTg4rd7wo5B_3qv',
                                '__spin_r': '1015041902',
                                '__spin_b': 'trunk',
                                '__spin_t': '1721610771',
                                'fb_api_caller_class': 'RelayModern',
                                'fb_api_req_friendly_name': 'useBarcelonaLikeMutationLikeMutation',
                                'variables': '{"mediaID":'+post_id+'}',
                                'server_timestamps': 'true',
                                'doc_id': '24068295876148027',
                            }
                            response = requests.post('https://www.threads.net/api/graphql', headers=headersTHR, data=data,proxies=proxyy).text
                            countdown(DELAY)
                            if '"is_final":true' in response:
                                url = 'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs'
                                json_data = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        except IndexError:
                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs'
                            PARAMS = {
                            'ads_id' : ads_id,
                            'account_id' : account_id,
                            'object_id' : object_id ,
                            'async': 'true',
                            'data': 'null',
                            'type': type,
                            }
                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                            if checkskipjob['status'] == 200:
                                message = checkskipjob['message']
                                print(Fore.RED+str(message))
                                PARAMSr = {
                                'ads_id' : ads_id,
                                'account_id' : account_id,
                                'object_id' : object_id ,
                                'async': 'true',
                                'data': 'null',
                                'type': type,
                                }
                            
                else:
                    print(nos['message'])
                    countdown(15)
                        
def LIST():
    mydata = [
        [Fore.RED+"1", "  Tiktok                ",Fore.GREEN+"  MOBILE"+Fore.RED],
        [Fore.RED+"2", "  Twitter/X             ",Fore.GREEN+"  PC+MOBILE"+Fore.RED], 
        [Fore.RED+"3", "  Instagram             ",Fore.GREEN+"  PC+MOBILE"+Fore.RED], 
        [Fore.RED+"4", "  Linkedin              ",Fore.GREEN+"  PC+MOBILE"+Fore.RED],
        [Fore.RED+"5", "  Threads               ",Fore.GREEN+"  PC+MOBILE"+Fore.RED],
        [Fore.RED+"6", "  YOUTUBE               ",Fore.YELLOW+"  BAO TRI  "+Fore.RED]
    ]
    
    # create header
    head = ["STT", "  TOOL","   STATUS"]
    LIST=Fore.RED+tabulate(mydata, headers=head, tablefmt="grid",)
    print(LIST)
os.system('cls' if os.name== 'nt' else 'clear')
tprint("DENO","rnd-xlarge")
print(Fore.RED+'\t\tTOOL BY DENO')
print('EMAIL : VINHYTB3010@gmail.com')
print('ZALO : 0961442667')
print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
print('WEBSITE : https://profiledeno.netlify.app/')
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'[+]''NHAP Authorization : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()

ses = requests.Session()
User_Agent=random.choice(open("useragent.txt","r").readline().splitlines())
try:
    headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
                'Referer':'https://app.golike.net/',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':"Windows",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
                'User-Agent':User_Agent,
                "Authorization" : file,
                'Content-Type':'application/json;charset=utf-8'            
    }

    url1 = 'https://gateway.golike.net/api/users/me'
    checkurl1 = ses.get(url1,headers=headers).json()
except requests.exceptions.InvalidHeader:
    os.remove('user.txt')
    #user
if checkurl1['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        print(Fore.BLUE+'1.TOOL GOLIKE MOBILE')
        choose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
        if choose == 1 :
            os.system('cls' if os.name== 'nt' else 'clear')
            tprint("DENO","rnd-xlarge")
            print(Fore.RED+'\t\tTOOL BY DENO')
            print('EMAIL : VINHYTB3010@gmail.com')
            print('ZALO : 0961442667')
            print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
            print('WEBSITE : https://profiledeno.netlify.app/')
            os.system('cls' if os.name== 'nt' else 'clear')
            tprint("DENO","rnd-xlarge")
            print(Fore.RED+'\t\tTOOL BY DENO')
            print('EMAIL : VINHYTB3010@gmail.com')
            print('ZALO : 0961442667')
            print('FACEBOOK : https://www.facebook.com/accngunghoatdongreal')
            print('WEBSITE : https://profiledeno.netlify.app/')
            ses.headers.update(headers)
            username = checkurl1['data']['username']
            coin = checkurl1['data']['coin']
            user_id = checkurl1['data']['id']
            print('________________________________________________________')
            print(Fore.GREEN+'[+] USERNAME : '+Fore.YELLOW+username)
            print(Fore.GREEN+'[+] TIEN : '+Fore.YELLOW+str(coin))
            print(Fore.RED+'_________________________________________________________')
            LIST()
            print(Fore.RED+'[+] 0.Xoa Authorization Hien Tai')
            choose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
            if choose==1:
                 os.system('cls' if os.name== 'nt' else 'clear')
                 TIKTOKINFO()
            elif choose==2:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                TWITTER()
            elif choose == 3:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                INSTAGRAM()
            elif choose == 4:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                LINKEDIN()
            elif choose==5:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                THREADS()
            elif choose==6:
                os.system('cls' if os.name== 'nt' else 'clear')
                print('TOOL DANG UPDATE VUI LONG CHO !')
            #     print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
            #     choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
            #     if(choose=='Y' or choose=='y'):
            #         os.system('cls' if os.name== 'nt' else 'clear')
            #         proxyy = {
            #             'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
            #             'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
            #         }
            #     elif(choose=='N' or choose=='n'):
            #         os.system('cls' if os.name== 'nt' else 'clear')
            #         proxyy= {}
            #     ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
            #     print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
            #     YOUTUBE()
            # elif choose == 0:
            #      os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')










    
