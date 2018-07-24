from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

import random

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create genres
genre = {
    "type": "",
}

genre_catalog = []

class CreateGenre:
    def __init__(self, type):
        self.type = type

g_genre = CreateGenre(type).__dict__
genre_catalog.append(g_genre)


g_philosophy = CreateGenre("Philosophy").__dict__
genre_catalog.append(g_philosophy)

g_biography_memoir = CreateGenre("Biography &amp; Memoir").__dict__
genre_catalog.append(g_biography_memoir)

g_womens_fiction = CreateGenre("Women’s Fiction").__dict__
genre_catalog.append(g_womens_fiction)

g_literary_fiction = CreateGenre("Literary Fiction").__dict__
genre_catalog.append(g_literary_fiction)

g_historical_fiction = CreateGenre("Historical Fiction").__dict__
genre_catalog.append(g_historical_fiction)

g_humor = CreateGenre("Humor").__dict__
genre_catalog.append(g_humor)

g_cooking = CreateGenre("Cooking").__dict__
genre_catalog.append(g_cooking)

g_teen_fiction = CreateGenre("Teen &amp; Young Adult Fiction").__dict__
genre_catalog.append(g_teen_fiction)

g_children_picture = CreateGenre("Children’s Picture Books").__dict__
genre_catalog.append(g_children_picture)

# Create authors
author = {
    "last_name": "",
    "first_name": "",
    "bio": "",
}

author_catalog = []

class CreateAuthor:
    def __init__(self, last_name, first_name, bio = None):
        self.last_name = last_name
        self.first_name = first_name
        self.bio = bio

new_author = CreateAuthor(last_name, first_name, bio).__dict__
author_catalog.append(new_author)

m_pollan = CreateAuthor("Pollan", "Michael", "Michael Pollan, recently featured on Netflix in the four-part series <i>Cooked</i>, is the author of seven previous books, including <i>Food Rules</i>, <i>In Defense of Food</i>, <i>The Omnivore’s Dilemma</i>, and <i>The Botany of Desire</i>, all <i>New York Times</i> bestsellers. A longtime contributor to the <i>New York Times</i> Magazine, he is also the John S. and James L. Knight Professor of Journalism at Berkeley. In 2010, Time magazine named him one of the one hundred most influential people in the world.").__dict__
author_catalog.append(m_pollan)

m_wollitzer = CreateAuthor("Wolitzer", "Meg". "Meg Wolitzer is the New York Times–bestselling author of <i>The Interestings</i>, <i>The Uncoupling</i>, <i>The Ten-Year Nap</i>, <i>The Position</i>, <i>The Wife</i>, and <i>Sleepwalking</i>. She is also the author of the young adult novel <i>Belzhar</i>. Wolitzer lives in New York City.").__dict__
author_catalog.append(m_wollitzer)

c_whitehead = CreateAuthor("Whitehead", "Colson", "Colson Whitehead is the #1 New York Times bestselling author of <i>The Underground Railroad</i>, which in 2016 won the Pulitzer Prize in Fiction and the National Book Award and was named one of the Ten Best Books of the Year by <i>The New York Times</i> Book Review, as well as <i>The Noble Hustle</i>, <i>Zone One</i>, <i>Sag Harbor</i>, <i>The Intuitionist</i>, <i>John Henry Days</i>, <i>Apex Hides the Hurt</i>, and <i>The Colossus of New York</i>. He is also a Pulitzer Prize finalist and a recipient of the MacArthur and Guggenheim Fellowships. He lives in New York City.").__dict__
author_catalog.append(c_whitehead)

a_baldwin = CreateAuthor("Baldwin", "Alec", "Alec Baldwin is a multiple Emmy, Golden Globe, and Screen Actors Guild Award-winning actor, producer, comedian, and philanthropist. He has also been nominated for an Oscar and a Tony Award and the author of the New York Times bestseller <i>A Promise to Ourselves</i>.").__dict__
author_catalog.append(a_baldwin)

k_andersen = CreateAuthor("Andersen", "Kurt", "Kurt Andersen is author of <i>Heyday</i> and <i>Turn of the Century</i> and frequently writes for <i>New York</i> and <i>Vanity Fair</i>. He is host and cocreator of the Peabody Award–winning public radio program Studio 360. In 2006, he founded Very Short List, an email service for connoisseurs of culture who would never call themselves “connoisseurs.” He was cofounder of Spy magazine, and has been a columnist and critic for the <i>New Yorker</i> and <i>Time</i>. Andersen lives with his wife and daughters in Brooklyn.").__dict__
author_catalog.append(k_andersen)

m_clark = CreateAuthor("Clark", "Melissa", "Melissa Clark is a staff writer for the <i>New York Times</i> where she writes the popular column “A Good Appetite,” and stars in a weekly complementary video series. The winner of James Beard and IACP Awards, she is a regular on <i>Today</i> and NPR (<i>The Splendid Table</i>, <i>The Leonard Lopate Show</i>). Melissa earned an MFA in writing from Columbia.").__dict__
author_catalog.append(m_clark)

j_green = CreateAuthor("Green", "John", "John Green is the award-winning, #1 bestselling author of Looking for Alaska, An Abundance of Katherines, Paper Towns, Will Grayson, Will Grayson (with David Levithan), and The Fault in Our Stars. His many accolades include the Printz Medal, a Printz Honor, and the Edgar Award. John has twice been a finalist for the LA Times Book Prize and was selected by TIME magazine as one of the 100 Most Influential People in the World. With his brother, Hank, John is one half of the Vlogbrothers  and co-created the online educational series CrashCourse. You can join the millions who follow him on Twitter @johngreen and Instagram @johngreenwritesbooks or visit him online at johngreenbooks.com. John lives with his family in Indianapolis, Indiana.").__dict__
author_catalog.append(j_green)

r_chernow = CreateAuthor("Chernow", "Ron", "Ron Chernow’s bestselling books include The House of Morgan, winner of the National Book Award; The Warburgs, which won the George S. Eccles Prize; The Death of the Banker; Titan: The Life of John D. Rockefeller, nominated for the National Book Critics Circle Award; Washington: A Life, which received the Pulitzer Prize for Biography; and Alexander Hamilton, nominated for the National Book Critics Circle Award and adapted into the award-winning Broadway musical Hamilton. Chernow has served as president of PEN American Center, has received six honorary doctoral degrees, and was awarded the 2015 National Humanities Medal. He lives in Brooklyn, New York.").__dict__
author_catalog.append(ron_chernow)

s_kelly = CreateAuthor("Kelly", "Scott", "Scott Kelly is a former U.S. Navy fighter pilot, test pilot, and NASA astronaut. Kelly retired from the Navy at the rank of captain after twenty-five years of service. A veteran of four spaceflights, Kelly commanded the space shuttle Endeavour in 2007 and twice commanded the International Space Station. He has logged more than 520 days in space on four spaceflights and currently holds the records for total time in space and for single-mission endurance by a U.S. astronaut. Kelly spent 340 consecutive days in space, launching in March 2015 and returning home in March 2016. He currently resides in Houston, Texas.").__dict__
author_catalog.append(s_kelly)

t_coates = CreateAuthor("Coates", "Ta-Nehisi", "Ta-Nehisi Coates is a national correspondent for The Atlantic. His book Between the World and Me won the National Book Award in 2015. Coates is the recipient of a MacArthur Fellowship. He lives in New York City with his wife and son.").__dict__
author_catalog.append(t_coates)

m_twain = CreateAuthor("Twain", "Mark", "Mark Twain, considered one of the greatest writers in American literature, was born Samuel Clemens in Florida, Missouri, in 1835, and died in Redding, Connecticut in 1910. As a young child, he moved with his family to Hannibal, Missouri, on the banks of the Mississippi River, a setting that inspired his two best-known novels, The Adventures of Tom Sawyer and Adventures of Huckleberry Finn. In his person and in his pursuits, he was a man of extraordinary contrasts. Although he left school at 12 when his father died, he was eventually awarded honorary degrees from Yale University, the University of Missouri, and Oxford University. His career encompassed such varied occupations as printer, Mississippi riverboat pilot, journalist, travel writer, and publisher. He made fortunes from his writing but toward the end of his life he had to resort to lecture tours to pay his debts. He was hot-tempered, profane, and sentimental—and also pessimistic, cynical, and tortured by self-doubt. His nostalgia for the past helped produce some of his best books. He lives in American letters as a great artist, described by writer William Dean Howells as “the Lincoln of our literature.” Twain and his wife, Olivia Langdon Clemens, had four children—a son, Langdon, who died as an infant, and three daughters, Susy, Clara, and Jean.").__dict__
author_catalog.append(m_twain)

p_stead = CreateAuthor("Stead", "Philip C.", "Philip Stead is the author of the Caldecott Medal–winning book A Sick Day for Amos McGee. With his wife, illustrator Erin Stead, he also created Bear Has a Story to Tell, Lenny & Lucy, and The Purloining of Prince Oleomargarine, based on a previously-unpublished children’s story by Mark Twain. Philip has also written and illustrated his own books, including Hello, My Name Is Ruby; Jonathan and the Big Blue Boat; and A Home for Bird. Philip and Erin live in northern Michigan. Visit Philip online at philipstead.com.").__dict__
author_catalog.append(p_stead)

c_ng = CreateAuthor("Ng", "Celeste", "Celeste Ng grew up in Pittsburgh, Pennsylvania, and Shaker Heights, Ohio. She attended Harvard University and earned an MFA from the University of Michigan. She lives in Cambridge, Massachusetts, with her husband and son.").__dict__
author_catalog.append(c_ng)

k_knausgaard = CreateAuthor("Knausgaard", "Karl Ove", "Karl Ove Knausgaard’s first novel, Out of the World, was the first ever debut novel to win The Norwegian Critics’ Prize and his second, A Time to Every Purpose Under Heaven, was widely acclaimed. A Death in the Family, the first of the My Struggle cycle of novels, was awarded the prestigious Brage Award. The My Struggle cycle has been heralded as a masterpiece wherever it appears.").__dict__
author_catalog.append(k_knausgaard)

r_saujani = CreateAuthor("Saujani", "Reshma", "Reshma Saujani is the Founder and CEO of Girls Who Code, a national nonprofit organization working to close the gender gap in technology while teaching girls confidence and bravery through coding. She’s been named one of Fortune‘s 40 under 40, a WSJ magazine innovator of the year, one of the 50 most powerful women in New York by the New York Daily News,Forbes‘s Most Powerful Women Changing the World, Business Insider‘s 50 Women Who Are Changing the World, and an AOL/PBS MAKER. She is the author of Girls Who Code, a New York Times bestselling book for young readers.").__dict__
author_catalog.append(r_saujani)

i_mbue = CreateAuthor("Mbue", "Imbolo", "Imbolo Mbue is a native of the seaside town of Limbe, Cameroon. She holds a BS from Rutgers University and an MA from Columbia University. A resident of the United States for more than a decade, she lives in New York City.").__dict__
author_catalog.append(i_mbue)

a_rubin = CreateAuthor("Rubin", "Adam", "Adam Rubin is the New York Times best-selling author of a half dozen critically-acclaimed picture books including Robo-Sauce and Dragons Love Tacos. He spent ten years working as a creative director in the advertising industry before leaving his day job to write full time. Adam has a keen interest in improv comedy, camping and magic tricks. He lives in New York City.").__dict__
author_catalog.append(a_rubin)

d_salmieri = CreateAuthor("Salmieri", "Daniel").__dict__
author_catalog.append(d_salmieri)

j_didion = CreateAuthor("Didion", "Joan", "Joan Didion is the author of five novels and nine books of nonfiction. Her collected nonfiction, We Tell Ourselves Stories in Order to Live, was published by Everyman’s Library in 2006. Born in Sacramento, California, Didion now lives in New York City.").__dict__
author_catalog.append(j_didion)

a_brown = CreateAuthor("Brown", "Alton", "Alton Brown used to direct TV commercials and cook on the side. Then he got the crazy idea to go to culinary school and reinvent the food show. The result: Good Eats, which kept Brown gainfully employed for fifteen years and earned him a Peabody Award. Along the way he also hosted Iron Chef America and Feasting on Asphalt and wrote seven books in his spare time. In 2013 he launched a live culinary variety show called The Edible Inevitable tour, which played to sold out theaters across the United States. In the spring of 2016, Brown’s new live show, Eat Your Science, toured forty U.S. cities. Brown also hosts the insanely popular Cutthroat Kitchen on Food Network.").__dict__
author_catalog.append(a_brown)

l_bastianich = CreateAuthor("Bastianich", "Lidia Matticchio", "Lidia Matticchio Bastianich is the author of thirteen cookbooks and the Emmy award-winning host of public television’s Lidia’s Kitchen, which also airs internationally. She is also a judge on MasterChef Junior Italy and Italy’s highly rated daily program La Prova del Cuoco. Lidia owns Felidia, Becco, several other restaurants, and is a partner in the acclaimed Eataly. She lives on Long Island, New York.").__dict__
author_catalog.append(l_bastianich)

t_manuali = CreateAuthor("Manuali", "Tanya Bastianich").__dict__
author_catalog.append(t_manuali)

a_dewdney = CreateAuthor("Dewdney", "Anna", "Anna Dewdney was a teacher, mother, and enthusiastic proponent of reading aloud to children. She continually honed her skills as an artist and writer and published her first Llama Llama book in 2005. Her passion for creating extended to home and garden and she lovingly restored an eighteenth-century farmhouse in southern Vermont. She wrote, painted, gardened, and lived there with her partner, Reed, her two daughters, two wirehaired pointing griffons, and one bulldog. Anna passed away in 2016, but her spirit will live on in her books.").__dict__
author_catalog.append(a_dewdney)

r_duncan = CreateAuthor("Duncan", "Reed").__dict__
author_catalog.append(r_duncan)

m_atwood = CreateAuthor("Atwood", "Margaret", "Margaret Atwood, whose work has been published in thirty-five countries, is the author of more than forty books of fiction, poetry, and critical essays. In addition to The Handmaid’s Tale, her novels include Cat’s Eye, short-listed for the 1989 Booker Prize; Alias Grace, which won the Giller Prize in Canada and the Premio Mondello in Italy; The Blind Assassin, winner of the 2000 Booker Prize; Oryx and Crake, short-listed for the 2003 Man Booker Prize; The Year of the Flood; and MaddAddam. She is the recipient of the Los Angeles Times Innovator’s Award, and lives in Toronto with the writer Graeme Gibson.").__dict__
author_catalog.append(m_atwood)

d_eggers = CreateAuthor("Eggers", "Dave", "Dave Eggers grew up near Chicago and graduated from the University of Illinois at Urbana-Champaign. He is the founder of McSweeney’s, an independent publishing house in San Francisco that produces books, a quarterly journal of new writing (McSweeney’s Quarterly Concern), and a monthly magazine, The Believer. McSweeney’s publishes Voice of Witness, a nonprofit book series that uses oral history to illuminate human rights crises around the world. In 2002, he co-founded 826 Valencia, a nonprofit youth writing and tutoring center in San Francisco’s Mission District. Sister centers have since opened in seven other American cities under the umbrella of 826 National, and like-minded centers have opened in Dublin, London, Copenhagen, Stockholm, and Birmingham, Alabama, among other locations. Eggers’s work has been nominated for the National Book Award, the Pulitzer Prize, and the National Book Critics Circle Award, and has won the Dayton Literary Peace Prize, France’s Prix Médicis, Germany’s Albatross Prize, the National Magazine Award, and the American Book Award. Eggers lives in Northern California with his family. His novels include The Circle, A Hologram for the King, and Heroes of the Frontier.").__dict__
author_catalog.append(d_eggers)

# Create books

book = {
    "title": "",
    "cover": "",
    "description": "",
    "authors": [
        {
            "last_name": "",
            "first_name": ""
        }
    ],
    "genres": [
    "type": ""
    ]
}

book_catalog = []

class CreateBook:
    def __init__(self, title, cover, description):
        self.title = title
        self.cover = cover
        self.description = description
        self.authors = []
        self.genres = []

book = CreateBook(title, cover, description).__dict__
book['authors'].append({"last_name": author['last_name'], "first_name": author['first_name']})
book['genres'].append({"type": genre['type']})
book_catalog.append(book)


how_to_change_your_mind = CreateBook("How to Change Your Mind", "https://images.penguinrandomhouse.com/cover/9781594204227", "The #1 New York Times bestseller.<br/>A brilliant and brave investigation into the medical and scientific revolution taking place around psychedelic drugs–and the spellbinding story of his own life-changing psychedelic experiences").__dict__
how_to_change_your_mind['authors'].append({"last_name": m_pollan['last_name'], "first_name": m_pollan['first_name']})
how_to_change_your_mind['genres'].append({"type": g_philosophy['type']}, {"type": g_biography_memoir['type']})
book_catalog.append(how_to_change_your_mind)

the_female_persuasion = CreateBook("The Female Persuasion", "https://images.penguinrandomhouse.com/cover/9781594488405", "Greer Kadetsky is a shy college freshman when she meets the woman she hopes will change her life. Faith Frank, dazzlingly persuasive and elegant at sixty-three, has been a central pillar of the women’s movement for decades, a figure who inspires others to influence the world. Upon hearing Faith speak for the first time, Greer—madly in love with her boyfriend, Cory, but still full of longing for an ambition that she can’t quite place—feels her inner world light up. And then, astonishingly, Faith invites Greer to make something out of that sense of purpose, leading Greer down the most exciting path of her life as it winds toward and away from her meant-to-be love story with Cory and the future she’d always imagined.").__dict__
the_female_persuasion['authors'].append({"last_name": m_wollitzer['last_name'], "first_name": m_wollitzer['first_name']})
the_female_persuasion['genres'].append({"type": g_womens_fiction['type']}, {"type": g_literary_fiction['type']})
book_catalog.append(the_female_persuasion)

the_underground_railroad = CreateBook("The Underground Railroad", "https://images.penguinrandomhouse.com/cover/9780345804327", "Cora is a young slave on a cotton plantation in Georgia. An outcast even among her fellow Africans, she is on the cusp of womanhood—where greater pain awaits. And so when Caesar, a slave who has recently arrived from Virginia, urges her to join him on the Underground Railroad, she seizes the opportunity and escapes with him. In Colson Whitehead’s ingenious conception, the Underground Railroad is no mere metaphor: engineers and conductors operate a secret network of actual tracks and tunnels beneath the Southern soil. Cora embarks on a harrowing flight from one state to the next, encountering, like Gulliver, strange yet familiar iterations of her own world at each stop. As Whitehead brilliantly re-creates the terrors of the antebellum era, he weaves in the saga of our nation, from the brutal abduction of Africans to the unfulfilled promises of the present day. The Underground Railroad is both the gripping tale of one woman’s will to escape the horrors of bondage—and a powerful meditation on the history we all share.").__dict__
the_underground_railroad['authors'].append({"last_name": c_whitehead['last_name'], "first_name": c_whitehead['first_name']})
the_underground_railroad['genres'].append({"type": g_literary_fiction['type']}, {"type": g_historical_fiction['type']})
book_catalog.append(the_underground_railroad)

sag_harbor = CreateBook("Sag Harbor", "https://images.penguinrandomhouse.com/cover/9780307455161", "From the Pulitzer-Prize winning author of The Underground Railroad: a tender, hilarious, and supremely original novel about coming-of-age in the 80s.<br/>Benji Cooper is one of the few black students at an elite prep school in Manhattan. But every summer, Benji escapes to the Hamptons, to Sag Harbor, where a small community of African American professionals have built a world of their own.<br/>The summer of ’85 won’t be without its usual trials and tribulations, of course. There will be complicated new handshakes to fumble through and state-of-the-art profanity to master. Benji will be tested by contests big and small, by his misshapen haircut (which seems to have a will of its own), by the New Coke Tragedy, and by his secret Lite FM addiction. But maybe, just maybe, this summer might be one for the ages.").__dict__
sag_harbor['authors'].append({"last_name": c_whitehead['last_name'], "first_name": c_whitehead['first_name']})
sag_harbor['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(sag_harbor)

the_noble_hustle = CreateBook("The Noble Hustle", "https://images.penguinrandomhouse.com/cover/9780345804334", "From the #1 New York Times bestselling author of The Underground Railroad<br/>In 2011, Grantland magazine gave bestselling novelist Colson Whitehead $10,000 to play at the World Series of Poker in Las Vegas. It was the assignment of a lifetime, except for one hitch—he’d never played in a casino tournament before. With just six weeks to train, our humble narrator took the Greyhound to Atlantic City to learn the ways of high-stakes Texas Hold’em.<br/>Poker culture, he discovered, is marked by joy, heartbreak, and grizzled veterans playing against teenage hotshots weaned on Internet gambling. Not to mention the not-to-be overlooked issue of coordinating Port Authority bus schedules with your kid’s drop-off and pickup at school. Finally arriving in Vegas for the multimillion-dollar tournament, Whitehead brilliantly details his progress, both literal and existential, through the event’s antes and turns, through its gritty moments of calculation, hope, and spectacle. Entertaining, ironic, and strangely profound, this epic search for meaning at the World Series of Poker is a sure bet.").__dict__
the_noble_hustle['authors'].append({"last_name": c_whitehead['last_name'], "first_name": c_whitehead['first_name']})
the_noble_hustle['genres'].append({"type": g_biography_memoir['type']}, {"type": g_humor['type']})
book_catalog.append(the_noble_hustle)

apex_hides_the_hurt = CreateBook("Apex Hides the Hurt", "https://images.penguinrandomhouse.com/cover/9781400031269", "This New York Times Notable Book from the #1 New York Times bestselling author of The Underground Railroad is a brisk, comic tour de force about identity, history, and the adhesive bandage industry.<br/>The town of Winthrop has decided it needs a new name. The resident software millionaire wants to call it New Prospera; the mayor wants to return to the original choice of the founding black settlers; and the town’s aristocracy sees no reason to change the name at all. What they need, they realize, is a nomenclature consultant. And, it turns out, the consultant needs them. But in a culture overwhelmed by marketing, the name is everything and our hero’s efforts may result in not just a new name for the town but a new and subtler truth about it as well.").__dict__
apex_hides_the_hurt['authors'].append({"last_name": c_whitehead['last_name'], "first_name": c_whitehead['first_name']})
apex_hides_the_hurt['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(apex_hides_the_hurt)

you_cant_spell_america_without_me = CreateBook("You Can’t Spell America Without Me", "https://images.penguinrandomhouse.com/cover/9780525521990", "Political satire as deeper truth: Donald Trump’s presidential memoir, as recorded by two world-renowned Trump scholars, and experts on greatness generally").__dict__
you_cant_spell_america_without_me['authors'].append({"last_name": a_baldwin['last_name'], "first_name": a_baldwin['first_name']}, {"last_name": k_andersen['last_name'], "first_name": k_andersen['first_name']})
you_cant_spell_america_without_me['genres'].append({"type": g_humor['type']})
book_catalog.append(you_cant_spell_america_without_me)

dinner_in_an_instant = CreateBook("Dinner in an Instant", "https://images.penguinrandomhouse.com/cover/9781524762964", "Dinner in an Instant gives home cooks recipes for elevated dinners that never sacrifice convenience. Beloved for her flawless recipes, Melissa Clark turns her imagination to the countertop appliances that have won American hearts from coast to coast. Recipes include Fresh Coconut Yogurt, Japanese Beef Curry, Osso Buco, Smoky Lentils, Green Persian Rice with Tahdig, and Lemon Verbena Crème Brulee.<br/>Dinner in an Instant provides instructions when possible for making the same dish on both the pressure cooker and slow cooker settings, allowing home cooks flexibility. Symbols guide the reader toward Paleo, Vegan, Vegetarian, and Gluten Free dinners.").__dict__
dinner_in_an_instant['authors'].append({"last_name": m_clark['last_name'], "first_name": m_clark['first_name']})
dinner_in_an_instant['genres'].append({"type": g_cooking['type']})
book_catalog.append(dinner_in_an_instant)

turtles_all_the_way_down = CreateBook("Turtles All the Way Down", "https://images.penguinrandomhouse.com/cover/9780525555384", "It’s quite rare to find someone who sees the same world you see.<br/>Sixteen-year-old Aza never intended to pursue the mystery of fugitive billionaire Russell Pickett, but there’s a hundred-thousand-dollar reward at stake and her Best and Most Fearless Friend, Daisy, is eager to investigate. So together, they navigate the short distance and broad divides that separate them from Russell Pickett’s son, Davis.<br/>Aza is trying. She is trying to be a good daughter, a good friend, a good student, and maybe even a good detective, while also living within the ever-tightening spiral of her own thoughts.<br/>In his long-awaited return, John Green, the acclaimed, award-winning author of Looking for Alaska and The Fault in Our Stars, shares Aza’s story with shattering, unflinching clarity in this brilliant novel of love, resilience, and the power of lifelong friendship.").__dict__
turtles_all_the_way_down['authors'].append({"last_name": j_green['last_name'], "first_name": j_green['first_name']})
turtles_all_the_way_down['genres'].append({"type": g_teen_fiction['type']})
book_catalog.append(turtles_all_the_way_down)

grant = CreateBook("Grant", "https://images.penguinrandomhouse.com/cover/9781594204876", "Pulitzer Prize winner Ron Chernow returns with a sweeping and dramatic portrait of one of our most compelling generals and presidents, Ulysses S. Grant.<br/>Ulysses S. Grant’s life has typically been misunderstood. All too often he is caricatured as a chronic loser and an inept businessman, or as the triumphant but brutal Union general of the Civil War. But these stereotypes don’t come close to capturing him, as Chernow shows in his masterful biography, the first to provide a complete understanding of the general and president whose fortunes rose and fell with dizzying speed and frequency.").__dict__
grant['authors'].append({"last_name": ron_chernow['last_name'], "first_name": ron_chernow['first_name']})
grant['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(grant)

endurance = CreateBook("Endurance", "https://images.penguinrandomhouse.com/cover/9781524731595", "A stunning, personal memoir from the astronaut and modern-day hero who spent a record-breaking year aboard the International Space Station—a message of hope for the future that will inspire for generations to come.").__dict__
endurance['authors'].append({"last_name": s_kelly['last_name'], "first_name": s_kelly['first_name']})
endurance['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(endurance)

power = CreateBook("We Were Eight Years in Power", "https://images.penguinrandomhouse.com/cover/9780399590566", "“We were eight years in power” was the lament of Reconstruction-era black politicians as the American experiment in multiracial democracy ended with the return of white supremacist rule in the South. In this sweeping collection of new and selected essays, Ta-Nehisi Coates explores the tragic echoes of that history in our own time: the unprecedented election of a black president followed by a vicious backlash that fueled the election of the man Coates argues is America’s “first white president.”").__dict__
power['authors'].append({"last_name": t_coates['last_name'], "first_name": t_coates['first_name']})
power['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(power)

between_world = CreateBook("Between the World and Me", "https://images.penguinrandomhouse.com/cover/9780812993547", "In a profound work that pivots from the biggest questions about American history and ideals to the most intimate concerns of a father for his son, Ta-Nehisi Coates offers a powerful new framework for understanding our nation’s history and current crisis. Americans have built an empire on the idea of “race,” a falsehood that damages us all but falls most heavily on the bodies of black women and men—bodies exploited through slavery and segregation, and, today, threatened, locked up, and murdered out of all proportion. What is it like to inhabit a black body and find a way to live within it? And how can we all honestly reckon with this fraught history and free ourselves from its burden?").__dict__
between_world['authors'].append({"last_name": t_coates['last_name'], "first_name": t_coates['first_name']})
between_world['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(between_world)

the_purloining_of_prince_oleomargarine = CreateBook("The Purloining of Prince Oleomargarine", "https://images.penguinrandomhouse.com/cover/9780553523225", "A never-before-published, previously unfinished Mark Twain children’s story is brought to life by Philip and Erin Stead, creators of the Caldecott Medal-winning A Sick Day for Amos McGee.<br/>In a hotel in Paris one evening in 1879, Mark Twain sat with his young daughters, who begged their father for a story. Twain began telling them the tale of Johnny, a poor boy in possession of some magical seeds. Later, Twain would jot down some rough notes about the story, but the tale was left unfinished . . . until now.").__dict__
the_purloining_of_prince_oleomargarine['authors'].append({"last_name": m_twain['last_name'], "first_name": m_twain['first_name']}, {"last_name": p_stead['last_name'], "first_name": p_stead['first_name']})
the_purloining_of_prince_oleomargarine['genres'].append({"type": g_children_picture['type']})
book_catalog.append(the_purloining_of_prince_oleomargarine)

little_fires_everywhere = CreateBook("Little Fires Everywhere", "https://images.penguinrandomhouse.com/cover/9780735224292", "From the bestselling author of Everything I Never Told You, a riveting novel that traces the intertwined fates of the picture-perfect Richardson family and the enigmatic mother and daughter who upend their lives.<br/>In Shaker Heights, a placid, progressive suburb of Cleveland, everything is planned – from the layout of the winding roads, to the colors of the houses, to the successful lives its residents will go on to lead. And no one embodies this spirit more than Elena Richardson, whose guiding principle is playing by the rules.").__dict__
little_fires_everywhere['authors'].append({"last_name": c_ng['last_name'], "first_name": c_ng['first_name']})
little_fires_everywhere['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(little_fires_everywhere)

everything_i_never_told_you = CreateBook("Little Fires Everywhere", "https://images.penguinrandomhouse.com/cover/9780143127550", "“Lydia is dead. But they don’t know this yet.” So begins this exquisite novel about a Chinese American family living in 1970s small-town Ohio. Lydia is the favorite child of Marilyn and James Lee, and her parents are determined that she will fulfill the dreams they were unable to pursue. But when Lydia’s body is found in the local lake, the delicate balancing act that has been keeping the Lee family together is destroyed, tumbling them into chaos. A profoundly moving story of family, secrets, and longing, Everything I Never Told You is both a gripping page-turner and a sensitive family portrait, uncovering the ways in which mothers and daughters, fathers and sons, and husbands and wives struggle, all their lives, to understand one another.").__dict__
everything_i_never_told_you['authors'].append({"last_name": c_ng['last_name'], "first_name": c_ng['first_name']})
everything_i_never_told_you['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(everything_i_never_told_you)

autumn = CreateBook("Autumn", "https://images.penguinrandomhouse.com/cover/9780399563300", "From the author of the monumental My Struggle series, Karl Ove Knausgaard, one of the masters of contemporary literature and a genius of observation and introspection, comes the first in a new autobiographical quartet based on the four seasons.").__dict__
autumn['authors'].append({"last_name": k_knausgaard['last_name'], "first_name": k_knausgaard['first_name']})
autumn['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(autumn)

girls_who_code = CreateBook("Girls Who Code", "https://images.penguinrandomhouse.com/cover/9780425287552", "Part how-to, part girl-empowerment, and all fun, from the leader of the movement championed by Sheryl Sandberg, Malala Yousafzai, and John Legend.<br/>Since 2012, the organization Girls Who Code has taught computing skills to and inspired over 40,000 girls across America. Now its founder, Reshma Saujani, wants to inspire you to be a girl who codes! Bursting with dynamic artwork, down-to-earth explanations of coding principles, and real-life stories of girls and women working at places like Pixar and NASA, this graphically animated book shows what a huge role computer science plays in our lives and how much fun it can be. No matter your interest—sports, the arts, baking, student government, social justice—coding can help you do what you love and make your dreams come true. Whether you’re a girl who’s never coded before, a girl who codes, or a parent raising one, this entertaining book, printed in bold two-color and featuring art on every page, will have you itching to create your own apps, games, and robots to make the world a better place.").__dict__
girls_who_code['authors'].append({"last_name": r_saujani['last_name'], "first_name": r_saujani['first_name']})
girls_who_code['genres'].append({"type": g_children_picture['type']})
book_catalog.append(girls_who_code)

behold_the_dreamers = CreateBook("Behold the Dreamers", "https://images.penguinrandomhouse.com/cover/9780525509714", "Jende Jonga, a Cameroonian immigrant living in Harlem, has come to the United States to provide a better life for himself, his wife, Neni, and their six-year-old son. In the fall of 2007, Jende can hardly believe his luck when he lands a job as a chauffeur for Clark Edwards, a senior executive at Lehman Brothers. Clark demands punctuality, discretion, and loyalty—and Jende is eager to please. Clark’s wife, Cindy, even offers Neni temporary work at the Edwardses’ summer home in the Hamptons. With these opportunities, Jende and Neni can at last gain a foothold in America and imagine a brighter future.").__dict__
behold_the_dreamers['authors'].append({"last_name": i_mbue['last_name'], "first_name": i_mbue['first_name']})
behold_the_dreamers['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(behold_the_dreamers)

dragons_love_tacos = CreateBook("Dragons Love Tacos", cover, "A #1 New York Times bestselling phenomenon, this deliciously funny read-aloud from the creators of Robo-Sauce and Secret Pizza Party will make you laugh until spicy salsa comes out of your nose.<br/>Dragons love tacos. They love chicken tacos, beef tacos, great big tacos, and teeny tiny tacos. So if you want to lure a bunch of dragons to your party, you should definitely serve tacos. Buckets and buckets of tacos. Unfortunately, where there are tacos, there is also salsa. And if a dragon accidentally eats spicy salsa . . . oh, boy. You’re in red-hot trouble.").__dict__
dragons_love_tacos['authors'].append({"last_name": a_rubin['last_name'], "first_name": a_rubin['first_name']}, {"last_name": d_salmieri['last_name'], "first_name": d_salmieri['first_name']})
dragons_love_tacos['genres'].append({"type": g_children_picture['type']})
book_catalog.append(dragons_love_tacos)

dragons_love_tacos_2 = CreateBook("Dragons Love Tacos 2: The Sequel", "https://images.penguinrandomhouse.com/cover/9780525428886", "The hilarious sequel to the smokin’ hot New York Times best seller, perfect for story time<br/>News alert! It has just been discovered that there are NO MORE TACOS left anywhere in the world. This is a huge problem because, as you know, dragons love tacos. If only there was a way for the dragons to travel back in time, to before tacos went extinct. Then they could grab lots of tacos and bring them back! It’s the perfect plan, as long as there’s no spicy salsa. You remember what happened last time . . .<br/>The award-winning creators of Robo-Sauce and Secret Pizza Party return with a gut-bustingly hilarious companion to the bestselling phenomenon Dragons Love Tacos.").__dict__
dragons_love_tacos_2['authors'].append({"last_name": a_rubin['last_name'], "first_name": a_rubin['first_name']}, {"last_name": d_salmieri['last_name'], "first_name": d_salmieri['first_name']})
dragons_love_tacos_2['genres'].append({"type": g_children_picture['type']})
book_catalog.append(dragons_love_tacos_2)

robo-sauce = CreateBook("Robo-Sauce", "https://images.penguinrandomhouse.com/cover/9780525428879", "Fans of the best-selling Dragons Love Tacos will devour Adam Rubin and Daniel Salmieri’s newest story, a hilarious picture book about robots that magically transforms into a super shiny metal ROBO-BOOK.<br/>FACT: Robots are awesome. They have lasers for eyes, rockets for feet, and supercomputers for brains! Plus, robots never have to eat steamed beans or take baths, or go to bed. If only there were some sort of magical “Robo-Sauce” that turned squishy little humans into giant awesome robots… Well, now there is.").__dict__
robo-sauce['authors'].append({"last_name": a_rubin['last_name'], "first_name": a_rubin['first_name']}, {"last_name": d_salmieri['last_name'], "first_name": d_salmieri['first_name']})
robo-sauce['genres'].append({"type": g_children_picture['type']})
book_catalog.append(robo-sauce)

south_and_west = CreateBook("South and West", "https://images.penguinrandomhouse.com/cover/9780525434191", "Joan Didion has always kept notebooks—of overheard dialogue, interviews, drafts of essays, copies of articles. South and West gives us two extended excerpts from notebooks she kept in the 1970s; read together, they form a piercing view of the American political and cultural landscape.<br/>“Notes on the South” traces a road trip that she and her husband, John Gregory Dunne, took through Louisiana, Mississippi, and Alabama. Her acute observations about the small towns they pass through, her interviews with local figures, and their preoccupation with race, class, and heritage suggest a South largely unchanged today. “California Notes” began as an assignment from Rolling Stone on the Patty Hearst trial. Though Didion never wrote the piece, the time she spent watching the trial in San Francisco triggered thoughts about the West and her own upbringing in Sacramento. Here we not only see Didion’s signature irony and imagination in play, we’re also granted an illuminating glimpse into her mind and process.").__dict__
south_and_west['authors'].append({"last_name": j_didion['last_name'], "first_name": j_didion['first_name']})
south_and_west['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(south_and_west)

democracy = CreateBook("Democracy", "https://images.penguinrandomhouse.com/cover/9780679754855", "Inez Victor knows that the major casualty of the political life is memory. But the people around Inez have made careers out of losing track. Her senator husband wants to forget the failure of his last bid for the presidency. Her husband’s handler would like the press to forget that Inez’s father is a murderer. And, in 1975, the year in which much of this bitterly funny novel is set, America is doing its best to lose track of its one-time client, the lethally hemorrhaging republic of South Vietnam.As conceived by Joan Didion, these personages and events constitute the terminal fallout of democracy, a fallout that also includes fact-finding junkets, senatorial groupies, the international arms market, and the Orwellian newspeak of the political class. Moving deftly from Honolulu to Jakarta, between romance, farce, and tragedy, Democracy is a tour de force from a writer who can dissect an entire society with a single phrase.").__dict__
democracy['authors'].append({"last_name": j_didion['last_name'], "first_name": j_didion['first_name']})
democracy['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(democracy)

where_i_was_from = CreateBook("Where I Was From", "https://images.penguinrandomhouse.com/cover/9780679752868", "In her moving and insightful new book, Joan Didion reassesses parts of her life, her work, her history and ours. A native Californian, Didion applies her scalpel-like intelligence to the state’s ethic of ruthless self-sufficiency in order to examine that ethic’s often tenuous relationship to reality.<br/>Combining history and reportage, memoir and literary criticism, Where I Was From explores California’s romances with land and water; its unacknowledged debts to railroads, aerospace, and big government; the disjunction between its code of individualism and its fetish for prisons. Whether she is writing about her pioneer ancestors or privileged sexual predators, robber barons or writers (not excluding herself), Didion is an unparalleled observer, and her book is at once intellectually provocative and deeply personal.").__dict__
where_i_was_from['authors'].append({"last_name": j_didion['last_name'], "first_name": j_didion['first_name']})
where_i_was_from['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(where_i_was_from)

alton_brown_everydaycook = CreateBook("Alton Brown: EveryDayCook", "https://images.penguinrandomhouse.com/cover/9781101885710", "My name is Alton Brown, and I wrote this book. It’s my first in a few years because I’ve been a little busy with TV stuff and interwebs stuff and live stage show stuff. Sure, I’ve been cooking, but it’s been mostly to feed myself and people in my immediate vicinity—which is really what a cook is supposed to do, right? Well, one day I was sitting around trying to organize my recipes, and I realized that I should put them into a personal collection. One thing led to another, and here’s EveryDayCook. There’s still plenty of science and hopefully some humor in here (my agent says that’s my “wheelhouse”), but unlike in my other books, a lot of attention went into the photos, which were all taken on my iPhone (take that, Instagram) and are suitable for framing. As for the recipes, which are arranged by time of day, they’re pretty darned tasty.").__dict__
alton_brown_everydaycook['authors'].append({"last_name": a_brown['last_name'], "first_name": a_brown['first_name']})
alton_brown_everydaycook['genres'].append({"type": g_cooking['type']})
book_catalog.append(alton_brown_everydaycook)


lidias_mastering_the_art_of_italian_cuisine = CreateBook("Lidia’s Mastering the Art of Italian Cuisine", "https://images.penguinrandomhouse.com/cover/9780385349468", "From the Emmy-winning host of Lidia’s Kitchen, best-selling author, and beloved ambassador for Italian culinary traditions in America comes the ultimate master class: a beautifully produced definitive guide to Italian cooking, coauthored with her daughter, Tanya—covering everything from ingredients to techniques to tools, plus more than 400 delectable recipes.<br/>Teaching has always been Lidia’s passion, and in this magnificent book she gives us the full benefit of that passion and of her deep, comprehensive understanding of what it takes to create delicious Italian meals. With this book, readers will learn all the techniques needed to master Italian cooking. Lidia introduces us to the full range of standard ingredients—meats and fish, vegetables and fruits, grains, spices and condiments—and how to buy, store, clean, and cook with them. The 400 recipes run the full gamut from classics like risotto alla milanese and Tagliatelle with Mushroom Sauce to Lidia’s always-satisfying originals like Bread and Prune Gnocchi and Beet Ravioli in Poppy Seed Sauce. She gives us a comprehensive guide to the tools every kitchen should have to produce the best results. And she has even included a glossary of cuisine-related words and phrases that will prove indispensable for cooking, as well as for traveling and dining in Italy. There is no other book like this; it is the one book on Italian cuisine that every cook will need.").__dict__
lidias_mastering_the_art_of_italian_cuisine['authors'].append({"last_name": l_bastianich['last_name'], "first_name": l_bastianich['first_name']}, {"last_name": t_manuali['last_name'], "first_name": t_manuali['first_name']})
lidias_mastering_the_art_of_italian_cuisine['genres'].append({"type": g_cooking['type']})
book_catalog.append(lidias_mastering_the_art_of_italian_cuisine)

lidias_italy_in_america = CreateBook("Lidia’s Italy in America", "https://images.penguinrandomhouse.com/cover/9780385349468", "From one of America’s most beloved chefs and authors, a road trip into the heart of Italian American cooking today—from Chicago deep-dish pizza to the Bronx’s eggplant parm—celebrating the communities that redefined what we know as Italian food.<br/>As she explores this utterly delectable and distinctive cuisine, Lidia shows us that every kitchen is different, every Italian community distinct, and little clues are buried in each dish: the Sicilian-style semolina bread and briny olives in New Orleans Muffuletta Sandwiches, the Neapolitan crust of New York pizza, and mushrooms (abundant in the United States, but scarce in Italy) stuffed with breadcrumbs, just as peppers or tomatoes are. Lidia shows us how this cuisine is an original American creation and gives recognition where it is long overdue to the many industrious Italians across the country who have honored the traditions of their homeland in a delicious new style.").__dict__
lidias_italy_in_america['authors'].append({"last_name": l_bastianich['last_name'], "first_name": l_bastianich['first_name']}, {"last_name": t_manuali['last_name'], "first_name": t_manuali['first_name']})
lidias_italy_in_america['genres'].append({"type": g_cooking['type']})
book_catalog.append(lidias_italy_in_america)

lidias_family_table = CreateBook("Lidia’s Family Table", "https://images.penguinrandomhouse.com/cover/9781400040353", "From one of America best-loved and most-admired chefs, an instructive and creative collection of over 200 recipes that bring simple, delicious Italian cooking to the family table, with imaginative ideas for variations and improvisations.<br/>Lidia’s Family Table features hundreds of fabulous new dishes that will appeal both to Lidia’s loyal following, who have come to rely on her wonderfully detailed recipes, and to the more adventurous cook ready to experiment.").__dict__
lidias_family_table['authors'].append({"last_name": l_bastianich['last_name'], "first_name": l_bastianich['first_name']})
lidias_family_table['genres'].append({"type": g_cooking['type']})
book_catalog.append(lidias_family_table)

llama_llama_i_love_you = CreateBook("Llama Llama I Love You", "https://images.penguinrandomhouse.com/cover/9780698156517", "Nothing could be sweeter than Valentine’s Day with Llama Llama! Llama Llama shows his friends and family how much he loves them with heart-shaped cards and lots of hugs.").__dict__
llama_llama_i_love_you['authors'].append({"last_name": a_dewdney['last_name'], "first_name": a_dewdney['first_name']})
llama_llama_i_love_you['genres'].append({"type": g_children_picture['type']})
book_catalog.append(llama_llama_i_love_you)

llama_llama_loves_to_read = CreateBook("Llama Llama Loves to Read", "https://images.penguinrandomhouse.com/cover/9780670013975", "Anna Dewdney’s Bestselling Llama Llama series continues with Llama learning to read!<br/>Anna Dewdney’s beloved Llama Llama is growing up and learning to read! Throughout the school day, the teacher helps Llama Llama and the other children practice their letters, shows word cards, reads stories, and brings them to the library where they can all choose a favorite book. By the end of the day, Llama Llama is recognizing words and can’t wait to show Mama Llama that he’s becoming a reader!").__dict__
llama_llama_loves_to_read['authors'].append({"last_name": a_dewdney['last_name'], "first_name": a_dewdney['first_name']}, {"last_name": r_duncan['last_name'], "first_name": r_duncan['first_name']})
llama_llama_loves_to_read['genres'].append({"type": g_children_picture['type']})
book_catalog.append(llama_llama_loves_to_read)

hag-seed = CreateBook("Hag-Seed", "https://images.penguinrandomhouse.com/cover/9780804141314", "William Shakespeare’s The Tempest retold as Hag-Seed<br/>Felix is at the top of his game as Artistic Director of the Makeshiweg Theatre Festival. His productions have amazed and confounded. Now he’s staging a Tempest like no other: not only will it boost his reputation, it will heal emotional wounds.<br/>Or that was the plan. Instead, after an act of unforeseen treachery, Felix is living in exile in a backwoods hovel, haunted by memories of his beloved lost daughter, Miranda. And also brewing revenge.<br/>After twelve years, revenge finally arrives in the shape of a theatre course at a nearby prison. Here, Felix and his inmate actors will put on his Tempest and snare the traitors who destroyed him. It’s magic! But will it remake Felix as his enemies fall?").__dict__
hag-seed['authors'].append({"last_name": m_atwood['last_name'], "first_name": m_atwood['first_name']})
hag-seed['genres'].append({"type": g_literary_fiction['type']}, {"type": g_womens_fiction['type']})
book_catalog.append(hag-seed)

the_tent = CreateBook("The Tent", "https://images.penguinrandomhouse.com/cover/9781400097012", "A delightful mélange of short fiction, here the Booker Prize-winning author pushes against form once again, with meditations on warlords, pet heaven, and aging homemakers. In these pieces, Margaret Atwood gives a sly pep talk to the ambitious young; writes about the disconcerting experience of looking at old photos of ourselves; and examines the boons and banes of orphanhood. Accompanied by her own playful illustrations, Atwood’s droll humor and keen insight make each piece full of clarity and grace. Prescient and personal, delectable and tart, The Tent reflects one of our wittiest authors at her best.").__dict__
the_tent['authors'].append({"last_name": m_atwood['last_name'], "first_name": m_atwood['first_name']})
the_tent['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_tent)

moral_disorder = CreateBook("Moral Disorder", "https://images.penguinrandomhouse.com/cover/9780385721646", "A brilliant collection of connected short stories following the life of a single woman, from the #1 New York Times bestselling author of The Handmaid’s Tale.<br/>In these eleven tales, Margaret Atwood brings to life the story of one remarkable character, following her from girlhood in the 1930s, through her coming-of-age in the 50s and 60s, and into the present day where, no longer young, she reflects on the new state of the world. Each story focuses on the ways relationships transform a life: a woman’s complex love for a married man, the grief upon the death of parents and the joy with the birth of children, and the realization of what growing old with someone you love really means. By turns funny, lyrical, incisive, earthy, shocking, and deeply personal, Moral Disorder displays Atwood’s celebrated storytelling gifts and unmistakable style to their best advantage.").__dict__
moral_disorder['authors'].append({"last_name": m_atwood['last_name'], "first_name": m_atwood['first_name']})
moral_disorder['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(moral_disorder)

good_bones_and_simple_murders = CreateBook("Good Bones and Simple Murders", "https://images.penguinrandomhouse.com/cover/9780307798534", "In this collection of short works that defy easy  categorization, Margaret Atwood displays, in  condensed and crystallized form, the trademark wit and  viruosity of her best-selling novels, brilliant  stories, and insightful poetry. Among the jewels  gathered here are Gertrude offering Hamlet a piece  of her mind, the real truth about the Little Red  Hen, a reincarnated bat explaining how Bram Stoker  got Dracula all wrong, and the  five methods of making a man (such as the  \"Traditional Method\": \"Take some dust off  the ground. Form. Breathe into the nostrils the  breath of life. Simple, but effective!\")  There are parables, monologues, prose poems, condensed  science fiction, reconfigured fairy tales, and  other miniature masterpieces–punctuated with  charming illustrations by the author. A must for her  fans, and a wonderful gift for all who savor the art  of exquisite prose, Good Bones And Simple  Murders marks the first time these  writings have been available in a trade edition in the  United States.").__dict__
good_bones_and_simple_murders['authors'].append({"last_name": m_atwood['last_name'], "first_name": m_atwood['first_name']})
good_bones_and_simple_murders['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(good_bones_and_simple_murders)

heroes_of_the_frontier = CreateBook("Heroes of the Frontier", "https://images.penguinrandomhouse.com/cover/9781101974636", "Josie and her children’s father have split up, she’s been sued by a former patient and lost her dental practice, and she’s grieving the death of a young man senselessly killed shortly after enlisting. When her ex asks to take the children to meet his new fiancée’s family, Josie makes a run for it to Alaska with her kids, Paul and Ana. At first their trip feels like a vacation: they see bears and bison, they eat hot dogs cooked on a bonfire, and they spend nights parked along icy cold rivers in dark forests. But as they drive in their rattling old RV, pushed north by the ubiquitous wildfires, Josie is chased by enemies both real and imagined, and past mistakes pursue her tiny family, even to the very edge of civilization. A captivating, often hilarious novel of family, loss, wilderness, and the curse of a violent America, Heroes of the Frontier is a powerful examination of our contemporary life and a rousing story of adventure.").__dict__
heroes_of_the_frontier['authors'].append({"last_name": d_eggers['last_name'], "first_name": d_eggers['first_name']})
heroes_of_the_frontier['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(heroes_of_the_frontier)

the_circle = CreateBook("The Circle", "https://images.penguinrandomhouse.com/cover/9780345807298", "Now a Major Motion Picture starring Emma Watson and Tom Hanks. A bestselling dystopian novel that tackles surveillance, privacy and the frightening intrusions of technology in our lives.<br/>When Mae Holland is hired to work for the Circle, the world’s most powerful internet company, she feels she’s been given the opportunity of a lifetime. The Circle, run out of a sprawling California campus, links users’ personal emails, social media, banking, and purchasing with their universal operating system, resulting in one online identity and a new age of civility and transparency. As Mae tours the open-plan office spaces, the towering glass dining facilities, the cozy dorms for those who spend nights at work, she is thrilled with the company’s modernity and activity. There are parties that last through the night, there are famous musicians playing on the lawn, there are athletic activities and clubs and brunches, and even an aquarium of rare fish retrieved from the Marianas Trench by the CEO. Mae can’t believe her luck, her great fortune to work for the most influential company in the world—even as life beyond the campus grows distant, even as a strange encounter with a colleague leaves her shaken, even as her role at the Circle becomes increasingly public. What begins as the captivating story of one woman’s ambition and idealism soon becomes a heart-racing novel of suspense, raising questions about memory, history, privacy, democracy, and the limits of human knowledge.").__dict__
the_circle['authors'].append({"last_name": d_eggers['last_name'], "first_name": d_eggers['first_name']})
the_circle['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_circle)

https://www.penguinrandomhouse.com/books/206755/chomp-by-carl-hiaasen/
https://www.penguinrandomhouse.com/books/227601/fox-in-socks-by-dr-seuss/
https://www.penguinrandomhouse.com/books/309505/marcel-the-shell-with-shoes-on-by-jenny-slate/
https://www.penguinrandomhouse.com/books/310267/stuck-by-oliver-jeffers-illustrated-by-oliver-jeffers/
https://www.penguinrandomhouse.com/books/214488/i-want-my-hat-back-by-jon-klassen/

https://www.penguinrandomhouse.com/books/6130/the-year-of-the-flood-by-margaret-atwood/

https://www.penguinrandomhouse.com/books/530131/you-cant-touch-my-hair-by-phoebe-robinson-foreword-by-jessica-williams/
https://www.penguinrandomhouse.com/books/317946/how-to-ruin-everything-by-george-watsky/
https://www.penguinrandomhouse.com/books/220620/based-on-a-true-story-by-norm-macdonald/
https://www.penguinrandomhouse.com/books/214489/attempting-normal-by-marc-maron/

https://www.penguinrandomhouse.com/books/228333/armada-by-ernest-cline/
https://www.penguinrandomhouse.com/books/33501/jurassic-park-by-michael-crichton/
https://www.penguinrandomhouse.com/books/6122/the-blind-assassin-by-margaret-atwood/

https://www.penguinrandomhouse.com/authors/29883/martha-stewart
https://www.penguinrandomhouse.com/authors/1261/james-baldwin


def add_book(book):
    new_book = Book(title=book['title'], cover=book['cover'], description=book['description'])
    session.add(new_book)
    session.commit()

    for genre in book['genres']:
        try:
            genre_search = session.query(Genre).filter_by(type=genre).one()
        else:
            new_genre = Genre(type=genre)
            session.add(new_genre)
            session.commit()
            genre_search = session.query(Genre).filter_by(type=genre).one()
        new_book.genres.append(genre_search)

    for author in book['authors']:
        try:
            author_search = session.query(Author).filter_by(last_name=author['last_name'], first_name=author['first_name']).one()
        else:
            new_author = Author(last_name=author['last_name'], first_name=author['first_name'])
            session.add(new_author)
            session.commit()
            author_search = session.query(Author).filter_by(last_name=author['last_name'], first_name=author['first_name']).one()
        new_book.authors.add(author_search)

for book in book_catalog:
    add_book(book)

print "Added books and authors and genres, woot woot!"