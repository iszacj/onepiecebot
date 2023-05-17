
class Character():
    def __init__(self,id,name,level,picture):
        self.id = id
        self.name = name
        self.level = level
        self.picture = picture

characters_pictures = {
    "Shanks": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231484177715261/shanks.png"],
    "Benn Beckman": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231484634890250/benn_beckman.png"],
    "Lucky Roux": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231483535982592/lucky_roux.png"],
    "Yasopp": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231483817017364/yasopp.png"],
    "Kaido": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231544558911518/kaido.png"],
    "King": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231544865103952/king.png"],
    "Queen": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231543787167744/queen.png"],
    "Jack": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231544214995006/jack.png"],
    "Big Mom": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231323636547644/big_mom.png"],
    "Katakuri": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231323250655364/katakuri.png"],
    "Smoothie": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231323967881247/smoothie.png"],
    "Cracker": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231322852212766/cracker.png"],
    "Blackbeard": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231447242690669/blackbeard.png"],
    "Jesus Burgess": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231447540473976/jesus_burges.png"],
    "Van Augur": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231446798082068/van_augr.png"],
    "Shiryu": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231446445772922/shiryu.png"],
    "Luffy": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106220323159953468/IMG_1457.png"],
    "Zoro": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106222017658765433/zoro.png"],
    "Nami": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106222008393547806/nami.png"],
    "Usopp": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106221990106370068/usopp.png"],
    "Sanji": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106221979893235712/sanji.png"],
    "Chopper": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106221968560242688/chopper.png"],
    "Nico Robin": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106223976180617247/robin.png"],
    "Franky": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106223987232604190/franky.png"],
    "Brook": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106223997613518878/brook.png"],
    "Jinbe": ["https://cdn.discordapp.com/attachments/1106203918729478195/1106224015900692530/jinbe.png"],

    #104 more
    
    # wano
    "Kawamatsu": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237497815175188/3557.png"],
    "Oden": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237498112983050/3553.png"],
    "Momonosuke": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237498364624926/2790.png"],
    "Hiyori": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237498712756245/2775.png"],
    "Raizo": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499027341382/1660.png"],
    "Kikunojo": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499316731984/2994.png"],
    "Izou": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499622920303/979.png"],
    "Denjiro": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499916533911/3382.png"],
    "Kinemon": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237500218507314/3392.png"],
    "Ashura Doji": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237500486946846/2813.png"],
    "Shinobu": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237536293716058/3569.png"],
    "Toko": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237536608301106/2988.png"],
    "Tama": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237537254211625/2931.png"],
    "Hyogoro": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237536914481222/3147.png"],
    "Orochimaru": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237537539432519/3381.png"],
    "Kanjuro": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237537782693968/3380.png"],
    "Yamato": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107237538122440724/3430.png"],
    "Sasaki": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107238794396184660/3431.png"],
    "Black Maria": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107238794769473566/3434.png"],
    "Whos Who": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107238795121799268/3435.png"],
    "Ulti": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107238795419590736/3871.png"],
    "Page One": ["https://cdn.discordapp.com/attachments/1107237323780927558/1107238795830628392/3873.png"],

    # wholecake

    "Reiju": ["https://cdn.discordapp.com/attachments/1107237651444137995/1107237794729955378/2453.png"],
    "Pudding": ["https://cdn.discordapp.com/attachments/1107237651444137995/1107238558638542868/1963.png"],
    "Perospero": ["https://cdn.discordapp.com/attachments/1107237651444137995/1107238558982479872/3242.png"],
    "Flampe": ["https://cdn.discordapp.com/attachments/1107237651444137995/1107238559448051732/2367.png"],

    # zou

    "Carrot": ["https://cdn.discordapp.com/attachments/1107237562373902377/1107237642183135233/3212.png"],
    "Inuarashi": ["https://cdn.discordapp.com/attachments/1107237562373902377/1107237642631909406/3178.png"],
    "Nekomamushi": ["https://cdn.discordapp.com/attachments/1107237562373902377/1107237643374317608/3180.png"],
    "Pedro": ["https://cdn.discordapp.com/attachments/1107237562373902377/1107237643848269864/1654.png"],
    "Wanda": ["https://cdn.discordapp.com/attachments/1107237562373902377/1107237644154441818/1573.png"],

    # dressrosa

    "Trebol": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238072883609710/1908.png"],
    "Doflamingo": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238073294671893/2444.png"],
    "Rebecca": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238073722470461/403.png"],
    "Viola": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238074007703593/995.png"],
    "Don Chinjao": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238074406142003/1025.png"],
    "Senor Pink": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238074720727191/1904.png"],
    "Sugar": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238075056279633/1906.png"],
    "Vergo": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238075400204308/840.png"],
    "Pica": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238075664453642/932.png"],
    "Diamante": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107238076029337621/1796.png"],
    "Cavendish": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107239429216682004/1122.png"],
    "Bartolomeow": ["https://cdn.discordapp.com/attachments/1107237839911006228/1107239436376358983/1879.png"],
    
    # supernovas
    
    "X Drake": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107239224589156392/3436.png"],
    "Basil Hawkins": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238376895152148/2729.png"],
    "Urouge": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238377293627442/781.png"],
    "Jewelry Bonney": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238377641750558/3307.png"],
    "Capone Bege": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238378191192064/2735.png"],
    "Killer": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238378581274644/3343.png"],
    "Eustass Kid": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238379109761085/3630.png"],
    "Bepo": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238379403346011/3633.png"],
    "Trafalgar Law": ["https://cdn.discordapp.com/attachments/1107238089065246790/1107238379717931008/3336.png"],

    # warlords

    "Buggy": ["https://cdn.discordapp.com/attachments/1107238861895110766/1107238933970046996/2035.png"],
    "Mihawk": ["https://cdn.discordapp.com/attachments/1107238861895110766/1107238934288793640/1680.png"],
    "Crocodile": ["https://cdn.discordapp.com/attachments/1107238861895110766/1107238934624342096/2876.png"],
    "Gecko Moria": ["https://cdn.discordapp.com/attachments/1107238861895110766/1107238934959902752/3409.png"],
    "Boa Hancock": ["https://cdn.discordapp.com/attachments/1107238861895110766/1107239086072279110/3246.png"],
    "Weevil": ["https://cdn.discordapp.com/attachments/1107238861895110766/1107239086353289326/3247.png"],

    # gov affiliated

    "Koby": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239609508831302/3480.png"],
    "Rosinante": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239609827602532/1000.png"],
    "Smoker": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239610217664522/3006.png"],
    "Tashigi": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239612507762698/2068.png"],
    "Hina": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239610620321792/2027.png"],
    "Tsuru": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239610981027960/1319.png"],
    "Magellan": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239611236884510/2159.png"],
    "Kalifa": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239611534684212/2761.png"],
    "Blueno": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239611891191918/1138.png"],
    "Sentomaru": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239612168019998/1469.png"],
    "Stussy": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239668048740382/3000.png"],
    "Kaku": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239668568821820/2482.png"],
    "Rob Lucci": ["https://cdn.discordapp.com/attachments/1107239377941299210/1107239668854046750/2670.png"],
    "Akainu": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106232045212016751/akainu.png"],
    "Aokiji": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106232044767424592/aokiji.png"],
    "Kizaru": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106232045711142953/kizaru.png"],
    "Fujitora": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106232046327701504/fujitora.png"],
    "Garp": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106232043790147606/garp.png"],
    "Sengoku": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106232044318625953/sengoku.png"],

    # revolutionaries
    
    "Kuma": ["https://cdn.discordapp.com/attachments/1107239923234381935/1107239984181805167/2193.png"],
    "Belo Betty": ["https://cdn.discordapp.com/attachments/1107239923234381935/1107239985226186802/2564.png"],
    "Lindbergh": ["https://cdn.discordapp.com/attachments/1107239923234381935/1107239984479608862/2563.png"],
    "Karasu": ["https://cdn.discordapp.com/attachments/1107239923234381935/1107239985586901022/2567.png"],
    "Ivankov": ["https://cdn.discordapp.com/attachments/1107239923234381935/1107239985914060860/1701.png"],
    "Sabo": ["https://cdn.discordapp.com/attachments/1107239923234381935/1107239986278961172/2684.png"],

    # alabasta thriller skypeia water7

    "Ryuma": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240542192025620/3396.png"],
    "Perona": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240542598864946/2499.png"],
    "Iceburg": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240542976360498/2392.png"],
    "Tom": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240543332872193/847.png"],
    "Enel": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240543605497927/2232.png"],
    "Karoo": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240543941046292/444.png"],
    "Vivi": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240544230449162/3667.png"],
    "Laboon": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240544549224498/214.png"],
    "Crocus": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240544897343548/3183.png"],
    "Oars": ["https://cdn.discordapp.com/attachments/1107240346649382993/1107240545186758737/2755.png"],

    # east blue

    "Wapol": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240724333871144/3526.png"],
    "Kaya": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240724870746142/502.png"],
    "Zeff": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240725176918076/2150.png"],
    "Makino": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240725449556030/2388.png"],
    "Gin": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240725789298769/1424.png"],
    "Don Krieg": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240726103867473/1489.png"],
    "Kuro": ["https://cdn.discordapp.com/attachments/1107240611444174899/1107240726498136064/1458.png"],

    # fishman punk

    "Shirahoshi": ["https://cdn.discordapp.com/attachments/1107240782332698714/1107240829019500605/2631.png"],
    "Caesar": ["https://cdn.discordapp.com/attachments/1107240782332698714/1107240829610901615/2731.png"],
    "Hody Jones": ["https://cdn.discordapp.com/attachments/1107240782332698714/1107240829325680660/2720.png"],

    # rand

    "Foxy": ["https://cdn.discordapp.com/attachments/1107240881590910977/1107240898162589736/568.png"],
    "Shiki": ["https://cdn.discordapp.com/attachments/1107240881590910977/1107241005352230932/2201.png"],
    "Uta": ["https://cdn.discordapp.com/attachments/1107240881590910977/1107241005796823130/3713.png"],
    "Rayleigh": ["https://cdn.discordapp.com/attachments/1107240881590910977/1107241006216257606/3018.png"],
    "Roger": ["https://cdn.discordapp.com/attachments/1107240881590910977/1107241006526627931/3177.png"],

    # whitebeards

    "Whitebeard": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231385687085208/whitebeard.png"],
    "Marco": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231385246666782/marco.png"],
    "Jozu": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231384902746122/jozu.png"],
    "Ace": ["https://cdn.discordapp.com/attachments/1106203961679155290/1106231385976488046/ace.png"],

    "Gaimon": ["https://cdn.discordapp.com/attachments/1107240881590910977/1108200361526829136/gaimon.png"],
}



# SEPARATE CHARACTERS BY CREW/AFFILIATION FOR BETTER SORTING, ADD MORE CHARACTERS INTO THIS FILE


#    "": "",