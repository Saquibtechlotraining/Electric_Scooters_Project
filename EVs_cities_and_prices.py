import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy    # These 2 libraries sqlalchemy and pyodbc are use to connect programming language with SQL (SSMS)
import pyodbc        # pyodbc is use to make a database connection
import datetime


# Database Connection:-
server = 'saquibevserver.database.windows.net, 1433'  # Here, 1433 are the port no. use to connect python with SQL (SSMS)
database = 'saquib_database_ev'
username = 'ev_saquibadmin'
password = '#################'    # (Hide because of crediential purpose)
driver = '{ODBC Driver 17 for SQL Server}'

# Create pyodbc connection string, by using this connection string we can establish a connection with SQL.
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the Database using pyodbc connection sting:-
connection = pyodbc.connect(connection_string)

# Create a sqlalchemy engine:-    (Use to process SQL Query, Execute etc)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')


def extract_table_data(url):

    dictionary_of_details = {}
    data_list = []  # Create a list to store the table data

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')

    # EV name
    name = soup.find('h1', class_='sectiom_block_style__Heading-sc-drgjgi-1 kXKqYB')
    ev_name = name.get_text() if name else None

    # Data when data scrap
    recorded_date = str(datetime.date.today())


    # EV prices in different cities
    table = soup.find('table', class_='table_style__CTable-sc-1qo50z6-0 fHkCXU mrg-b16')
    if table:
        table_rows = table.find_all('tr', class_='table_style__CTr-sc-1qo50z6-2 gYjnh')

        for table_row in table_rows:
            table_data = table_row.find_all('td', class_='table_style__CTd-sc-1qo50z6-5 caVOSP')
            if len(table_data) == 2:
                city_name = table_data[0].get_text()
                price = table_data[1].get_text()
                data_list.append({'name': ev_name, 'city': city_name, 'price': price,
                                  'recorded_date' : recorded_date})

    return data_list

urls = [
'https://www.91wheels.com/scooters/river-ev/indie',
    'https://www.91wheels.com/scooters/benling-india/aura',
    'https://www.91wheels.com/scooters/benling-india/falcon',
    'https://www.91wheels.com/scooters/benling-india/kriti',
    'https://www.91wheels.com/scooters/gt-force/soul-ev',
    'https://www.91wheels.com/scooters/gt-force/oneev',
    'https://www.91wheels.com/scooters/gt-force/prime',
    'https://www.91wheels.com/scooters/gt-force/one-plus',
    'https://www.91wheels.com/scooters/gt-force/drive-pro',
    'https://www.91wheels.com/scooters/gt-force/drive-plus',
    'https://www.91wheels.com/scooters/gt-force/flying-ev',
    'https://www.91wheels.com/scooters/maruthisan/ms-3-0',
    'https://www.91wheels.com/scooters/trouve-motor/h2',
    'https://www.91wheels.com/scooters/sokudo/acute',
    'https://www.91wheels.com/scooters/hero-vida/vida-v1',
    'https://www.91wheels.com/scooters/silence/s01-plus',
    'https://www.91wheels.com/scooters/igowise/beigo',
    'https://www.91wheels.com/scooters/zelio/gracy',
    'https://www.91wheels.com/scooters/zelio/eeva',
    'https://www.91wheels.com/scooters/zelio/eeva-zx',
    'https://www.91wheels.com/scooters/zelio/gracy-i',
    'https://www.91wheels.com/scooters/joy-e-bike/wolf-plus',
    'https://www.91wheels.com/scooters/joy-e-bike/wolf',
    'https://www.91wheels.com/scooters/joy-e-bike/gen-nxt-nanu-plus',
    'https://www.91wheels.com/scooters/joy-e-bike/glob',
    'https://www.91wheels.com/scooters/joy-e-bike/gen-nxt-nanu-e-scooter',
    'https://www.91wheels.com/scooters/joy-e-bike/mihos',
    'https://www.91wheels.com/scooters/m2go-scooters/x1-ev',
    'https://www.91wheels.com/scooters/m2go-scooters/civitas',
    'https://www.91wheels.com/scooters/kabira-scooters/intercity-neo',
    'https://www.91wheels.com/scooters/kabira-scooters/kollegio-neo',
    'https://www.91wheels.com/scooters/kabira-scooters/kollegio-plus',
    'https://www.91wheels.com/scooters/kabira-scooters/aetos-100',
    'https://www.91wheels.com/scooters/kabira-scooters/hermes-75',
    'https://www.91wheels.com/scooters/kabira-scooters/kollegio',
    'https://www.91wheels.com/scooters/kabira-scooters/intercity-aeolus',
    'https://www.91wheels.com/scooters/gravton/quanta',
    'https://www.91wheels.com/scooters/komaki/se',
    'https://www.91wheels.com/scooters/komaki/ly',
    'https://www.91wheels.com/scooters/komaki/xone',
    'https://www.91wheels.com/scooters/komaki/xgt-x5',
    'https://www.91wheels.com/scooters/komaki/flora',
    'https://www.91wheels.com/scooters/komaki/xgt-km',
    'https://www.91wheels.com/scooters/komaki/venice-ev',
    'https://www.91wheels.com/scooters/komaki/xgt-vp',
    'https://www.91wheels.com/scooters/komaki/dt-3000',
    'https://www.91wheels.com/scooters/komaki/xgt-x3',
    'https://www.91wheels.com/scooters/komaki/tn-95',
    'https://www.91wheels.com/scooters/komaki/x2-vogue',
    'https://www.91wheels.com/scooters/komaki/super',
    'https://www.91wheels.com/scooters/odysse/racer',
    'https://www.91wheels.com/scooters/odysse/hawk',
    'https://www.91wheels.com/scooters/odysse/e2go',
    'https://www.91wheels.com/scooters/odysse/v2',
    'https://www.91wheels.com/scooters/odysse/v2-plus',
    'https://www.91wheels.com/scooters/odysse/trot',
    'https://www.91wheels.com/scooters/simple-energy-scooters/simple-one',
    'https://www.91wheels.com/scooters/techo-electra/raptor-ev',
    'https://www.91wheels.com/scooters/techo-electra/emerge',
    'https://www.91wheels.com/scooters/techo-electra/neo-ev',
    'https://www.91wheels.com/scooters/techo-electra/saathi',
    'https://www.91wheels.com/scooters/yukie-scooters/yuvee',
    'https://www.91wheels.com/scooters/yukie-scooters/shiga',
    'https://www.91wheels.com/scooters/lohia/oma-star',
    'https://www.91wheels.com/scooters/lohia/oma-star-li',
    'https://www.91wheels.com/scooters/one-moto/electa',
    'https://www.91wheels.com/scooters/one-moto/commuta',
    'https://www.91wheels.com/scooters/one-moto/byka',
    'https://www.91wheels.com/scooters/bgauss/d15',
    'https://www.91wheels.com/scooters/bgauss/c12i-max',
    'https://www.91wheels.com/scooters/kinetic/green-zing',
    'https://www.91wheels.com/scooters/kinetic/green-zoom',
    'https://www.91wheels.com/scooters/hcd-india-scooters/nps-cargo-48v',
    'https://www.91wheels.com/scooters/evtric-motors/ride',
    'https://www.91wheels.com/scooters/evtric-motors/rise',
    'https://www.91wheels.com/scooters/evtric-motors/axis',
    'https://www.91wheels.com/scooters/evtric-motors/connect',
    'https://www.91wheels.com/scooters/evtric-motors/mighty',
    'https://www.91wheels.com/scooters/ampere/magnus-ex',
    'https://www.91wheels.com/scooters/ampere/zeal-ex',
    'https://www.91wheels.com/scooters/ampere/primus',
    'https://www.91wheels.com/scooters/adms/sathi',
    'https://www.91wheels.com/scooters/adms/maevel',
    'https://www.91wheels.com/scooters/adms/eva',
    'https://www.91wheels.com/scooters/adms/rame',
    'https://www.91wheels.com/scooters/adms/mantra',
    'https://www.91wheels.com/scooters/prevail/elite',
    'https://www.91wheels.com/scooters/prevail/wolfury',
    'https://www.91wheels.com/scooters/prevail/finesse',
    'https://www.91wheels.com/scooters/merico-scooters/eagle-100-4-8',
    'https://www.91wheels.com/scooters/merico-scooters/eagle-100-6-0',
    'https://www.91wheels.com/scooters/merico-scooters/fashia',
    'https://www.91wheels.com/scooters/merico-scooters/evanka',
    'https://www.91wheels.com/scooters/merico-scooters/speedstar',
    'https://www.91wheels.com/scooters/heroelectric/optima',
    'https://www.91wheels.com/scooters/heroelectric/photon',
    'https://www.91wheels.com/scooters/heroelectric/nyx',
    'https://www.91wheels.com/scooters/heroelectric/atria',
    'https://www.91wheels.com/scooters/heroelectric/eddy',
    'https://www.91wheels.com/scooters/geliose-hope/hope',
    'https://www.91wheels.com/scooters/bajaj/chetak',
    'https://www.91wheels.com/scooters/wroley-e-scooter/posh',
    'https://www.91wheels.com/scooters/wroley-e-scooter/platina',
    'https://www.91wheels.com/scooters/wroley-e-scooter/mars',
    'https://www.91wheels.com/scooters/okaya-electric/faast-f3',
    'https://www.91wheels.com/scooters/okaya-electric/freedum',
    'https://www.91wheels.com/scooters/okaya-electric/classiq',
    'https://www.91wheels.com/scooters/okaya-electric/faast-f2f',
    'https://www.91wheels.com/scooters/okaya-electric/motofast',
    'https://www.91wheels.com/scooters/okaya-electric/faast',
    'https://www.91wheels.com/scooters/okaya-electric/faast-f2t',
    'https://www.91wheels.com/scooters/okaya-electric/faast-f2b',
    'https://www.91wheels.com/scooters/velev-motors-scooters/vev-01',
    'https://www.91wheels.com/scooters/velev-motors-scooters/vio',
    'https://www.91wheels.com/scooters/greta-electric/harper',
    'https://www.91wheels.com/scooters/greta-electric/e-glide',
    'https://www.91wheels.com/scooters/greta-electric/evespa',
    'https://www.91wheels.com/scooters/greta-electric/harper-zx',
    'https://www.91wheels.com/scooters/dao-electirc/zor-405',
    'https://www.91wheels.com/scooters/dao-electirc/model-703',
    'https://www.91wheels.com/scooters/dao-electirc/vidyut-108',
    'https://www.91wheels.com/scooters/eeve/soul',
    'https://www.91wheels.com/scooters/eeve/xeniaa',
    'https://www.91wheels.com/scooters/eeve/wind',
    'https://www.91wheels.com/scooters/eeve/ahava',
    'https://www.91wheels.com/scooters/eeve/atreo',
    'https://www.91wheels.com/scooters/evolet/pony',
    'https://www.91wheels.com/scooters/evolet/dhanno',
    'https://www.91wheels.com/scooters/evolet/epolo',
    'https://www.91wheels.com/scooters/evolet/derby',
    'https://www.91wheels.com/scooters/hop-electric/leo',
    'https://www.91wheels.com/scooters/hop-electric/leo-extended',
    'https://www.91wheels.com/scooters/hop-electric/lyf',
    'https://www.91wheels.com/scooters/ivoomi/jeetx',
    'https://www.91wheels.com/scooters/ivoomi/s1-ev',
    'https://www.91wheels.com/scooters/ivoomi/city-1',
    'https://www.91wheels.com/scooters/ivoomi/icity',
    'https://www.91wheels.com/scooters/ivoomi/jeet',
    'https://www.91wheels.com/scooters/grp-ev/11-mini',
    'https://www.91wheels.com/scooters/grp-ev/11-pro',
    'https://www.91wheels.com/scooters/grp-ev/11-max',
    'https://www.91wheels.com/scooters/crayon-scooters/zeez',
    'https://www.91wheels.com/scooters/crayon-scooters/envy',
    'https://www.91wheels.com/scooters/tvs/iqube-electric',
    'https://www.91wheels.com/scooters/tvs/x-ev',
    'https://www.91wheels.com/scooters/pure-ev/epluto',
    'https://www.91wheels.com/scooters/pure-ev/etrance-neo',
    'https://www.91wheels.com/scooters/pure-ev/epluto-7g',
    'https://www.91wheels.com/scooters/ses-electric/eagle',
    'https://www.91wheels.com/scooters/ses-electric/fly',
    'https://www.91wheels.com/scooters/ses-electric/tuff',
    'https://www.91wheels.com/scooters/ses-electric/zoom',
    'https://www.91wheels.com/scooters/ses-electric/bold',
    'https://www.91wheels.com/scooters/ses-electric/hobby',
    'https://www.91wheels.com/scooters/energy-automobile/evone',
    'https://www.91wheels.com/scooters/quantum-energy/elektron',
    'https://www.91wheels.com/scooters/quantum-energy/plasma',
    'https://www.91wheels.com/scooters/quantum-energy/bziness',
    'https://www.91wheels.com/scooters/quantum-energy/milan',
    'https://www.91wheels.com/scooters/tunwal/sport-63-48v',
    'https://www.91wheels.com/scooters/tunwal/roma-s',
    'https://www.91wheels.com/scooters/tunwal/t-133',
    'https://www.91wheels.com/scooters/tunwal/sport-63-60v',
    'https://www.91wheels.com/scooters/tunwal/mini-lithino-48v',
    'https://www.91wheels.com/scooters/tunwal/strom-zx',
    'https://www.91wheels.com/scooters/tunwal/storm-zx-advance-1',
    'https://www.91wheels.com/scooters/tunwal/storm-zx-advance-2',
    'https://www.91wheels.com/scooters/tunwal/lithino-li',
    'https://www.91wheels.com/scooters/warivo/nexa',
    'https://www.91wheels.com/scooters/warivo/queen-sx',
    'https://www.91wheels.com/scooters/warivo/enduro',
    'https://www.91wheels.com/scooters/warivo/queen',
    'https://www.91wheels.com/scooters/warivo/smarty',
    'https://www.91wheels.com/scooters/battre/storie',
    'https://www.91wheels.com/scooters/battre/loev',
    'https://www.91wheels.com/scooters/battre/iot',
    'https://www.91wheels.com/scooters/battre/one-ev',
    'https://www.91wheels.com/scooters/battre/gpsie',
    'https://www.91wheels.com/scooters/stella-automobili-scooters/sa-1000',
    'https://www.91wheels.com/scooters/stella-automobili-scooters/sa-2000',
    'https://www.91wheels.com/scooters/stella-automobili-scooters/buzz',
    'https://www.91wheels.com/scooters/fidato-evtech/easy-go',
    'https://www.91wheels.com/scooters/fidato-evtech/easygo-plus',
    'https://www.91wheels.com/scooters/fidato-evtech/future',
    'https://www.91wheels.com/scooters/fidato-evtech/loder',
    'https://www.91wheels.com/scooters/fidato-evtech/cutie',
    'https://www.91wheels.com/scooters/rugged/g1',
    'https://www.91wheels.com/scooters/segway/e110a',
    'https://www.91wheels.com/scooters/okinawa/praisepro',
    'https://www.91wheels.com/scooters/okinawa/okhi-90',
    'https://www.91wheels.com/scooters/okinawa/r30-electric-scooter',
    'https://www.91wheels.com/scooters/okinawa/ridge',
    'https://www.91wheels.com/scooters/okinawa/lite',
    'https://www.91wheels.com/scooters/okinawa/dual',
    'https://www.91wheels.com/scooters/okinawa/ipraise',
    'https://www.91wheels.com/scooters/okinawa/ipraise-plus',
    'https://www.91wheels.com/scooters/herald-e-bike/herald-e-bike-rider',
    'https://www.91wheels.com/scooters/herald-e-bike/herald-e-bike-royal',
    'https://www.91wheels.com/scooters/herald-e-bike/lengend-dlx',
    'https://www.91wheels.com/scooters/herald-e-bike/lengend-super',
    'https://www.91wheels.com/scooters/herald-e-bike/royal-prime',
    'https://www.91wheels.com/scooters/herald-e-bike/legend-prime',
    'https://www.91wheels.com/scooters/herald-e-bike/royal-dlx',
    'https://www.91wheels.com/scooters/ujaas-scooters/ezy',
    'https://www.91wheels.com/scooters/ujaas-scooters/ego-la',
    'https://www.91wheels.com/scooters/ujaas-scooters/espa-la',
    'https://www.91wheels.com/scooters/ujaas-scooters/ego-t3',
    'https://www.91wheels.com/scooters/ujaas-scooters/espa-li',
    'https://www.91wheels.com/scooters/ujaas-scooters/ego-li',
    'https://www.91wheels.com/scooters/gowel-scooters/zx-ev',
    'https://www.91wheels.com/scooters/ather/450x',
    'https://www.91wheels.com/scooters/ather/450s',
    'https://www.91wheels.com/scooters/detel-ev/easy-plus',
    'https://www.91wheels.com/scooters/aeroride/e-spark',
    'https://www.91wheels.com/scooters/aeroride/aero',
    'https://www.91wheels.com/scooters/aeroride/yb2000',
    'https://www.91wheels.com/scooters/yobykes/drift',
    'https://www.91wheels.com/scooters/yobykes/edge',
    'https://www.91wheels.com/scooters/raftaar-scooters/galaxy',
    'https://www.91wheels.com/scooters/raftaar-scooters/electrica',
    'https://www.91wheels.com/scooters/raftaar-scooters/lima',
    'https://www.91wheels.com/scooters/raftaar-scooters/cruzer-r1',
    'https://www.91wheels.com/scooters/raftaar-scooters/bumblebee',
    'https://www.91wheels.com/scooters/ola-electric/s1-pro',
    'https://www.91wheels.com/scooters/ola-electric/s1-air',
    'https://www.91wheels.com/scooters/ola-electric/s1-x',
    'https://www.91wheels.com/scooters/keeway/vieste-300',
    'https://www.91wheels.com/scooters/dynamo/rx4',
    'https://www.91wheels.com/scooters/dynamo/rx1',
    'https://www.91wheels.com/scooters/dynamo/x-1',
    'https://www.91wheels.com/scooters/dynamo/x-2',
    'https://www.91wheels.com/scooters/dynamo/x-4',
    'https://www.91wheels.com/scooters/dynamo/xl',
    'https://www.91wheels.com/scooters/dynamo/smiley',
    'https://www.91wheels.com/scooters/rbseva/legend',
    'https://www.91wheels.com/scooters/rbseva/rider-ev',
    'https://www.91wheels.com/scooters/rbseva/rider-new',
    'https://www.91wheels.com/scooters/rbseva/auram',
    'https://www.91wheels.com/scooters/rbseva/rbs250-loader',
    'https://www.91wheels.com/scooters/rbseva/rbseva-rio',
    'https://www.91wheels.com/scooters/rbseva/royal-zl3',
    'https://www.91wheels.com/scooters/rbseva/rbseva-royal-dlx',
    'https://www.91wheels.com/scooters/rbseva/legend-super',
    'https://www.91wheels.com/scooters/amo-electric/jaunty',
    'https://www.91wheels.com/scooters/amo-electric/inspirer',
    'https://www.91wheels.com/scooters/amo-electric/jaunty-plus',
    'https://www.91wheels.com/scooters/amo-electric/jaunty-3w',
    'https://www.91wheels.com/scooters/enigma/gt450',
    'https://www.91wheels.com/scooters/enigma/crink',
    'https://www.91wheels.com/scooters/enigma/ambier-n8',
    'https://www.91wheels.com/scooters/super-eco-scooters/t1',
    'https://www.91wheels.com/scooters/super-eco-scooters/s-2',
    'https://www.91wheels.com/scooters/viertric/v4-eagle',
    'https://www.91wheels.com/scooters/viertric/v4-max',
    'https://www.91wheels.com/scooters/viertric/v4-xl',
    'https://www.91wheels.com/scooters/viertric/v4-mist',
    'https://www.91wheels.com/scooters/deltic/drixx',
    'https://www.91wheels.com/scooters/deltic/trento',
    'https://www.91wheels.com/scooters/deltic/legion',
    'https://www.91wheels.com/scooters/deltic/zgs',
    'https://www.91wheels.com/scooters/eveium/czar',
    'https://www.91wheels.com/scooters/eveium/comet',
    'https://www.91wheels.com/scooters/eveium/cosmo-ev',
    'https://www.91wheels.com/scooters/bnc/challenger-s110',
    'https://www.91wheels.com/scooters/eblu/feo',
    'https://www.91wheels.com/scooters/gemopai/ryder',
    'https://www.91wheels.com/scooters/gemopai/astrid-lite',
    'https://www.91wheels.com/scooters/gemopai/miso',
    'https://www.91wheels.com/scooters/gemopai/ryder-supermax',
    'https://www.91wheels.com/scooters/white-carbon-motors/gt5',
    'https://www.91wheels.com/scooters/white-carbon-motors/o3',
    'https://www.91wheels.com/scooters/bounce/infinity-e1',
    'https://www.91wheels.com/scooters/lectrix/sx25',
    'https://www.91wheels.com/scooters/lectrix/lxs-g-2-0',
    'https://www.91wheels.com/scooters/lectrix/lxs',
    'https://www.91wheels.com/scooters/avon/e-lite',
    'https://www.91wheels.com/scooters/avon/e-scoot',
    'https://www.91wheels.com/scooters/avon/e-plus',
    'https://www.91wheels.com/scooters/avon/e-star-dx',
    'https://www.91wheels.com/scooters/avon/e-mate',
    'https://www.91wheels.com/scooters/kyte-energy/magnum-pro',
    'https://www.91wheels.com/scooters/li-ions/spock-electric-scooter',
    'https://www.91wheels.com/scooters/avera-scooters/retrosa',
    'https://www.91wheels.com/scooters/fujiyama/spectra',
    'https://www.91wheels.com/scooters/fujiyama/spectra-pro',
    'https://www.91wheels.com/scooters/fujiyama/ozoine',
    'https://www.91wheels.com/scooters/vegh/25s',
    'https://www.91wheels.com/scooters/vegh/s-60',
    'https://www.91wheels.com/scooters/vegh/l25'
]

all_data = []
for url in urls:
    data = extract_table_data(url)
    all_data.extend(data)

# Create a DataFrame from the list of dictionaries

cities_price = pd.json_normalize(all_data)

with engine.connect() as connection:
    cities_price.to_sql('cities_and_prices', con=connection, if_exists='append', index=False, schema='dbo')

# if_exists='append' ->  Because if whenever we run again the data will be append.
# index=False        ->  We dont want index 0,1,2,3....
# con=connection     ->  Make a pyodbc connection
# schema='dbo'       ->  Giving schema 'dbo' in SSMS