import json
import random
from googlesearch import search
from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler
import requests
from bs4 import BeautifulSoup as BS


TOKEN = ""
bot = Bot(token = TOKEN)

cities = [
        'москва','санкт-петербург', 'новосибирск','екатеринбург',
        'нижний новгород', 'казань', 'челябинск', 'омск',  'самара', 'ростов-на-дону', 
        'уфа', 'красноярск', 'воронеж', 'пермь', 'волгоград', 'краснодар'       ,
        'саратов'           ,'тюмень'            ,'тольятти'          ,'ижевск'            ,'барнаул'           ,
        'ульяновск'         ,'иркутск'           ,'хабаровск'         , 'ярославль'        ,'владивосток'       ,
        'махачкала'         ,'томск'             ,'оренбург'          ,'кемерово'          ,'новокузнецк'       ,'рязань'          ,
        'астрахань'         ,'набережные челны'  ,'пенза'             ,'киров'             ,'липецк'            ,'чебоксары'         ,'балашиха'          ,'калининград'       ,
        'тула'              ,'курск'             ,'севастополь'       ,'сочи'              ,'ставрополь'        ,'улан-Удэ'          ,'тверь'             ,
        'магнитогорск'      ,'иваново'           ,'брянск'            ,'белгород'          ,'сургут'            ,'ханты-Мансийск'    ,'владимир'          ,'нижний Тагил'      ,
        'чита'              ,'архангельск'       , 'симферополь'      , 'калуга'           , 'смоленск'         , 'волжский'          ,
        'якутск'            ,'саранск'           ,'череповец'         ,'курган'            ,'вологда'           ,'орёл'              ,
        'владикавказ'       ,'подольск'          ,'грозный'           ,'мурманск'          ,'тамбов'            ,'петрозаводск'      ,'стерлитамак'       ,
        'нижневартовск'     ,'кострома'          ,'новороссийск'      ,'химки'             ,'таганрог'          ,'сыктывкар'         ,'нижнекамск'        ,
        'нальчик'           ,'шахты'             ,'дзержинск'         ,'орск'              ,
        'братск'            ,'благовещенск'      ,'энгельс'           ,'ангарск'           ,'королёв'           ,'мытищи'            ,'псков'             ,'люберцы'           ,
        'бийск'             ,'прокопьевск'       ,'армавир'           ,'балаково'          ,'рыбинск'           ,'абакан'            ,
        'северодвинск'      ,'норильск'          ,'уссурийск'         ,'волгодонск'        ,'красногорск'       ,'сызрань'           ,
        'новочеркасск'      ,'златоуст'          ,'пятигорск'         ,'домодедово'        ,'кисловодск'        ,'нефтеюганск'       ,'батайск'           ,
        'новочебоксар'      ,'серпухов'          ,'щёлково'           ,'новомосковск'      ,'черкесск'          ,'первоуральск'      ,
        'раменское'         ,'каспийск'          ,'ессентуки'         ,'северск'           ,'пушкино'           ,'ноябрьск'          ,
        'бердск'            ,'елец'              ,'сергиев посад'     ,'новокуйбышевск'    ,'железногорск'      , '%s'  
         ]
link_cities = [ 'moskva/', 'sankt_peterburg/', 'novosibirsk/', 'ekaterinburg/', 'nizhniy_novgorod/',
                'kazan/', 'chelyabinsk/', 'omsk/', 'samara/', 'rostov-na-donu/', 'ufa/', 'krasnoyarsk/',
                'voronezh/', 'perm/', 'volgograd/', 'krasnodar'         ,'saratov'           ,'tyumen'            ,'toliatti'          ,
                'izhevsk'           ,'barnaul'           ,'ulianovsk'         ,'irkutsk'           ,'khabarovsk'        ,'yaroslavl'         ,
                'vladivostok'       ,'makhachkala'       ,'tomsk'             ,'orenburg'          ,'kemerovo'          ,'novokuznetsk'      ,
                'ryazan'            ,'astrakhan'         ,'naberezhnye_chelny','penza'             ,'kirov'             ,'lipetsk'           ,
                'cheboksary'        ,'balashikha'        ,'kaliningrad'       ,'tula'              ,'kursk'             ,'sevastopol'        ,
                'sochi'             ,'stavropol'         ,'ulan-ude'          ,'tver'              ,'magnitogorsk'      ,'ivanovo'           ,'bryansk'           ,
                'belgorod'          ,'surgut'            ,'khanty-mansiysk'   ,'vladimir'          ,'nizhniy_tagil'     ,'chita'             ,
                'arkhangelsk'       ,'simferopol'        ,'kaluga'            ,'smolensk'          ,'volzhskiy'         ,'yakutsk'           ,
                'saransk'           ,'cherepovets'       ,'kurgan'            ,'vologda'           ,'orel'              ,'vladikavkaz'       ,
                'podolsk'           ,'grozny'            ,'murmansk'          ,'tambov'            ,'petrozavodsk'      ,'sterlitamak'       ,
                'nizhnevartovsk'    ,'kostroma'          ,'novorossiysk'      ,'khimki'            ,'taganrog'          ,'syktyvkar'         ,
                'nizhnekamsk'       ,'nalchik'           ,'shakhty'           ,'dzerzhinsk'        ,'orsk'              ,'bratsk'            ,
                'blagoveschensk'    ,'engels'            ,'angarsk'           ,'korolev'           ,'mytischi'          ,'pskov'             ,
                'lyubertsy'         ,'biysk'             ,'prokopyevs'        ,'armavir'           ,'balakovo'          ,'rybinsk'           ,'abakan'            ,
                'severodvink'       ,'norilsk'           ,'ussuriysk'         ,'volgodonsk'        ,'krasnogorsk'       ,'syzran'            ,'novocherkassk'     ,
                'zlatoust'          ,'pyatigorsk'        ,'domodedovo'        ,'kislovodsk'        ,'nefteyugansk'      ,'bataysk'           ,
                'novocheboksarsk'   ,'serpukhov'         ,'schelkovo'         ,'novomoskovsk'      ,'cherkessk'         ,'pervouralsk'       ,
                'ramenskoe'         ,'kaspiysk'          ,'essentuki'         ,'seversk'           ,'pushkino'          ,'noyabrsk'          ,
                'berdsk'            ,'elets'             ,'sergiev_posad'     ,'novokuybyshevsk'   ,'zheleznogorsk'     ,''     
              ]

def message_cb_weather(bot, event):
    if event.text[0:8] == "/weather":
        _text = event.text
        i = 0
        while i < 130:
            if _text.replace("/weather ", "").lower() == cities[i]:
                URL = 'https://pogoda.mail.ru/prognoz/' + link_cities[i]
                r = requests.get(URL)
                html = BS(r.content, 'html.parser')
                title = html.select('.information__header__left__place__city')
                degrees = html.select('.information__content__temperature')
                bot.send_text(chat_id=event.from_chat, 
                    text= title[0].get_text(strip = True) + ' ' + degrees[0].get_text(strip = True))
                i = 0
                break
            elif i == 129:
                cities[129] = _text.replace("/weather ", "").lower()
                if _text.replace("/weather ", "").lower() == cities[129]:
                    bot.send_text(chat_id=event.from_chat, text= 'Вашего города нет в списке, но вы можете посетить сайт mail.ru, для ознакомления с прогнозом погоды.')
            i += 1


def message_cb_news(bot, event):
    r = requests.get('https://news.mail.ru')
    html = BS(r.content, 'html.parser')
    if event.text == "/news":
        bot.send_text(chat_id=event.from_chat, 
        text="Актуальные новости на данный момент.\n")
        
        i = 0
        while i < 3:
            i += 1
            title = html.select('.list__text')              
            bot.send_text(chat_id=event.from_chat, 
                text= title[i].get_text(strip = True) + '\n' + 'https://news.mail.ru' + title[i].get('href'))


def message_cb_search(bot, event):
    if event.text[0:7] == "/search":
        user_search = event.text
        query = user_search.replace("/search ", "")
        find = search(query, tld='com', lang = 'ru', num=1, stop=1, pause=0)
        bot.send_text(chat_id=event.from_chat, text = "Сайт по вашему запросу.\n")
        bot.send_text(chat_id=event.from_chat, text = find)
        

def message_cb_coin(bot, event):
    if event.text[0:5] == "/coin":
        coin = random.randint(0, 1)
        if coin == 1:
            bot.send_text(chat_id=event.from_chat, text = "Выпал орёл.")
        else:
            bot.send_text(chat_id=event.from_chat, text = "Выпала решка.")
   

def message_cb_to_rus(bot, event):
    if event.text[0:6] == "/torus":
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
        key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'  
        lang = 'en-ru'
        user_input = event.text
        text = user_input.replace("/torus ", "")
        translate = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
        translation = json.loads(translate.text)['text'][0]        
        bot.send_text(chat_id=event.from_chat, text = 'Перевод:\n'+translation)
        
def message_cb_to_eng(bot, event):
    if event.text[0:6] == "/toeng":
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate' 
        key = 'trnsl.1.1.20200507T145200Z.9c4430c9346f518b.1b460c0d7ef1ba2a633e140b62d912e64b9de9a0'  
        lang = 'ru-en'
        user_input = event.text
        text = user_input.replace("/toeng ", "")
        translate = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
        translation = json.loads(translate.text)['text'][0]        
        bot.send_text(chat_id=event.from_chat, text = 'Перевод:\n'+translation)

def message_cb_serials(bot, event):
    r = requests.get('https://www.kinopoisk.ru/popular/?quick_filters=serials')
    html = BS(r.content, 'html.parser')
    if event.text == "/serials":
        title = html.select('.selection-film-item-meta__name')
        bot.send_text(chat_id=event.from_chat, 
            text= "Лучшие сериалы на данный момент, приукрасьте свой карантин!")
        bot.send_text(chat_id=event.from_chat, 
            text= '1. ' + title[0].text + '\n2. ' + title[1].text + '\n3. ' + title[2].text + '\n4. ' + title[3].text + '\n5. '+ title[4].text)
            
def message_cb_find(bot, event):
    if event.text[0:5] == "/find":
        _text = event.text
        url = 'https://search-maps.yandex.ru/v1/' 
        key = '35f4bf19-2ad9-4d42-83a7-51d6b26b5d17'  
        payload = {'text': _text.replace("/find ",""), 'type': 'biz', 'lang': 'ru_RU','results': '1','apikey': key}
        find = requests.get(url, params=payload )
        prop = json.loads(find.text)["properties"]["ResponseMetaData"]["SearchResponse"]["found"]
        if prop == 0:
            bot.send_text(chat_id=event.from_chat, text = "По вашему запросу ничего не найдено.")
        else:
            name = json.loads(find.text)["features"][0]["properties"]["CompanyMetaData"]["name"]
            address = json.loads(find.text)["features"][0]["properties"]["CompanyMetaData"]["address"]
            finded = "Название: " + name+ '\n' + "Адрес: " + address
            bot.send_text(chat_id=event.from_chat, text = finded)


def buttons_answer_cb_coronavirus(bot, event):
    if event.data['callbackData'] == "call_back_id_1":
        r = requests.get('https://www.worldometers.info/coronavirus/country/russia/')
        html = BS(r.content, 'html.parser')
        for el in html.select('.content-inner'):
            title = el.select('.maincounter-number')
            bot.answer_callback_query(
                query_id=event.data['queryId'],
                text='Заражений: '+title[0].get_text(strip = True)+ '\n'+ 'Смертей: '+title[1].get_text(strip = True)+ '\n'+ 'Выздоровлений: '+title[2].get_text(strip = True),
                show_alert=True
                )

    elif event.data['callbackData'] == "call_back_id_2":
        r_w = requests.get('https://www.worldometers.info/coronavirus/')
        htmlw = BS(r_w.content, 'html.parser')
        for el in htmlw.select('.content-inner'):
            title = el.select('.maincounter-number')
            bot.answer_callback_query(
                query_id=event.data['queryId'],
                text='Заражений: '+title[0].get_text(strip = True)+ '\n'+ 'Смертей: '+title[1].get_text(strip = True)+ '\n'+ 'Выздоровлений: '+title[2].get_text(strip = True),
                show_alert=True
                )


def message_cb_coronavirus(bot, event):
    if event.text[0:12] == "/coronavirus":
        bot.send_text(chat_id=event.from_chat,
                  text="Статистика коронавируса Covid-19 на сегодня (используются кнопки).",
                  inline_keyboard_markup="{}".format(json.dumps([[
                      {"text": "В России", "callbackData": "call_back_id_1", "style": "attention"},
                      {"text": "В мире", "callbackData": "call_back_id_2", "style": "attention"}
                                        ]])))

def message_cb_rate(bot, event):
    r = requests.get('https://business.ngs.ru/currency/?from=money')
    html = BS(r.content, 'html.parser')
    if event.text == "/rate":
        bot.send_text(chat_id=event.from_chat, 
            text= 'Курс доллара и евро на сегодня.')
        for el in html.select('.bus-currency-box__informer'):
            title = el.select('.bus-currency-box__informer-main')
            usd = title[0].get_text(strip = True)
            a = usd[0:10]
            b = a.replace("USD", "USD ")
            c = b.replace("EUR", "EUR ")
            bot.send_text(chat_id=event.from_chat, 
            text= c)
            
def message_cb_code(bot, event):
    if event.text[0:10] == "/promocode":
        r = requests.get('https://promokod.pikabu.ru/actions/edim-doma')
        html = BS(r.content, 'html.parser')
        title = html.select('.name')
        code = html.select('.clipboardjs-workaround')
        bot.send_text(chat_id=event.from_chat, 
            #Да я знаю что это глупо, но лень было придумывать грамотный цикл)))
                text= "Предложения по доставке еды.\n"+
                      "Организация: "+title[0].get_text(strip = True)+" -" + "промокод: "+ code[0].get_text(strip = True)+'\n'+
                      "Организация: "+title[1].get_text(strip = True)+" -" + "промокод: "+ code[1].get_text(strip = True)+'\n'+
                      "Организация: "+title[2].get_text(strip = True)+" -" + "промокод: "+ code[2].get_text(strip = True)+'\n'+
                      "Организация: "+title[3].get_text(strip = True)+" -" + "промокод: "+ code[3].get_text(strip = True)+'\n'+
                      "Организация: "+title[4].get_text(strip = True)+" -" + "промокод: "+ code[4].get_text(strip = True)+'\n'+
                      "Организация: "+title[5].get_text(strip = True)+" -" + "промокод: "+ code[5].get_text(strip = True)+'\n'+
                      "Организация: "+title[6].get_text(strip = True)+" -" + "промокод: "+ code[6].get_text(strip = True)+'\n'+
                      "Организация: "+title[7].get_text(strip = True)+" -" + "промокод: "+ code[7].get_text(strip = True)+'\n'+
                      "Организация: "+title[8].get_text(strip = True)+" -" + "промокод: "+ code[8].get_text(strip = True)+'\n'+
                      "Организация: "+title[9].get_text(strip = True)+" -" + "промокод: "+ code[9].get_text(strip = True)+'\n'+
                      "Организация: "+title[10].get_text(strip = True)+" -" + "промокод: "+ code[10].get_text(strip = True))

def message_cb_start(bot, event):
    if event.text[0:6] == "/start":
        bot.send_text(chat_id=event.from_chat, 
                text="Приветствую тебя, мой друг! Я бот-помощник. Я с радостью помогу тебе решить множество проблем. С помощью меня ты сможешь найти различные организации, узнать погоду, новости и многое другое! Напиши  /help для ознакомления со всеми моими командами. Удачного использования!")
        
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_start))      
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_code))            
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_rate))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_coronavirus))
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb_coronavirus))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_find))            
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_weather))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_news))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_search))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_coin))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_to_rus))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_to_eng))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb_serials))

bot.start_polling()
bot.idle()
