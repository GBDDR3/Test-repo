from requests import get, utils

def currency_rate(tiket):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    date = response.headers['Date'].split(', ')[1]
    print(f'Дата сервера: {date}')

    t_content = response.content.decode(encoding=encodings)
    keys = ['Nominal', 'Name', 'Value']
    t_str = t_content[t_content.find(str(tiket.upper())):]

    if len(t_str) > 2:
        t_str = t_str[:t_str.find('</Valute>')]
        c_info = list(map(lambda x: str(t_str.split(x)[1])[1:-2],keys))
        c_info[0] = int(c_info[0])
        c_info[2] = float('.'.join(c_info[2].split(',')))
        print(f'За {c_info[0]} {c_info[1]} дают {c_info[2]} рублей')
    else:
        print(None)

if __name__ == "__main__":

    currency_rate(input('Введите значение валюты: '))


