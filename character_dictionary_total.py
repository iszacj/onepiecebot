
class Character():
    def __init__(self,name,level,picture,special_name, description):
        self.name = name
        self.level = level
        self.picture = picture
        self.special_name = special_name
        self.description = description

#"Character name: [[Image Urls],[Probabilities of the corresponding image],[corresponding special names],[descriptions]


characters_pictures = {
    "Shanks": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231484177715261/shanks.png","https://cdn.discordapp.com/attachments/1106203961679155290/1106231484634890250/benn_beckman.png"],[0.8,0.2],["", "Halloween Shanks"],
    ["Shanks Normal Desc", "Shanks Special Desc"]],

    "Benn Beckman": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231484634890250/benn_beckman.png"],[1],[""],
    [""]],

    "Lucky Roux": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231483535982592/lucky_roux.png"],[1],[""],
    [""]],

    "Yasopp": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231483817017364/yasopp.png"],[1],[""],
    [""]],

    "Kaido": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231544558911518/kaido.png"],[1],[""],
    [""]],

    "King": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231544865103952/king.png"],[1],[""],
    [""]],

    "Queen": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231543787167744/queen.png"],[1],[""],
    [""]],

    "Jack": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231544214995006/jack.png"],[1],[""],
    [""]],

    "Big Mom": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231323636547644/big_mom.png"],[1],[""],
    [""]],

    "Katakuri": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231323250655364/katakuri.png"],[1],[""],
    [""]],

    "Smoothie": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231323967881247/smoothie.png"],[1],[""],
    [""]],

    "Cracker": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231322852212766/cracker.png"],[1],[""],
    [""]],

    "Blackbeard": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231447242690669/blackbeard.png"],[1],[""],
    [""]],

    "Jesus Burgess": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231447540473976/jesus_burges.png"],[1],[""],
    [""]],

    "Van Augur": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231446798082068/van_augr.png"],[1],[""],
    [""]],

    "Shiryu": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231446445772922/shiryu.png"],[1],[""],
    [""]],

    # strawhats

    "Luffy": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106220323159953468/IMG_1457.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040225625329694/2749.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040225310740501/3365.png"],[1],["", "Halloween Luffy", "Germa Luffy"],
    [""]],

    "Zoro": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106222017658765433/zoro.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040224660639784/2414.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040224983597107/3368.png"],[1],["", "Cowboy Zoro", "Germa Zoro"],
    [""]],

    "Nami": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106222008393547806/nami.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040226313195550/2763.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040225994412122/3367.png"],[1],["", "Halloween Nami", "Germa Nami"],
    [""]],

    "Usopp": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106221990106370068/usopp.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040265232125952/3679.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040264963702784/3371.png"],[1],["", "Kiss Usopp", "Germa Usopp"],
    [""]],

    "Sanji": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106221979893235712/sanji.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040265580249168/3112.png"],[1],["", "Halloween Sanji", "Three Musketeers Sanji"],
    [""]],

    "Chopper": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106221968560242688/chopper.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040266209398875/3551.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040265903226941/3366.png"],[1],["","Love-struck Chopper", "Germa Chopper"],
    [""]],

    "Nico Robin": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106223976180617247/robin.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040266565910558/3792.png", "https://cdn.discordapp.com/attachments/1109028698461589524/1109040266939219968/3370.png"],[1],["", "Devil Robin", "Germa Robin"],
    [""]],

    "Franky": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106223987232604190/franky.png"],[1],[""],
    [""]],

    "Brook": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106223997613518878/brook.png"],[1],[""],
    [""]],

    "Jinbe": [["https://cdn.discordapp.com/attachments/1106203918729478195/1106224015900692530/jinbe.png"],[1],[""],
    [""]],


    #104 more
    
    # wano
    "Kawamatsu": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237497815175188/3557.png"],[1],[""],
    [""]],

    "Oden": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237498112983050/3553.png"],[1],[""],
    [""]],

    "Momonosuke": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237498364624926/2790.png"],[1],[""],
    [""]],

    "Hiyori": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237498712756245/2775.png"],[1],[""],
    [""]],

    "Raizo": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499027341382/1660.png"],[1],[""],
    [""]],

    "Kikunojo": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499316731984/2994.png"],[1],[""],
    [""]],

    "Izou": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499622920303/979.png"],[1],[""],
    [""]],

    "Denjiro": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237499916533911/3382.png"],[1],[""],
    [""]],

    "Kinemon": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237500218507314/3392.png"],[1],[""],
    [""]],

    "Ashura Doji": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237500486946846/2813.png"],[1],[""],
    [""]],

    "Shinobu": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237536293716058/3569.png"],[1],[""],
    [""]],

    "Toko": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237536608301106/2988.png"],[1],[""],
    [""]],

    "Tama": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237537254211625/2931.png"],[1],[""],
    [""]],

    "Hyogoro": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237536914481222/3147.png"],[1],[""],
    [""]],

    "Orochimaru": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237537539432519/3381.png"],[1],[""],
    [""]],

    "Kanjuro": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237537782693968/3380.png"],[1],[""],
    [""]],

    "Yamato": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107237538122440724/3430.png"],[1],[""],
    [""]],

    "Sasaki": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107238794396184660/3431.png"],[1],[""],
    [""]],

    "Black Maria": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107238794769473566/3434.png"],[1],[""],
    [""]],

    "Whos Who": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107238795121799268/3435.png"],[1],[""],
    [""]],

    "Ulti": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107238795419590736/3871.png"],[1],[""],
    [""]],

    "Page One": [["https://cdn.discordapp.com/attachments/1107237323780927558/1107238795830628392/3873.png"],[1],[""],
    [""]],


    # wholecake

    "Reiju": [["https://cdn.discordapp.com/attachments/1107237651444137995/1107237794729955378/2453.png"],[1],[""],
    [""]],

    "Pudding": [["https://cdn.discordapp.com/attachments/1107237651444137995/1107238558638542868/1963.png"],[1],[""],
    [""]],

    "Perospero": [["https://cdn.discordapp.com/attachments/1107237651444137995/1107238558982479872/3242.png"],[1],[""],
    [""]],

    "Flampe": [["https://cdn.discordapp.com/attachments/1107237651444137995/1107238559448051732/2367.png"],[1],[""],
    [""]],


    # zou

    "Carrot": [["https://cdn.discordapp.com/attachments/1107237562373902377/1107237642183135233/3212.png"],[1],[""],
    [""]],

    "Inuarashi": [["https://cdn.discordapp.com/attachments/1107237562373902377/1107237642631909406/3178.png"],[1],[""],
    [""]],

    "Nekomamushi": [["https://cdn.discordapp.com/attachments/1107237562373902377/1107237643374317608/3180.png"],[1],[""],
    [""]],

    "Pedro": [["https://cdn.discordapp.com/attachments/1107237562373902377/1107237643848269864/1654.png"],[1],[""],
    [""]],

    "Wanda": [["https://cdn.discordapp.com/attachments/1107237562373902377/1107237644154441818/1573.png"],[1],[""],
    [""]],


    # dressrosa

    "Trebol": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238072883609710/1908.png"],[1],[""],
    [""]],

    "Doflamingo": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238073294671893/2444.png"],[1],[""],
    [""]],

    "Rebecca": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238073722470461/403.png"],[1],[""],
    [""]],

    "Viola": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238074007703593/995.png"],[1],[""],
    [""]],

    "Don Chinjao": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238074406142003/1025.png"],[1],[""],
    [""]],

    "Senor Pink": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238074720727191/1904.png"],[1],[""],
    [""]],

    "Sugar": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238075056279633/1906.png"],[1],[""],
    [""]],

    "Vergo": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238075400204308/840.png"],[1],[""],
    [""]],

    "Pica": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238075664453642/932.png"],[1],[""],
    [""]],

    "Diamante": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107238076029337621/1796.png"],[1],[""],
    [""]],

    "Cavendish": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107239429216682004/1122.png"],[1],[""],
    [""]],

    "Bartolomeow": [["https://cdn.discordapp.com/attachments/1107237839911006228/1107239436376358983/1879.png"],[1],[""],
    [""]],

    
    # supernovas
    
    "X Drake": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107239224589156392/3436.png"],[1],[""],
    [""]],

    "Basil Hawkins": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238376895152148/2729.png"],[1],[""],
    [""]],

    "Urouge": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238377293627442/781.png"],[1],[""],
    [""]],

    "Jewelry Bonney": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238377641750558/3307.png"],[1],[""],
    [""]],

    "Capone Bege": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238378191192064/2735.png"],[1],[""],
    [""]],

    "Killer": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238378581274644/3343.png"],[1],[""],
    [""]],

    "Eustass Kid": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238379109761085/3630.png"],[1],[""],
    [""]],

    "Bepo": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238379403346011/3633.png"],[1],[""],
    [""]],

    "Trafalgar Law": [["https://cdn.discordapp.com/attachments/1107238089065246790/1107238379717931008/3336.png"],[1],[""],
    [""]],


    # warlords

    "Buggy": [["https://cdn.discordapp.com/attachments/1107238861895110766/1107238933970046996/2035.png"],[1],[""],
    [""]],

    "Mihawk": [["https://cdn.discordapp.com/attachments/1107238861895110766/1107238934288793640/1680.png"],[1],[""],
    [""]],

    "Crocodile": [["https://cdn.discordapp.com/attachments/1107238861895110766/1107238934624342096/2876.png"],[1],[""],
    [""]],

    "Gecko Moria": [["https://cdn.discordapp.com/attachments/1107238861895110766/1107238934959902752/3409.png"],[1],[""],
    [""]],

    "Boa Hancock": [["https://cdn.discordapp.com/attachments/1107238861895110766/1107239086072279110/3246.png"],[1],[""],
    [""]],

    "Weevil": [["https://cdn.discordapp.com/attachments/1107238861895110766/1107239086353289326/3247.png"],[1],[""],
    [""]],


    # gov affiliated

    "Koby": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239609508831302/3480.png"],[1],[""],
    [""]],

    "Rosinante": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239609827602532/1000.png"],[1],[""],
    [""]],

    "Smoker": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239610217664522/3006.png"],[1],[""],
    [""]],

    "Tashigi": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239612507762698/2068.png"],[1],[""],
    [""]],

    "Hina": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239610620321792/2027.png"],[1],[""],
    [""]],

    "Tsuru": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239610981027960/1319.png"],[1],[""],
    [""]],

    "Magellan": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239611236884510/2159.png"],[1],[""],
    [""]],

    "Kalifa": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239611534684212/2761.png"],[1],[""],
    [""]],

    "Blueno": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239611891191918/1138.png"],[1],[""],
    [""]],

    "Sentomaru": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239612168019998/1469.png"],[1],[""],
    [""]],

    "Stussy": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239668048740382/3000.png"],[1],[""],
    [""]],

    "Kaku": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239668568821820/2482.png"],[1],[""],
    [""]],

    "Rob Lucci": [["https://cdn.discordapp.com/attachments/1107239377941299210/1107239668854046750/2670.png"],[1],[""],
    [""]],

    "Akainu": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106232045212016751/akainu.png"],[1],[""],
    [""]],

    "Aokiji": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106232044767424592/aokiji.png"],[1],[""],
    [""]],

    "Kizaru": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106232045711142953/kizaru.png"],[1],[""],
    [""]],

    "Fujitora": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106232046327701504/fujitora.png"],[1],[""],
    [""]],

    "Garp": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106232043790147606/garp.png"],[1],[""],
    [""]],

    "Sengoku": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106232044318625953/sengoku.png"],[1],[""],
    [""]],


    # revolutionaries
    
    "Kuma": [["https://cdn.discordapp.com/attachments/1107239923234381935/1107239984181805167/2193.png"],[1],[""],
    [""]],

    "Belo Betty": [["https://cdn.discordapp.com/attachments/1107239923234381935/1107239985226186802/2564.png"],[1],[""],
    [""]],

    "Lindbergh": [["https://cdn.discordapp.com/attachments/1107239923234381935/1107239984479608862/2563.png"],[1],[""],
    [""]],

    "Karasu": [["https://cdn.discordapp.com/attachments/1107239923234381935/1107239985586901022/2567.png"],[1],[""],
    [""]],

    "Ivankov": [["https://cdn.discordapp.com/attachments/1107239923234381935/1107239985914060860/1701.png"],[1],[""],
    [""]],

    "Sabo": [["https://cdn.discordapp.com/attachments/1107239923234381935/1107239986278961172/2684.png"],[1],[""],
    [""]],


    # alabasta thriller skypeia water7

    "Ryuma": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240542192025620/3396.png"],[1],[""],
    [""]],

    "Perona": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240542598864946/2499.png"],[1],[""],
    [""]],

    "Iceburg": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240542976360498/2392.png"],[1],[""],
    [""]],

    "Tom": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240543332872193/847.png"],[1],[""],
    [""]],

    "Enel": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240543605497927/2232.png"],[1],[""],
    [""]],

    "Karoo": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240543941046292/444.png"],[1],[""],
    [""]],

    "Vivi": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240544230449162/3667.png"],[1],[""],
    [""]],

    "Laboon": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240544549224498/214.png"],[1],[""],
    [""]],

    "Crocus": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240544897343548/3183.png"],[1],[""],
    [""]],

    "Oars": [["https://cdn.discordapp.com/attachments/1107240346649382993/1107240545186758737/2755.png"],[1],[""],
    [""]],


    # east blue

    "Wapol": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240724333871144/3526.png"],[1],[""],
    [""]],

    "Kaya": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240724870746142/502.png"],[1],[""],
    [""]],

    "Zeff": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240725176918076/2150.png"],[1],[""],
    [""]],

    "Makino": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240725449556030/2388.png"],[1],[""],
    [""]],

    "Gin": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240725789298769/1424.png"],[1],[""],
    [""]],

    "Don Krieg": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240726103867473/1489.png"],[1],[""],
    [""]],

    "Kuro": [["https://cdn.discordapp.com/attachments/1107240611444174899/1107240726498136064/1458.png"],[1],[""],
    [""]],


    # fishman punk

    "Shirahoshi": [["https://cdn.discordapp.com/attachments/1107240782332698714/1107240829019500605/2631.png"],[1],[""],
    [""]],

    "Caesar": [["https://cdn.discordapp.com/attachments/1107240782332698714/1107240829610901615/2731.png"],[1],[""],
    [""]],

    "Hody Jones": [["https://cdn.discordapp.com/attachments/1107240782332698714/1107240829325680660/2720.png"],[1],[""],
    [""]],


    # rand

    "Foxy": [["https://cdn.discordapp.com/attachments/1107240881590910977/1107240898162589736/568.png"],[1],[""],
    [""]],

    "Shiki": [["https://cdn.discordapp.com/attachments/1107240881590910977/1107241005352230932/2201.png"],[1],[""],
    [""]],

    "Uta": [["https://cdn.discordapp.com/attachments/1107240881590910977/1107241005796823130/3713.png"],[1],[""],
    [""]],

    "Rayleigh": [["https://cdn.discordapp.com/attachments/1107240881590910977/1107241006216257606/3018.png"],[1],[""],
    [""]],

    "Roger": [["https://cdn.discordapp.com/attachments/1107240881590910977/1107241006526627931/3177.png"],[1],[""],
    [""]],


    # whitebeards

    "Whitebeard": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231385687085208/whitebeard.png"],[1],[""],
    [""]],

    "Marco": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231385246666782/marco.png"],[1],[""],
    [""]],

    "Jozu": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231384902746122/jozu.png"],[1],[""],
    [""]],

    "Ace": [["https://cdn.discordapp.com/attachments/1106203961679155290/1106231385976488046/ace.png"],[1],[""],
    [""]],


    "Gaimon": [["https://cdn.discordapp.com/attachments/1107240881590910977/1108200361526829136/gaimon.png"],[1],[""],
    [""]],

}



# SEPARATE CHARACTERS BY CREW/AFFILIATION FOR BETTER SORTING, ADD MORE CHARACTERS INTO THIS FILE


#    "": "",