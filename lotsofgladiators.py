from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

import random

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

fake_gladiators = ["Slam", "Chop", "Zoom", "Slide", "Crater", "Lynx", "Power",
                   "Roundabout", "Cutthroat", "Firework", "Arrow", "Harmonica",
                   "Tooth", "Lavender", "Highwind"]

real_gladiators = ["Malibu", "Lace", "Zap", "Gemini", "Nitro", "Sunny",
                   "Blaze", "Bronco", "Gold", "Laser", "Jade", "Titan",
                   "Diamond", "Ice", "Thunder", "Turbo", "Storm", "Tower",
                   "Viper", "Atlas", "Cyclone", "Elektra", "Lace", "Havoc",
                   "Sabre", "Siren", "Sky", "Dallas", "Hawk", "Jazz",
                   "Rebel", "Tank"]

male_photos = ["https://img.buzzfeed.com/buzzfeed-static/static/2014-11/11/19/campaign_images/webdr11/these-brad-pitt-photos-from-1987-are-wonderfully--2-10500-1415753132-12_dblbig.jpg",  # NOQA
               "https://d3jjg4nf4bbybe.cloudfront.net/u/54/b46162a58188e6fde286b06e355f6425b710f7c7/photo/254843-231176963562919-7144621-n.jpg",  # NOQA
               "https://lunchat1130.files.wordpress.com/2013/09/rob-lowe-in-the-80s.jpg?w=304",  # NOQA
               "https://vignette.wikia.nocookie.net/americangladiators/images/4/4b/Malibu.jpg/revision/latest?cb=20120207050448",  # NOQA
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr5MaOmD-4sMPsbflrWxyCTklEWA9aJ_OJlKrwDVobVDYhDd2org",  # NOQA
               "http://towleroad.com/wp-content/uploads/2009/01/6a00d8341c730253ef010536b44906970c-640wi.jpg",  # NOQA
               "https://cdn-ami-drupal.heartyhosting.com/sites/muscleandfitness.com/files/styles/full_node_image_1090x614/public/media/Jim-starr.jpg?itok=5RWkHEgA&timestamp=1479244555",  # NOQA
               "http://cdn.skim.gs/image/upload/v1456338829/msi/American-Gladiators-Wolf_okkzdq.jpg",  # NOQA
               "https://www.getbig.com/news/2007/12/amglad/titan009.jpg",  # NOQA
               "http://www.liketotally80s.com/wp-content/uploads/2016/03/American-Gladiators-Hawk.jpg",  # NOQA
               "http://mightygodking.com/images/gladiators/toa.jpg",  # NOQA
               "http://www.canmag.com/images/front/tv/gladiator9.jpg",  # NOQA
               "https://heystupid.files.wordpress.com/2007/04/turbo5.jpg?w=500",  # NOQA
               "https://i2-prod.mirror.co.uk/incoming/article6300762.ece/ALTERNATES/s615b/Gladiators-TV-Game-Show-1990s-Shadow-Jefferson-King.jpg",  # NOQA
               "http://img.photobucket.com/albums/v166/ryanmediocre/AGJustice.jpg",  # NOQA
               "https://i.pinimg.com/236x/5c/b1/82/5cb18222d2a073829b84e8dd5d70ba08--dan-clark-american-gladiators.jpg",  # NOQA
               "https://i.pinimg.com/originals/12/9e/50/129e500c6f6f85c7f297e641bd38d437.jpg",  # NOQA
               "https://i.pinimg.com/736x/e8/37/58/e83758c68f980312139ed0395a713610--american-gladiators-motivation.jpg",  # NOQA
               "https://www.mensjournal.com/wp-content/uploads/mf/whittenburg_main.jpg",  # NOQA
               "https://i.pinimg.com/736x/6a/1d/7e/6a1d7ea608be206e5a45e9e035cea21e.jpg",  # NOQA
               "http://digitalspyuk.cdnds.net/17/20/980x1257/gallery-1495203177-uktv-gladiators-mark-griffin.jpg",  # NOQA
               "https://keyassets-p2.timeincuk.net/wp/prod/wp-content/uploads/sites/42/2018/04/rexfeatures_8999250dw-630x400.jpg",  # NOQA
               "https://www.telegraph.co.uk/content/dam/tv/2016/04/02/glad_trans_NvBQzQNjv4Bqeo_i_u9APj8RuoebjoAHt0k9u7HhRJvuo-ZLenGRumA.jpg?imwidth=450",  # NOQA
               "http://cdn1.spiegel.de/images/image-963944-860_poster_16x9-qeec-963944.jpg",  # NOQA
               "http://i.dailymail.co.uk/i/pix/2015/08/14/21/2B5CB43300000578-3198351-Australian_Gladiator_Vulcan_whose_real_name_is_John_Seru_was_dra-m-142_1439584000281.jpg",  # NOQA
               "http://i.dailymail.co.uk/i/pix/2015/08/14/19/2B5CB45700000578-3198351-image-m-101_1439577243349.jpg",  # NOQA
               "http://cdn.playbuzz.com/cdn/71e590fd-242c-42ba-9d9f-3cf68071f8e2/08994ed9-63a3-45cb-855d-96be5eaf60da.jpg",  # NOQA
               "http://home.bt.com/images/hunter-136416163030902601",  # NOQA
               "http://magarticles.magzter.com/articles/3401/192164/5811968d6e536/All-American-Gladiator.jpg",  # NOQA
               "http://digitalspyuk.cdnds.net/17/20/980x1274/gallery-1495202767-uktv-gladiators-jefferson-king.jpg",  # NOQA
               "http://i1.cdnds.net/15/18/618x660/uktv-gladiators-michael-van-wijk.jpg",  # NOQA
               "http://oi25.photobucket.com/albums/c52/FlangMasterJ/05e2e2dd.jpg",  # NOQA
               "https://www.telegraph.co.uk/content/dam/tv/2016/04/02/glad-xlarge_trans_NvBQzQNjv4Bqeo_i_u9APj8RuoebjoAHt0k9u7HhRJvuo-ZLenGRumA.jpg",  # NOQA
               "https://i.kinja-img.com/gawker-media/image/upload/s--U4MaQh8x--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/iachmahq4cdrovjol6md.jpg",  # NOQA
               "http://www.nydailynews.com/resizer/ONUraV-AIzVUyiB-348el7cyG1o=/1400x0/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/Z3DV6V6KYIXJDT2HNHCTIEQKDE.jpg",  # NOQA
               "https://www.nbc.com/sites/nbcunbc/files/files/styles/1080xauto/public/scet/photos/146/1590/NUP_113212_0037.jpg?itok=o7LyJuZn",  # NOQA
               "https://www.telegraph.co.uk/content/dam/tv/2016/04/05/Wolf_trans_NvBQzQNjv4Bqp2HdEvMdCw5n3XrRYSzui4CzqtU_MAlWPJoBYdDCpMs.jpg",  # NOQA
               "http://cimg.tvgcdn.net/i/2017/03/17/675394e9-6245-48cc-b4b7-7b674bcdd7b6/c3e6f2587e3077e84933b0ad4a86c4b4/170317-news-american-ninja-warrior.jpg",  # NOQA
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_cWNQuqmTP0pmn81u0DXQ9qvmll1edhCGZ899l374P3dB9JTy-Q",  # NOQA
               "https://www.telegraph.co.uk/content/dam/tv/2016/04/05/Hunter_trans_NvBQzQNjv4Bq2iH8Z9UDmET2NfUmE0cLq1WJj_C5aiUQVsoT2QvHlIs.jpg"]  # NOQA

female_photos = ["https://static.businessinsider.com/image/515ba38becad043510000013-750.jpg",  # NOQA
                 "http://i.dailymail.co.uk/i/newpix/2018/04/30/14/4BB49C4800000578-5673211-image-a-189_1525093312562.jpg",  # NOQA
                 "https://imagesvc.timeincapp.com/v3/mm/image?url=https%3A%2F%2Fcdn-img.instyle.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F684xflex%2Fpublic%2Fimages%2F2014%2FGALLERY%2F013114-original-supermodels-7-567_0.jpg%3Fitok%3DY5P4PB6Y&w=700&q=85",  # NOQA
                 "https://ksassets.timeincuk.net/wp/uploads/sites/46/2016/05/rexfeatures-111118a-1.jpg",  # NOQA
                 "http://www.canmag.com/images/front/tv/gladiator8.jpg",  # NOQA
                 "http://www.getbig.com/boards/index.php?action=dlattach;topic=184144.0;attach=220012;image",  # NOQA
                 "http://www.canmag.com/images/front/tv/gladiator14.jpg",  # NOQA
                 "http://lmnop.blogs.com/photos/uncategorized/2008/05/12/venom.jpg",  # NOQA
                 "http://ilarge.lisimg.com/image/5922651/740full-valerie-waugaman.jpg",  # NOQA
                 "http://www.fightinginsider.com/wp-content/uploads/2010/11/gina-carano.jpg",  # NOQA
                 "http://media.liveauctiongroup.net/i/33534/28843451_1.jpg?v=8D548A8B2BB7B10",  # NOQA
                 "https://i.ytimg.com/vi/oHRKF1XUeZ4/hqdefault.jpg",  # NOQA
                 "https://i.pinimg.com/474x/06/43/eb/0643eb23dfbd48f3fbfe9cebd8d2806a--american-gladiators--lbs.jpg",  # NOQA
                 "https://i.pinimg.com/originals/eb/5d/bb/eb5dbb47463201aba1784085f8912836.jpg",  # NOQA
                 "http://mightygodking.com/images/gladiators/stealth.jpg",  # NOQA
                 "http://www.afterellen.com/assets/uploads/venom-joust-12182007.jpg",  # NOQA
                 "http://i.dailymail.co.uk/i/pix/2015/08/14/19/2B5CB3C300000578-3198351-image-a-112_1439577412095.jpg",  # NOQA
                 "https://i.pinimg.com/originals/df/86/f9/df86f9051e77f11d9c642ccf96ac9f8c.jpg",  # NOQA
                 "http://i.ytimg.com/vi/Pa8P25fe2as/hqdefault.jpg",  # NOQA
                 "https://cdn-s3.si.com/s3fs-public/2016/07/01/american-gladiators-rings.jpg",  # NOQA
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnzNKgWe66JA47ECjx0sd8QyKng2Rx6zEza7q8flmnGvUH8JJH",  # NOQA
                 "http://www.getbig.com/news/2007/12/amglad/stealth002.jpg",  # NOQA
                 "http://3.bp.blogspot.com/_2-7AdSkZA7I/SaQW89gdzWI/AAAAAAAAUtE/cTnKtq9ZP0M/s400/Erin+Toughill-mma.jpg",  # NOQA
                 "https://femuscleblog.files.wordpress.com/2014/12/730467492.jpg",  # NOQA
                 "http://digitalspyuk.cdnds.net/17/20/980x1247/gallery-1495202896-uktv-gladiators-bernadette-hunt.jpg",  # NOQA
                 "http://digitalspyuk.cdnds.net/15/52/768x994/gallery-uktv-gladiators-helen-oreilly.jpg",  # NOQA
                 "https://i2-prod.chroniclelive.co.uk/incoming/article9853117.ece/ALTERNATES/s615/JS70000211.jpg",  # NOQA
                 "https://1.bp.blogspot.com/_DiyxVzBLalc/R2LfXFqdsLI/AAAAAAAAAt0/KSuyFuGWCVk/s400/fury.jpg",  # NOQA
                 "http://sharrondavies.co.uk/wp-content/uploads/2013/03/cv-pics-019.jpg",  # NOQA
                 "https://www.nbc.com/sites/nbcunbc/files/files/styles/1080xauto/public/scet/photos/146/1590/NUP_112968_0236.jpg?itok=BNPz_8dX",  # NOQA
                 "https://www.nbc.com/sites/nbcunbc/files/files/styles/768xauto/public/scet/photos/146/1538/NUP_112957_0592.jpg?itok=hCpwIbgu",  # NOQA
                 "https://i.ytimg.com/vi/3KdlakJ6FMM/maxresdefault.jpg",  # NOQA
                 "https://campgladiator.com/wp-content/uploads/2016/02/cg-about-6-1350x980.jpg",  # NOQA
                 "https://static.independent.co.uk/s3fs-public/thumbnails/image/2013/06/18/15/Eunice-Huthart.jpg",  # NOQA
                 "https://www.gannett-cdn.com/-mm-/0c9109c71ea0524d9fe840f91fabd67bb94a26a9/r=537&c=0-0-534-712/local/-/media/USATODAY/USATODAY/2013/06/30/1372624450000-AMERICAN-NINJA-WARRIOR---TV-jy-0463-1306301636_3_4.jpg",  # NOQA
                 "https://i.pinimg.com/originals/66/25/47/662547eb86e8bdc070c532bfd05b9333.jpg",  # NOQA
                 "https://orig00.deviantart.net/34c2/f/2016/230/5/9/gladiators_venom_and_jet_by_fatehound45-daeeygk.jpg",  # NOQA
                 "https://i.pinimg.com/originals/a6/f3/0b/a6f30bec468e917562211b00782b1815.jpg",  # NOQA
                 "http://digitalspyuk.cdnds.net/17/20/980x1283/gallery-1495202614-uktv-gladiators-nikki-diamond.jpg",  # NOQA
                 "http://dz8z45gu0xcif.cloudfront.net/wp-content/uploads/2017/11/06084316/07d25f45_ronda-rousey-main.xxxlarge_2x-e1509957856905.jpg"]  # NOQA

genders = ["female", "male"]

hairdos = ["spiked", "mullet", "ponytail", "man bun", "mohawk", "bald",
           "flattop", "dreads", "braids", "bowl cut", "crew cut",
           "feathered", "curled", "long", "rattail", "shaved"]

events = ["Pyramid", "Hang Tough", "Assault", "Joust", "Whiplash",
          "Gauntlet", "Tug O War", "Snapback", "Powerball", "Swingshot",
          "Breakthrough and Conquer", "Skytrack", "The Wall"]

accessories = ["headband", "gold chain", "sunglasses", "wristbands",
               "bubblegum", "shark-tooth necklace", "high socks", "brace",
               "cross earring", "hair mousse", "suspenders", "elbow pads",
               "knee pads"]


def randomizer(list):
    return random.choice(list)


def create_gladiator(person):
    gladiator = Gladiator(name=person, gender=randomizer(genders),
                          hairdo=randomizer(hairdos),
                          main_event=randomizer(events),
                          secondary_event=randomizer(events),
                          accessory=randomizer(accessories))

    if gladiator.gender == "female":
        gladiator.img = randomizer(female_photos)
        female_photos.pop(female_photos.index(gladiator.img))
    else:
        gladiator.img = randomizer(male_photos)
        male_photos.pop(male_photos.index(gladiator.img))

    while gladiator.secondary_event == gladiator.main_event:
        gladiator.secondary_event = randomizer(events)

    session.add(gladiator)
    session.commit()


all_gladiators = real_gladiators + fake_gladiators

for gladiator in all_gladiators:
    create_gladiator(gladiator)

print "Added gladiators!"


# class Gladiator(Base):
#     __tablename__ = "gladiator"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80))
#     img = Column(String)
#     gender = Column(String(12))
#     hairdo = Column(String(20))
#     main_event = Column(String(40))
#     secondary_event = Column(String(40))
#     accessory = Column(String(20))
