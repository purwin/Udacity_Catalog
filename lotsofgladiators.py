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

male_photos = ["https://img.buzzfeed.com/buzzfeed-static/static/2014-11/11/19/campaign_images/webdr11/these-brad-pitt-photos-from-1987-are-wonderfully--2-10500-1415753132-12_dblbig.jpg",
               "https://d3jjg4nf4bbybe.cloudfront.net/u/54/b46162a58188e6fde286b06e355f6425b710f7c7/photo/254843-231176963562919-7144621-n.jpg",
               "https://lunchat1130.files.wordpress.com/2013/09/rob-lowe-in-the-80s.jpg?w=304",
               "https://vignette.wikia.nocookie.net/americangladiators/images/4/4b/Malibu.jpg/revision/latest?cb=20120207050448",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr5MaOmD-4sMPsbflrWxyCTklEWA9aJ_OJlKrwDVobVDYhDd2org",
               "http://towleroad.com/wp-content/uploads/2009/01/6a00d8341c730253ef010536b44906970c-640wi.jpg",
               "https://cdn-ami-drupal.heartyhosting.com/sites/muscleandfitness.com/files/styles/full_node_image_1090x614/public/media/Jim-starr.jpg?itok=5RWkHEgA&timestamp=1479244555",
               "http://cdn.skim.gs/image/upload/v1456338829/msi/American-Gladiators-Wolf_okkzdq.jpg",
               "https://www.getbig.com/news/2007/12/amglad/titan009.jpg",
               "http://www.liketotally80s.com/wp-content/uploads/2016/03/American-Gladiators-Hawk.jpg",
               "http://mightygodking.com/images/gladiators/toa.jpg",
               "http://www.canmag.com/images/front/tv/gladiator9.jpg",
               "https://heystupid.files.wordpress.com/2007/04/turbo5.jpg?w=500",
               "https://i2-prod.mirror.co.uk/incoming/article6300762.ece/ALTERNATES/s615b/Gladiators-TV-Game-Show-1990s-Shadow-Jefferson-King.jpg", ]

female_photos = ["https://static.businessinsider.com/image/515ba38becad043510000013-750.jpg",
                 "http://i.dailymail.co.uk/i/newpix/2018/04/30/14/4BB49C4800000578-5673211-image-a-189_1525093312562.jpg",
                 "https://imagesvc.timeincapp.com/v3/mm/image?url=https%3A%2F%2Fcdn-img.instyle.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F684xflex%2Fpublic%2Fimages%2F2014%2FGALLERY%2F013114-original-supermodels-7-567_0.jpg%3Fitok%3DY5P4PB6Y&w=700&q=85",
                 "https://ksassets.timeincuk.net/wp/uploads/sites/46/2016/05/rexfeatures-111118a-1.jpg",
                 "http://www.canmag.com/images/front/tv/gladiator8.jpg",
                 "http://www.getbig.com/boards/index.php?action=dlattach;topic=184144.0;attach=220012;image",
                 "http://www.canmag.com/images/front/tv/gladiator14.jpg",
                 "http://lmnop.blogs.com/photos/uncategorized/2008/05/12/venom.jpg",
                 "http://ilarge.lisimg.com/image/5922651/740full-valerie-waugaman.jpg",
                 "http://www.fightinginsider.com/wp-content/uploads/2010/11/gina-carano.jpg",
                 "http://media.liveauctiongroup.net/i/33534/28843451_1.jpg?v=8D548A8B2BB7B10",
                 "https://i.ytimg.com/vi/oHRKF1XUeZ4/hqdefault.jpg",
                 "https://i.pinimg.com/474x/06/43/eb/0643eb23dfbd48f3fbfe9cebd8d2806a--american-gladiators--lbs.jpg",
                 "https://i.pinimg.com/originals/eb/5d/bb/eb5dbb47463201aba1784085f8912836.jpg",
                 "http://mightygodking.com/images/gladiators/stealth.jpg",
                 "http://www.afterellen.com/assets/uploads/venom-joust-12182007.jpg",
                 "http://i.dailymail.co.uk/i/pix/2015/08/14/19/2B5CB3C300000578-3198351-image-a-112_1439577412095.jpg",
                 "https://i.pinimg.com/originals/df/86/f9/df86f9051e77f11d9c642ccf96ac9f8c.jpg",
                 "http://i.ytimg.com/vi/Pa8P25fe2as/hqdefault.jpg",
                 "https://cdn-s3.si.com/s3fs-public/2016/07/01/american-gladiators-rings.jpg",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnzNKgWe66JA47ECjx0sd8QyKng2Rx6zEza7q8flmnGvUH8JJH",
                 "http://www.getbig.com/news/2007/12/amglad/stealth002.jpg",
                 "http://3.bp.blogspot.com/_2-7AdSkZA7I/SaQW89gdzWI/AAAAAAAAUtE/cTnKtq9ZP0M/s400/Erin+Toughill-mma.jpg"]

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
    hairdo=randomizer(hairdos), main_event=randomizer(events),
    secondary_event=randomizer(events), accessory=randomizer(accessories))

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
