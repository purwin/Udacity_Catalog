#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

import random

reload(sys)
sys.setdefaultencoding('utf-8')

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Data pulled from the Penguin Random House: www.penguinrandomhouse.com

# Create genres

genre_catalog = []


class CreateGenre:
    def __init__(self, type):
        self.type = type


g_philosophy = CreateGenre("Philosophy").__dict__
genre_catalog.append(g_philosophy)

g_biography_memoir = CreateGenre("Biography & Memoir").__dict__
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

g_teen_fiction = CreateGenre("Teen & Young Adult Fiction").__dict__
genre_catalog.append(g_teen_fiction)

g_children_picture = CreateGenre("Children’s Picture Books").__dict__
genre_catalog.append(g_children_picture)

g_science_fiction = CreateGenre("Science Fiction").__dict__
genre_catalog.append(g_science_fiction)

# Create authors


author_catalog = []


class CreateAuthor:
    def __init__(self, last_name, first_name, bio=None):
        self.last_name = last_name
        self.first_name = first_name
        self.bio = bio


c_hiaasen = CreateAuthor("Hiaasen", "Carl", "CARL HIAASEN was born and raised \
                         in Florida. He is the author of thirteen previous \
                         novels, including the best sellers Razor Girl, Bad \
                         Monkey, Star Island, Nature Girl, Skinny Dip, Sick \
                         Puppy, and Lucky You, and five best-selling \
                         children’s books, Hoot, Flush, Scat, Chomp, and \
                         Skink. His most recent work of nonfiction is Dance \
                         of the Reptiles, a collection of his columns from \
                         The Miami Herald. www.carlhiaasen.com. CARL HIAASEN \
                         is available for select readings and \
                         lectures.").__dict__
author_catalog.append(c_hiaasen)

r_chast = CreateAuthor("Chast", "Roz").__dict__
author_catalog.append(r_chast)

m_pollan = CreateAuthor("Pollan", "Michael", "Michael Pollan, recently \
                        featured on Netflix in the four-part series \
                        <i>Cooked</i>, is the author of seven previous books, \
                        including <i>Food Rules</i>, <i>In Defense of \
                        Food</i>, <i>The Omnivore’s Dilemma</i>, and <i>The \
                        Botany of Desire</i>, all <i>New York Times</i> \
                        bestsellers. A longtime contributor to the <i>New \
                        York Times</i> Magazine, he is also the John S. and \
                        James L. Knight Professor of Journalism at Berkeley. \
                        In 2010, Time magazine named him one of the one \
                        hundred most influential people in the \
                        world.").__dict__
author_catalog.append(m_pollan)

m_wollitzer = CreateAuthor("Wolitzer", "Meg", "Meg Wolitzer is the New York \
                           Times–bestselling author of <i>The \
                           Interestings</i>, <i>The Uncoupling</i>, <i>The \
                           Ten-Year Nap</i>, <i>The Position</i>, <i>The \
                           Wife</i>, and <i>Sleepwalking</i>. She is also the \
                           author of the young adult novel <i>Belzhar</i>. \
                           Wolitzer lives in New York City.").__dict__
author_catalog.append(m_wollitzer)

c_whitehead = CreateAuthor("Whitehead", "Colson", "Colson Whitehead is the #1 \
                           New York Times bestselling author of <i>The \
                           Underground Railroad</i>, which in 2016 won the \
                           Pulitzer Prize in Fiction and the National Book \
                           Award and was named one of the Ten Best Books of \
                           the Year by <i>The New York Times</i> Book Review, \
                           as well as <i>The Noble Hustle</i>, <i>Zone One\
                           </i>, <i>Sag Harbor</i>, <i>The Intuitionist</i>, \
                           <i>John Henry Days</i>, <i>Apex Hides the Hurt\
                           </i>, and <i>The Colossus of New York</i>. He is \
                           also a Pulitzer Prize finalist and a recipient of \
                           the MacArthur and Guggenheim Fellowships. He lives \
                           in New York City.").__dict__
author_catalog.append(c_whitehead)

a_baldwin = CreateAuthor("Baldwin", "Alec", "Alec Baldwin is a multiple Emmy, \
                         Golden Globe, and Screen Actors Guild Award-winning \
                         actor, producer, comedian, and philanthropist. He \
                         has also been nominated for an Oscar and a Tony \
                         Award and the author of the New York Times \
                         bestseller <i>A Promise to Ourselves</i>.").__dict__
author_catalog.append(a_baldwin)

k_andersen = CreateAuthor("Andersen", "Kurt", "Kurt Andersen is author of <i>\
                          Heyday</i> and <i>Turn of the Century</i> and \
                          frequently writes for <i>New York</i> and <i>Vanity \
                          Fair</i>. He is host and cocreator of the Peabody \
                          Award–winning public radio program Studio 360. In \
                          2006, he founded Very Short List, an email service \
                          for connoisseurs of culture who would never call \
                          themselves “connoisseurs.” He was cofounder of Spy \
                          magazine, and has been a columnist and critic for \
                          the <i>New Yorker</i> and <i>Time</i>. Andersen \
                          lives with his wife and daughters in \
                          Brooklyn.").__dict__
author_catalog.append(k_andersen)

m_clark = CreateAuthor("Clark", "Melissa", "Melissa Clark is a staff writer \
                       for the <i>New York Times</i> where she writes the \
                       popular column “A Good Appetite,” and stars in a \
                       weekly complementary video series. The winner of James \
                       Beard and IACP Awards, she is a regular on <i>Today\
                       </i> and NPR (<i>The Splendid Table</i>, <i>The \
                       Leonard Lopate Show</i>). Melissa earned an MFA in \
                       writing from Columbia.").__dict__
author_catalog.append(m_clark)

j_green = CreateAuthor("Green", "John", "John Green is the award-winning, #1 \
                       bestselling author of Looking for Alaska, An Abundance \
                       of Katherines, Paper Towns, Will Grayson, Will Grayson \
                       (with David Levithan), and The Fault in Our Stars. His \
                       many accolades include the Printz Medal, a Printz \
                       Honor, and the Edgar Award. John has twice been a \
                       finalist for the LA Times Book Prize and was selected \
                       by TIME magazine as one of the 100 Most Influential \
                       People in the World. With his brother, Hank, John is \
                       one half of the Vlogbrothers  and co-created the \
                       online educational series CrashCourse. You can join \
                       the millions who follow him on Twitter @johngreen and \
                       Instagram @johngreenwritesbooks or visit him online at \
                       johngreenbooks.com. John lives with his family in \
                       Indianapolis, Indiana.").__dict__
author_catalog.append(j_green)

r_chernow = CreateAuthor("Chernow", "Ron", "Ron Chernow’s bestselling books \
                         include The House of Morgan, winner of the National \
                         Book Award; The Warburgs, which won the George S. \
                         Eccles Prize; The Death of the Banker; Titan: The \
                         Life of John D. Rockefeller, nominated for the \
                         National Book Critics Circle Award; Washington: A \
                         Life, which received the Pulitzer Prize for Biography\
                         ; and Alexander Hamilton, nominated for the National \
                         Book Critics Circle Award and adapted into the award-\
                         winning Broadway musical Hamilton. Chernow has \
                         served as president of PEN American Center, has \
                         received six honorary doctoral degrees, and was \
                         awarded the 2015 National Humanities Medal. He lives \
                         in Brooklyn, New York.").__dict__
author_catalog.append(r_chernow)

s_kelly = CreateAuthor("Kelly", "Scott", "Scott Kelly is a former U.S. Navy \
                       fighter pilot, test pilot, and NASA astronaut. Kelly \
                       retired from the Navy at the rank of captain after \
                       twenty-five years of service. A veteran of four \
                       spaceflights, Kelly commanded the space shuttle \
                       Endeavour in 2007 and twice commanded the \
                       International Space Station. He has logged more than \
                       520 days in space on four spaceflights and currently \
                       holds the records for total time in space and for \
                       single-mission endurance by a U.S. astronaut. Kelly \
                       spent 340 consecutive days in space, launching in \
                       March 2015 and returning home in March 2016. He \
                       currently resides in Houston, Texas.").__dict__
author_catalog.append(s_kelly)

t_coates = CreateAuthor("Coates", "Ta-Nehisi", "Ta-Nehisi Coates is a \
                        national correspondent for The Atlantic. His book \
                        Between the World and Me won the National Book Award \
                        in 2015. Coates is the recipient of a MacArthur \
                        Fellowship. He lives in New York City with his wife \
                        and son.").__dict__
author_catalog.append(t_coates)

m_twain = CreateAuthor("Twain", "Mark", "Mark Twain, considered one of the \
                       greatest writers in American literature, was born \
                       Samuel Clemens in Florida, Missouri, in 1835, and died \
                       in Redding, Connecticut in 1910. As a young child, he \
                       moved with his family to Hannibal, Missouri, on the \
                       banks of the Mississippi River, a setting that \
                       inspired his two best-known novels, The Adventures of \
                       Tom Sawyer and Adventures of Huckleberry Finn. In his \
                       person and in his pursuits, he was a man of \
                       extraordinary contrasts. Although he left school at 12 \
                       when his father died, he was eventually awarded \
                       honorary degrees from Yale University, the University \
                       of Missouri, and Oxford University. His career \
                       encompassed such varied occupations as printer, \
                       Mississippi riverboat pilot, journalist, travel \
                       writer, and publisher. He made fortunes from his \
                       writing but toward the end of his life he had to \
                       resort to lecture tours to pay his debts. He was hot-\
                       tempered, profane, and sentimental—and also \
                       pessimistic, cynical, and tortured by self-doubt. His \
                       nostalgia for the past helped produce some of his best \
                       books. He lives in American letters as a great artist, \
                       described by writer William Dean Howells as “the \
                       Lincoln of our literature.” Twain and his wife, Olivia \
                       Langdon Clemens, had four children—a son, Langdon, who \
                       died as an infant, and three daughters, Susy, Clara, \
                       and Jean.").__dict__
author_catalog.append(m_twain)

p_stead = CreateAuthor("Stead", "Philip C.", "Philip Stead is the author of \
                       the Caldecott Medal–winning book A Sick Day for Amos \
                       McGee. With his wife, illustrator Erin Stead, he also \
                       created Bear Has a Story to Tell, Lenny & Lucy, and \
                       The Purloining of Prince Oleomargarine, based on a \
                       previously-unpublished children’s story by Mark Twain. \
                       Philip has also written and illustrated his own books, \
                       including Hello, My Name Is Ruby; Jonathan and the Big \
                       Blue Boat; and A Home for Bird. Philip and Erin live \
                       in northern Michigan. Visit Philip online at \
                       philipstead.com.").__dict__
author_catalog.append(p_stead)

c_ng = CreateAuthor("Ng", "Celeste", "Celeste Ng grew up in Pittsburgh, \
                    Pennsylvania, and Shaker Heights, Ohio. She attended \
                    Harvard University and earned an MFA from the University \
                    of Michigan. She lives in Cambridge, Massachusetts, with \
                    her husband and son.").__dict__
author_catalog.append(c_ng)

k_knausgaard = CreateAuthor("Knausgaard", "Karl Ove", "Karl Ove Knausgaard’s \
                            first novel, Out of the World, was the first ever \
                            debut novel to win The Norwegian Critics’ Prize \
                            and his second, A Time to Every Purpose Under \
                            Heaven, was widely acclaimed. A Death in the \
                            Family, the first of the My Struggle cycle of \
                            novels, was awarded the prestigious Brage Award. \
                            The My Struggle cycle has been heralded as a \
                            masterpiece wherever it appears.").__dict__
author_catalog.append(k_knausgaard)

r_saujani = CreateAuthor("Saujani", "Reshma", "Reshma Saujani is the Founder \
                         and CEO of Girls Who Code, a national nonprofit \
                         organization working to close the gender gap in \
                         technology while teaching girls confidence and \
                         bravery through coding. She’s been named one of \
                         Fortune‘s 40 under 40, a WSJ magazine innovator of \
                         the year, one of the 50 most powerful women in New \
                         York by the New York Daily News,Forbes‘s Most \
                         Powerful Women Changing the World, Business \
                         Insider‘s 50 Women Who Are Changing the World, and \
                         an AOL/PBS MAKER. She is the author of Girls Who \
                         Code, a New York Times bestselling book for young \
                         readers.").__dict__
author_catalog.append(r_saujani)

i_mbue = CreateAuthor("Mbue", "Imbolo", "Imbolo Mbue is a native of the \
                      seaside town of Limbe, Cameroon. She holds a BS from \
                      Rutgers University and an MA from Columbia University. \
                      A resident of the United States for more than a decade, \
                      she lives in New York City.").__dict__
author_catalog.append(i_mbue)

a_rubin = CreateAuthor("Rubin", "Adam", "Adam Rubin is the New York Times best\
                       -selling author of a half dozen critically-acclaimed \
                       picture books including Robo-Sauce and Dragons Love \
                       Tacos. He spent ten years working as a creative \
                       director in the advertising industry before leaving \
                       his day job to write full time. Adam has a keen \
                       interest in improv comedy, camping and magic tricks. \
                       He lives in New York City.").__dict__
author_catalog.append(a_rubin)

d_salmieri = CreateAuthor("Salmieri", "Daniel").__dict__
author_catalog.append(d_salmieri)

j_didion = CreateAuthor("Didion", "Joan", "Joan Didion is the author of five \
                        novels and nine books of nonfiction. Her collected \
                        nonfiction, We Tell Ourselves Stories in Order to \
                        Live, was published by Everyman’s Library in 2006. \
                        Born in Sacramento, California, Didion now lives in \
                        New York City.").__dict__
author_catalog.append(j_didion)

a_brown = CreateAuthor("Brown", "Alton", "Alton Brown used to direct TV \
                       commercials and cook on the side. Then he got the \
                       crazy idea to go to culinary school and reinvent the \
                       food show. The result: Good Eats, which kept Brown \
                       gainfully employed for fifteen years and earned him a \
                       Peabody Award. Along the way he also hosted Iron Chef \
                       America and Feasting on Asphalt and wrote seven books \
                       in his spare time. In 2013 he launched a live culinary \
                       variety show called The Edible Inevitable tour, which \
                       played to sold out theaters across the United States. \
                       In the spring of 2016, Brown’s new live show, Eat Your \
                       Science, toured forty U.S. cities. Brown also hosts \
                       the insanely popular Cutthroat Kitchen on Food \
                       Network.").__dict__
author_catalog.append(a_brown)

l_bastianich = CreateAuthor("Bastianich", "Lidia Matticchio", "Lidia \
                            Matticchio Bastianich is the author of thirteen \
                            cookbooks and the Emmy award-winning host of \
                            public television’s Lidia’s Kitchen, which also \
                            airs internationally. She is also a judge on \
                            MasterChef Junior Italy and Italy’s highly rated \
                            daily program La Prova del Cuoco. Lidia owns \
                            Felidia, Becco, several other restaurants, and is \
                            a partner in the acclaimed Eataly. She lives on \
                            Long Island, New York.").__dict__
author_catalog.append(l_bastianich)

t_manuali = CreateAuthor("Manuali", "Tanya Bastianich").__dict__
author_catalog.append(t_manuali)

a_dewdney = CreateAuthor("Dewdney", "Anna", "Anna Dewdney was a teacher, \
                         mother, and enthusiastic proponent of reading aloud \
                         to children. She continually honed her skills as an \
                         artist and writer and published her first Llama \
                         Llama book in 2005. Her passion for creating \
                         extended to home and garden and she lovingly \
                         restored an eighteenth-century farmhouse in southern \
                         Vermont. She wrote, painted, gardened, and lived \
                         there with her partner, Reed, her two daughters, two \
                         wirehaired pointing griffons, and one bulldog. Anna \
                         passed away in 2016, but her spirit will live on in \
                         her books.").__dict__
author_catalog.append(a_dewdney)

r_duncan = CreateAuthor("Duncan", "Reed").__dict__
author_catalog.append(r_duncan)

m_atwood = CreateAuthor("Atwood", "Margaret", "Margaret Atwood, whose work \
                        has been published in thirty-five countries, is the \
                        author of more than forty books of fiction, poetry, \
                        and critical essays. In addition to The Handmaid’s \
                        Tale, her novels include Cat’s Eye, short-listed for \
                        the 1989 Booker Prize; Alias Grace, which won the \
                        Giller Prize in Canada and the Premio Mondello in \
                        Italy; The Blind Assassin, winner of the 2000 Booker \
                        Prize; Oryx and Crake, short-listed for the 2003 Man \
                        Booker Prize; The Year of the Flood; and MaddAddam. \
                        She is the recipient of the Los Angeles Times \
                        Innovator’s Award, and lives in Toronto with the \
                        writer Graeme Gibson.").__dict__
author_catalog.append(m_atwood)

d_eggers = CreateAuthor("Eggers", "Dave", "Dave Eggers grew up near Chicago \
                        and graduated from the University of Illinois at \
                        Urbana-Champaign. He is the founder of McSweeney’s, \
                        an independent publishing house in San Francisco that \
                        produces books, a quarterly journal of new writing \
                        (McSweeney’s Quarterly Concern), and a monthly \
                        magazine, The Believer. McSweeney’s publishes Voice \
                        of Witness, a nonprofit book series that uses oral \
                        history to illuminate human rights crises around the \
                        world. In 2002, he co-founded 826 Valencia, a \
                        nonprofit youth writing and tutoring center in San \
                        Francisco’s Mission District. Sister centers have \
                        since opened in seven other American cities under the \
                        umbrella of 826 National, and like-minded centers \
                        have opened in Dublin, London, Copenhagen, Stockholm, \
                        and Birmingham, Alabama, among other locations. \
                        Eggers’s work has been nominated for the National \
                        Book Award, the Pulitzer Prize, and the National Book \
                        Critics Circle Award, and has won the Dayton Literary \
                        Peace Prize, France’s Prix Médicis, Germany’s \
                        Albatross Prize, the National Magazine Award, and the \
                        American Book Award. Eggers lives in Northern \
                        California with his family. His novels include The \
                        Circle, A Hologram for the King, and Heroes of the \
                        Frontier.").__dict__
author_catalog.append(d_eggers)

d_seuss = CreateAuthor("Seuss", "Dr.", "Theodor Seuss Geisel—aka Dr. Seuss—is \
                       one of the most beloved children’s book authors of all \
                       time. From The Cat in the Hat to Oh, the Places You’ll \
                       Go!, his iconic characters, stories, and art style \
                       have been a lasting influence on generations of \
                       children and adults. The books he wrote and \
                       illustrated under the name Dr. Seuss (and others that \
                       he wrote but did not illustrate, including some under \
                       the pseudonyms Theo. LeSieg and Rosetta Stone) have \
                       been translated into 30 languages. Hundreds of \
                       millions of copies have found their way into homes and \
                       hearts around the world. Dr. Seuss’s long list of \
                       awards includes Caldecott Honors for McElligot’s Pool, \
                       If I Ran the Zoo, and Bartholomew and the Oobleck; the \
                       Pulitzer Prize; and eight honorary doctorates. Works \
                       based on his original stories have won three Oscars, \
                       three Emmys, three Grammys, and a Peabody.").__dict__
author_catalog.append(d_seuss)

j_slate = CreateAuthor("Slate", "Jenny", "Jenny Slate is a writer, comedian, \
                       and actress. She and Dean Fleischer-Camp created the \
                       short film Marcel the Shell with Shoes On in the late \
                       summer of 2010. It screened at film festivals all over \
                       the world, including Sundance and the New York \
                       International Children’s Film Festival, where it won \
                       the Grand Jury and Audience Awards. It subsequently \
                       became a viral sensation, garnering more than 20 \
                       million views on YouTube. Their first picture book, \
                       Marcel the Shell with Shoes On: Things About Me, was a \
                       New York Times bestseller. Slate has appeared in \
                       numerous films and TV programs, including Obvious \
                       Child, Saturday Night Live, Parks and Recreation, and \
                       Zootopia.").__dict__
author_catalog.append(j_slate)

d_camp = CreateAuthor("Fleischer-Camp", "Dean", "Dean Fleischer-Camp is a \
                      writer, director, and artist. He and Jenny Slate \
                      created the short film Marcel the Shell with Shoes On \
                      in the late summer of 2010. It screened at film \
                      festivals all over the world, including Sundance and \
                      the New York International Children’s Film Festival, \
                      where it won the Grand Jury and Audience Awards. It \
                      subsequently became a viral sensation, garnering more \
                      than 20 million views on YouTube. Their first picture \
                      book, Marcel the Shell with Shoes On: Things About Me, \
                      was a New York Times bestseller.").__dict__
author_catalog.append(d_camp)

j_baldwin = CreateAuthor("Baldwin", "James", "James Baldwin (1924–1987) was a \
                         novelist, essayist, playwright, poet, and social \
                         critic. His first novel, Go Tell It on the Mountain, \
                         appeared in 1953 to excellent reviews, and his essay \
                         collections Notes of a Native Son and The Fire Next \
                         Time were bestsellers that made him an influential \
                         figure in the growing civil rights movement. Baldwin \
                         spent much of his life in France, where he moved to \
                         escape the racism and homophobia of the United \
                         States. He died in France in 1987, a year after \
                         being made a Commander of the French Legion of \
                         Honor.").__dict__
author_catalog.append(j_baldwin)

m_stewart = CreateAuthor("Stewart", "Martha", "Martha Stewart is the author \
                         of dozens of bestselling books on cooking, \
                         entertaining, homekeeping, gardening, weddings, and \
                         decorating. She was the host of The Martha Stewart \
                         Show, the Emmy-winning daily syndicated television \
                         program, and is the founder of Martha Stewart Living \
                         Omnimedia, which publishes several magazines, \
                         including Martha Stewart Living.").__dict__
author_catalog.append(m_stewart)

m_crichton = CreateAuthor("Crichton", "Michael", "Michael Crichton was a \
                          writer, director, and producer, best known as the \
                          author of Jurassic Park and the creator of ER. One \
                          of the most recognizable names in literature and \
                          entertainment, Crichton sold more than 200 million \
                          copies of his books, which have been translated \
                          into 40 languages and adapted into 15 films. He \
                          died in 2008.").__dict__
author_catalog.append(m_crichton)

e_cline = CreateAuthor("Cline", "Ernest", "Ernest Cline is an internationally \
                       best-selling novelist, screenwriter, father, and full-\
                       time geek. He is the #1 New York Times best-selling \
                       author of the novels Ready Player One and Armada, and \
                       co-screenwriter of the blockbuster film adaptation of \
                       Ready Player One, directed by Steven Spielberg.  His \
                       books have been published in over fifty countries and \
                       have spent more than 100 weeks on The New York Times \
                       Best Sellers list.  He lives in Austin, Texas, with \
                       his family, a time-traveling DeLorean, and a large \
                       collection of classic video games.").__dict__
author_catalog.append(e_cline)

a_weir = CreateAuthor("Weir", "Andy", "Andy Weir built a career as a software \
                      engineer until the success of his first published \
                      novel, THE MARTIAN, allowed him to live out his dream \
                      of writing fulltime. He is a lifelong space nerd and a \
                      devoted hobbyist of subjects such as relativistic \
                      physics, orbital mechanics, and the history of manned \
                      spaceflight. He also mixes a mean cocktail. He lives in \
                      California.").__dict__
author_catalog.append(a_weir)

m_maron = CreateAuthor("Maron", "Marc", "Marc Maron is a stand-up comedian \
                       and host of the podcast WTF with Marc Maron. He has \
                       appeared in his own comedy specials on Comedy Central \
                       and HBO, and his sitcom Maron airs on IFC. He lives in \
                       Los Angeles.").__dict__
author_catalog.append(m_maron)

k_vonnegut = CreateAuthor("Vonnegut", "Kurt", "Kurt Vonnegut was a master of \
                          contemporary American literature. His black humor, \
                          satiric voice, and incomparable imagination first \
                          captured America’s attention in The Sirens of Titan \
                          in 1959 and established him, in the words of The \
                          New York Times, as “a true artist” with the \
                          publication of Cat’s Cradle in 1963. He was, as \
                          Graham Greene declared, “one of the best living \
                          American writers.” Mr. Vonnegut passed away in \
                          April 2007.").__dict__
author_catalog.append(k_vonnegut)

z_smith = CreateAuthor("Smith", "Zadie", "Zadie Smith is the author of the \
                       novels White Teeth, The Autograph Man, On Beauty, NW \
                       and Swing Time, as well as a novella, The Embassy of \
                       Cambodia, and a collection of essays, Changing My \
                       Mind. She is also the editor of The Book of Other \
                       People. Zadie was elected a fellow of the Royal \
                       Society of Literature in 2002, and was listed as one \
                       of Granta’s 20 Best Young British Novelists in 2003 \
                       and again in 2013. White Teeth won multiple literary \
                       awards including the James Tait Black Memorial Prize, \
                       the Whitbread First Novel Award and the Guardian First \
                       Book Award. On Beauty was shortlisted for the Man \
                       Booker Prize and won the Orange Prize for Fiction, and \
                       NW was shortlisted for the Baileys Women’s Prize for \
                       Fiction. Zadie Smith is currently a tenured professor \
                       of fiction at New York University and a Member of the \
                       American Academy of Arts and Letters.").__dict__
author_catalog.append(z_smith)

c_achebe = CreateAuthor("Achebe", "Chinua", "Chinua Achebe was born in \
                        Nigeria in 1930. His first novel, Things Falls Apart, \
                        became a classic of international literature and \
                        required reading for students worldwide. He also \
                        authored four subsequent novels, two short-story \
                        collections, and numerous other books. He was the \
                        David and Marianna Fisher University Professor and \
                        Professor of Africana Studies at Brown University \
                        and, for more than 15 years, was the Charles P. \
                        Stevenson Jr. Professor of Languages and Literature \
                        at Bard College. In 2007, Achebe was awarded the Man \
                        Booker International Prize for lifetime achievement. \
                        He died in 2013.").__dict__
author_catalog.append(c_achebe)

g_vidal = CreateAuthor("Vidal", "Gore", "Gore Vidal (1925–2012) was born at \
                       the United States Military Academy at West Point. His \
                       first novel, Williwaw, written when he was 19 years \
                       old and serving in the army, appeared in the spring of \
                       1946. He wrote 23 novels, five plays, many \
                       screenplays, short stories, well over 200 essays, and \
                       a memoir.").__dict__
author_catalog.append(g_vidal)

n_macdonald = CreateAuthor("Macdonald", "Norm", "Norm Macdonald is a stand-up \
                           comedian, writer, and actor who lives in Los \
                           Angeles. He is the proud father of Devery. From \
                           the Hardcover edition.").__dict__
author_catalog.append(n_macdonald)

g_watsky = CreateAuthor("Watsky", "George", "George Watsky is a writer and \
                        musician from San Francisco, California. After \
                        getting his start as a teenager in competitive poetry \
                        slam, winning both the Youth Speaks Slam and Brave \
                        New Voices National Poetry Slam at the Apollo \
                        Theater, he has since branched out into hip hop and \
                        long-form writing. Watsky has performed on HBO’s \
                        Russell Simmons Presents Def Poetry, the Ellen Show, \
                        the NAACP Image Awards, and his online videos have \
                        received hundreds of millions of YouTube hits. A \
                        committed live performer, he’s played hundreds of \
                        shows, both with his band and solo, across the North \
                        America, Europe, Australia, and India, including \
                        festival slots at San Francisco’s Outside Lands, Just \
                        for Laughs in Montreal, Rock the Bells, Soundset, \
                        Warped Tour, and released numerous music albums and \
                        mixtapes, including his most recent projects, 2013’s \
                        “Cardboard Castles” and 2014’s “All You Can Do.” He \
                        graduated from Emerson College with a degree in \
                        acting and dramatic writing, where he received the \
                        Rod Parker playwriting fellowship, and released a \
                        poetry collection, “Undisputed Backtalk Champion,” on \
                        First Word Press way back in 2006. And although he \
                        was forced to write a lot essays in school, he \
                        considers this his first attempt at prose.").__dict__
author_catalog.append(g_watsky)

p_robinson = CreateAuthor("Robinson", "Phoebe", "Phoebe Robinson is a stand-\
                          up comedian, actress, and the author of the New \
                          York Times bestseller You Can’t Touch My Hair. \
                          Most recently, she and Jessica Williams turned \
                          their hit WNYC Studios podcast, 2 Dope Queens, into \
                          four one-hour HBO specials. Robinson has also \
                          appeared on The Late Show with Stephen Colbert, \
                          Late Night with Seth Meyers, Conan, Broad City, \
                          Search Party, The Daily Show, and the Today show; \
                          she was also a staff writer on the final season of \
                          Portlandia. When not working in TV, she’s the host \
                          of the critically acclaimed WNYC Studios interview \
                          podcast Sooo Many White Guys. She recently made her \
                          feature film debut in the Netflix comedy Ibiza, \
                          released earlier this year.").__dict__
author_catalog.append(p_robinson)

o_jeffers = CreateAuthor("Jeffers", "Oliver").__dict__
author_catalog.append(o_jeffers)

j_klassen = CreateAuthor("Klassen", "Jon").__dict__
author_catalog.append(j_klassen)

m_barnett = CreateAuthor("Barnett", "Mac").__dict__
author_catalog.append(m_barnett)


# Create books


book_catalog = []


class CreateBook:
    def __init__(self, title, cover, description):
        self.title = title
        self.cover = cover
        self.description = description
        self.authors = []
        self.genres = []


this_is_not_my_hat = CreateBook("This Is Not My Hat",
                                "https://images.penguinrandomhouse.com/cover/9780763655990",  # NOQA
                                "From the creator of the #1 New York Times \
                                best-selling and award-winning I Want My Hat \
                                Back comes a second wry tale.<br/>When a tiny \
                                fish shoots into view wearing a round blue \
                                topper (which happens to fit him perfectly), \
                                trouble could be following close behind. So \
                                it’s a good thing that enormous fish won’t \
                                wake up. And even if he does, it’s not like \
                                he’ll ever know what happened. . . . Visual \
                                humor swims to the fore as the best-selling \
                                Jon Klassen follows his breakout debut with \
                                another deadpan-funny tale.").__dict__
this_is_not_my_hat['authors'].append(
    {"last_name": j_klassen['last_name'],
     "first_name": j_klassen['first_name']})
this_is_not_my_hat['genres'].append({"type": g_children_picture['type']})
book_catalog.append(this_is_not_my_hat)

we_found_a_hat = CreateBook("We Found a Hat",
                            "https://images.penguinrandomhouse.com/cover/9780763656003",  # NOQA
                            "Hold on to your hats for the conclusion of the \
                            celebrated hat trilogy by Caldecott Medalist Jon \
                            Klassen, who gives his deadpan finale a \
                            surprising new twist.<br/>Two turtles have found \
                            a hat. The hat looks good on both of them. But \
                            there are two turtles. And there is only one hat\
                            . . . . Evoking hilarity and sympathy, the \
                            shifting eyes tell the tale in this brilliantly \
                            paced story in three parts, highlighting Jon \
                            Klassen’s visual comedy and deceptive simplicity. \
                            The delicious buildup takes an unexpected turn \
                            that is sure to please loyal fans and newcomers \
                            alike.").__dict__
we_found_a_hat['authors'].append(
    {"last_name": j_klassen['last_name'],
     "first_name": j_klassen['first_name']})
we_found_a_hat['genres'].append({"type": g_children_picture['type']})
book_catalog.append(we_found_a_hat)

sam_and_dave_dig_a_hole = CreateBook("Sam and Dave Dig a Hole",
                                     "https://images.penguinrandomhouse.com/cover/9780763662295",  # NOQA
                                     "With perfect pacing, the multi-award-\
                                     winning, New York Times best-selling \
                                     team of Mac Barnett and Jon Klassen dig \
                                     down for a deadpan tale full of visual \
                                     humor.<br/>Sam and Dave are on a \
                                     mission. A mission to find something \
                                     spectacular. So they dig a hole. And \
                                     they keep digging. And they find . . . \
                                     nothing. Yet the day turns out to be \
                                     pretty spectacular after all. Attentive \
                                     readers will be rewarded with a rare \
                                     treasure in this witty story of looking \
                                     for the extraordinary — and finding it \
                                     in a manner you’d never expect."
                                     ).__dict__
sam_and_dave_dig_a_hole['authors'].append(
    {"last_name": j_klassen['last_name'],
     "first_name": j_klassen['first_name']})
sam_and_dave_dig_a_hole['authors'].append(
    {"last_name": m_barnett['last_name'],
     "first_name": m_barnett['first_name']})
sam_and_dave_dig_a_hole['genres'].append({"type": g_children_picture['type']})
book_catalog.append(sam_and_dave_dig_a_hole)

square = CreateBook("Square",
                    "https://images.penguinrandomhouse.com/cover/9780763696078",  # NOQA
                    "The beguiling second entry in the innovative shape \
                    trilogy by multi-award-winning, New York Times best-\
                    selling duo Mac Barnett and Jon Klassen.<br/>This book is \
                    about Square. Square spends every day taking blocks from \
                    a pile below the ground to a pile above the ground. This \
                    book is also about Square’s friend Circle. Circle thinks \
                    Square is an artistic genius. But is he really? With the \
                    second story in a trilogy of tales about Triangle, \
                    Square, and Circle, Mac Barnett and Jon Klassen nudge \
                    readers toward a more well-rounded way of looking at \
                    things. Understated and striking in its simplicity, this \
                    funny, thoughtful offering from two of today’s most \
                    talented picture-book creators emphasizes the importance \
                    of keeping your eyes — and your mind — open to wonder \
                    where others see only rubble and rocks.").__dict__
square['authors'].append(
    {"last_name": j_klassen['last_name'],
     "first_name": j_klassen['first_name']})
square['authors'].append(
    {"last_name": m_barnett['last_name'],
     "first_name": m_barnett['first_name']})
square['genres'].append({"type": g_children_picture['type']})
book_catalog.append(square)

i_want_my_hat_back = CreateBook("I Want My Hat Back",
                                "https://images.penguinrandomhouse.com/cover/9780763655983",  # NOQA
                                "A picture-book delight by a rising talent \
                                tells a cumulative tale with a mischievous \
                                twist.<br/>The bear’s hat is gone, and he \
                                wants it back. Patiently and politely, he \
                                asks the animals he comes across, one by one, \
                                whether they have seen it. Each animal says \
                                no, some more elaborately than others. But \
                                just as the bear begins to despond, a deer \
                                comes by and asks a simple question that \
                                sparks the bear’s memory and renews his \
                                search with a vengeance. Told completely in \
                                dialogue, this delicious take on the classic \
                                repetitive tale plays out in sly \
                                illustrations laced with visual humor— and \
                                winks at the reader with a wry irreverence \
                                that will have kids of all ages thrilled to \
                                be in on the joke.").__dict__
i_want_my_hat_back['authors'].append(
    {"last_name": j_klassen['last_name'],
     "first_name": j_klassen['first_name']})
i_want_my_hat_back['genres'].append({"type": g_children_picture['type']})
book_catalog.append(i_want_my_hat_back)


up_and_down = CreateBook("Up and Down",
                         "https://images.penguinrandomhouse.com/cover/9780399257377",  # NOQA
                         "A penguin has wings for a reason . . . doesn’t he? \
                         Having a best friend with his own airplane is one \
                         thing, but actually experiencing what it feels like \
                         to fly by himself? Here is one penguin who believes \
                         this is precisely what he needs to feel complete. \
                         Only . . . if flying by himself is so wonderful, \
                         then why does he feel so empty?<br/>Because some \
                         experiences are better shared. (And penguins are \
                         much happier on the ground.)").__dict__
up_and_down['authors'].append(
    {"last_name": o_jeffers['last_name'],
     "first_name": o_jeffers['first_name']})
up_and_down['genres'].append({"type": g_children_picture['type']})
book_catalog.append(up_and_down)

this_moose_belongs_to_me = CreateBook("This Moose Belongs to Me",
                                      "https://images.penguinrandomhouse.com/cover/9780399257377",  # NOQA
                                      "Wilfred is a boy with rules. He lives \
                                      a very orderly life. It’s fortunate, \
                                      then, that he has a pet who abides by \
                                      rules, such as not making noise while \
                                      Wilfred educates him on his record \
                                      collection. There is, however, one rule \
                                      that Wilfred’s pet has difficulty \
                                      following: Going whichever way Wilfred \
                                      wants to go. Perhaps this is because \
                                      Wilfred’s pet doesn’t quite realize \
                                      that he belongs to anyone.<br/>A moose \
                                      can be obstinate in such ways.<br/>\
                                      Fortunately, the two manage to work out \
                                      a compromise. Let’s just say it \
                                      involves apples.").__dict__
this_moose_belongs_to_me['authors'].append(
    {"last_name": o_jeffers['last_name'],
     "first_name": o_jeffers['first_name']})
this_moose_belongs_to_me['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(this_moose_belongs_to_me)

stuck = CreateBook("Stuck",
                   "https://images.penguinrandomhouse.com/cover/9780399257377",  # NOQA
                   "From the illustrator of the #1 smash The Day the Crayons \
                   Quit comes another bestseller–a giggle-inducing tale of \
                   everything tossed, thrown, and hurled in order to free a \
                   kite!<br/>When Floyd’s kite gets stuck in a tree, he’s \
                   determined to get it out. But how? Well, by knocking it \
                   down with his shoe, of course. But strangely enough, it \
                   too gets stuck. And the only logical course of action \
                   . . . is to throw his other shoe. Only now it’s stuck! \
                   Surely there must be something he can use to get his kite \
                   unstuck. An orangutan? A boat? His front door? Yes, yes, \
                   and yes. And that’s only the beginning. Stuck is Oliver \
                   Jeffers’ most absurdly funny story since The Incredible \
                   Book-Eating Boy. Childlike in concept and vibrantly \
                   illustrated as only Oliver Jeffers could, here is a \
                   picture book worth rescuing from any tree.").__dict__
stuck['authors'].append(
    {"last_name": o_jeffers['last_name'],
     "first_name": o_jeffers['first_name']})
stuck['genres'].append({"type": g_children_picture['type']})
book_catalog.append(stuck)

the_year_of_the_flood = CreateBook("The Year of the Flood",
                                   "https://images.penguinrandomhouse.com/cover/9780307455475",  # NOQA
                                   "Set in the visionary future of Atwood’s \
                                   acclaimed Oryx and Crake, The Year of the \
                                   Flood is at once a moving tale of lasting \
                                   friendship and a landmark work of \
                                   speculative fiction. In this second book \
                                   of the MaddAddam trilogy, the long-feared \
                                   waterless flood has occurred, altering \
                                   Earth as we know it and obliterating most \
                                   human life. Among the survivors are Ren, a \
                                   young trapeze dancer locked inside the \
                                   high-end sex club Scales and Tails, and \
                                   Toby, who is barricaded inside a luxurious \
                                   spa. Amid shadowy, corrupt ruling powers \
                                   and new, gene-spliced life forms, Ren and \
                                   Toby will have to decide on their next \
                                   move, but they can’t stay locked \
                                   away.").__dict__
the_year_of_the_flood['authors'].append(
    {"last_name": m_atwood['last_name'],
     "first_name": m_atwood['first_name']})
the_year_of_the_flood['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_year_of_the_flood)

everythings_trash_but_its_okay = CreateBook("Everything’s Trash, But It’s Okay",
                                            "https://images.penguinrandomhouse.com/cover/9780525534143",  # NOQA
                                            "From New York Times bestselling \
                                            author and star of 2 Dope Queens, \
                                            Phoebe Robinson, comes a new, \
                                            hilarious, and timely essay \
                                            collection on gender, race, \
                                            dating, and a world that seems to \
                                            always be a self-starting \
                                            Dumpster fire.<br/>Wouldn’t it be \
                                            great if life came with \
                                            instructions? Of course, but like \
                                            access to Michael B. Jordan’s \
                                            house, none of us are getting \
                                            any. Thankfully, Phoebe Robinson \
                                            is ready to share everything she \
                                            has experienced to prove that if \
                                            you can laugh at her topsy-turvy \
                                            life, you can laugh at your own.\
                                            <br/>Written in her trademark \
                                            unfiltered and singularly witty \
                                            style, Robinson’s latest essay \
                                            collection is a call to arms. She \
                                            tackles a wide range of topics, \
                                            such as giving feminism a tough-\
                                            love talk in hopes it can become \
                                            more intersectional; telling \
                                            society’s beauty standards to \
                                            kick rocks; and takes a hard \
                                            look at our culture’s obsession \
                                            with work.<br/>Robinson also gets \
                                            personal, exploring debt she has \
                                            hidden from her parents, how \
                                            dating is mainly a warmed-over \
                                            bowl of hot mess, and maybe most \
                                            importantly, meeting Bono not \
                                            once, but twice. She’s struggled \
                                            with being a woman with a \
                                            political mind and a woman with \
                                            an ever-changing jeans size. She \
                                            knows about trash not only \
                                            because she sees it every day, \
                                            but also because she’s seen about \
                                            one-hundred-thousand hours of \
                                            reality TV and zero hours of \
                                            Schindler’s List.<br/>\
                                            Everything’s Trash, But It’s \
                                            Okay is a candid perspective for \
                                            a generation that has had the rug \
                                            pulled out from under it too many \
                                            times to count, as well as an \
                                            intimate conversation with a new \
                                            best friend.").__dict__
everythings_trash_but_its_okay['authors'].append(
    {"last_name": p_robinson['last_name'],
     "first_name": p_robinson['first_name']})
everythings_trash_but_its_okay['genres'].append({"type": g_humor['type']})
everythings_trash_but_its_okay['genres'].append(
    {"type": g_biography_memoir['type']})
book_catalog.append(everythings_trash_but_its_okay)

you_cant_touch_my_hair = CreateBook("You Can’t Touch My Hair",
                                    "https://images.penguinrandomhouse.com/cover/9780143129202",  # NOQA
                                    "A hilarious and timely essay collection \
                                    about race, gender, and pop culture from \
                                    comedy superstar and 2 Dope Queens \
                                    podcaster Phoebe Robinson<br/>Being a \
                                    black woman in America means contending \
                                    with old prejudices and fresh absurdities \
                                    every day. Comedian Phoebe Robinson has \
                                    experienced her fair share over the \
                                    years: she’s been unceremoniously \
                                    relegated to the role of “the black \
                                    friend,” as if she is somehow the \
                                    authority on all things racial; she’s \
                                    been questioned about her love of U2 and \
                                    Billy Joel (“isn’t that…white people \
                                    music?”); she’s been called “uppity” for \
                                    having an opinion in the workplace; she’s \
                                    been followed around stores by security \
                                    guards; and yes, people do ask her \
                                    whether they can touch her hair all. the. \
                                    time. Now, she’s ready to take these \
                                    topics to the page—and she’s going to \
                                    make you laugh as she’s doing it.<br/>\
                                    Using her trademark wit alongside pop-\
                                    culture references galore, Robinson \
                                    explores everything from why Lisa Bonet \
                                    is “Queen. Bae. Jesus,” to breaking down \
                                    the terrible nature of casting calls, to \
                                    giving her less-than-traditional advice \
                                    to the future female president, and \
                                    demanding that the NFL clean up its act, \
                                    all told in the same conversational voice \
                                    that launched her podcast, 2 Dope Queens, \
                                    to the top spot on iTunes. As personal as \
                                    it is political, You Can’t Touch My Hair \
                                    examines our cultural climate and skewers \
                                    our biases with humor and heart, \
                                    announcing Robinson as a writer on the \
                                    rise.").__dict__
you_cant_touch_my_hair['authors'].append(
    {"last_name": p_robinson['last_name'],
     "first_name": p_robinson['first_name']})
you_cant_touch_my_hair['genres'].append({"type": g_humor['type']})
you_cant_touch_my_hair['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(you_cant_touch_my_hair)

how_to_ruin_everything = CreateBook(
    "How to Ruin Everything",
    "https://images.penguinrandomhouse.com/cover/9780147515995",
    "Are you a sensible, universally competent individual? Are you tired of \
    the crushing monotony of leaping gracefully from one lily pad of success \
    to the next? Are you sick of doing everything right?<br/>In this brutally \
    honest and humorous debut, musician and artist George Watsky chronicles \
    the small triumphs over humiliation that make life bearable and how he \
    has come to accept defeat as necessary to personal progress. The essays \
    in How to Ruin Everything range from the absurd (how he became an \
    international ivory smuggler) to the comical (his middle-school rap \
    battle dominance) to the revelatory (his experiences with epilepsy), yet \
    all are delivered with the type of linguistic dexterity and self-\
    awareness that has won Watsky devoted fans across the globe. Alternately \
    ribald and emotionally resonant, How to Ruin Everything announces a \
    versatile writer with a promising career ahead."
).__dict__
how_to_ruin_everything['authors'].append(
    {"last_name": g_watsky['last_name'],
     "first_name": g_watsky['first_name']})
how_to_ruin_everything['genres'].append({"type": g_humor['type']})
how_to_ruin_everything['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(how_to_ruin_everything)

based_on_a_true_story = CreateBook(
    "Based on a True Story",
    "https://images.penguinrandomhouse.com/cover/9780812983869",
    "When Norm Macdonald, one of the greatest stand-up comics of all time, \
    was approached to write a celebrity memoir, he flatly refused, calling \
    the genre “one step below instruction manuals.” Norm then promptly took a \
    two-year hiatus from stand-up comedy to live on a farm in northern \
    Canada. When he emerged he had under his arm a manuscript, a genre-\
    smashing book about comedy, tragedy, love, loss, war, and redemption. \
    When asked if this was the celebrity memoir, Norm replied, “Call it \
    anything you damn like.”"
).__dict__
based_on_a_true_story['authors'].append(
    {"last_name": n_macdonald['last_name'],
     "first_name": n_macdonald['first_name']})
based_on_a_true_story['genres'].append({"type": g_humor['type']})
book_catalog.append(based_on_a_true_story)

lincoln = CreateBook(
    "Lincoln",
    "https://images.penguinrandomhouse.com/cover/9780375708763",
    "Gore Vidal’s Narratives of Empire series spans the history of the United \
    States from the Revolution to the post-World War II years. With their \
    broad canvas and large cast of fictional and historical characters, the \
    novels in this series present a panorama of the American political and \
    imperial experience as interpreted by one of its most worldly, knowing, \
    and ironic observers.<br/>To most Americans, Abraham Lincoln is a \
    monolithic figure, the Great Emancipator and Savior of the Union, beloved \
    by all. In Gore Vidal’s Lincoln we meet Lincoln the man and Lincoln the \
    political animal, the president who entered a besieged capital where most \
    of the population supported the South and where even those favoring the \
    Union had serious doubts that the man from Illinois could save it. Far \
    from steadfast in his abhorrence of slavery, Lincoln agonizes over the \
    best course of action and comes to his great decision only when all else \
    seems to fail. As the Civil War ravages his nation, Lincoln must face \
    deep personal turmoil, the loss of his dearest son, and the harangues of \
    a wife seen as a traitor for her Southern connections. Brilliantly \
    conceived, masterfully executed, Gore Vidal’s Lincoln allows the man to \
    breathe again."
).__dict__
lincoln['authors'].append(
    {"last_name": g_vidal['last_name'],
     "first_name": g_vidal['first_name']})
lincoln['genres'].append({"type": g_historical_fiction['type']})
lincoln['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(lincoln)

burr = CreateBook(
    "Burr",
    "https://images.penguinrandomhouse.com/cover/9780375708732",
    "For readers who can’t get enough of the hit Broadway musical Hamilton, \
    Gore Vidal’s stunning novel about Aaron Burr, the man who killed \
    Alexander Hamilton in a duel—and who served as a successful, if often \
    feared, statesman of our fledgling nation.<br/>Here is an extraordinary \
    portrait of one of the most complicated—and misunderstood—figures among \
    the Founding Fathers. In 1804, while serving as vice president, Aaron \
    Burr fought a duel with his political nemesis, Alexander Hamilton, and \
    killed him. In 1807, he was arrested, tried, and acquitted of treason. In \
    1833, Burr is newly married, an aging statesman considered a monster by \
    many. But he is determined to tell his own story, and he chooses to \
    confide in a young New York City journalist named Charles Schermerhorn \
    Schuyler. Together, they explore both Burr’s past—and the continuing \
    civic drama of their young nation.<br/>Burr is the first novel in Gore \
    Vidal’s Narratives of Empire series, which spans the history of the \
    United States from the Revolution to post-World War II. With their broad \
    canvas and sprawling cast of fictional and historical characters, these \
    novels present a panorama of American politics and imperialism, as \
    interpreted by one of our most incisive and ironic observers."
).__dict__
burr['authors'].append(
    {"last_name": g_vidal['last_name'],
     "first_name": g_vidal['first_name']})
burr['genres'].append({"type": g_historical_fiction['type']})
burr['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(burr)

julian = CreateBook("Julian",
    "https://images.penguinrandomhouse.com/cover/9780375727061",
    "The remarkable bestseller about the fourth-century Roman emperor who \
    famously tried to halt the spread of Christianity, Julian is widely \
    regarded as one of Gore Vidal’s finest historical novels.<br/>Julian the \
    Apostate, nephew of Constantine the Great, was one of the brightest yet \
    briefest lights in the history of the Roman Empire. A military genius on \
    the level of Julius Caesar and Alexander the Great, a graceful and \
    persuasive essayist, and a philosopher devoted to worshipping the gods of \
    Hellenism, he became embroiled in a fierce intellectual war with \
    Christianity that provoked his murder at the age of thirty-two, only four \
    years into his brilliantly humane and compassionate reign. A marvelously \
    imaginative and insightful novel of classical antiquity, Julian captures \
    the religious and political ferment of a desperate age and restores with \
    blazing wit and vigor the legacy of an impassioned ruler."
).__dict__
julian['authors'].append(
    {"last_name": g_vidal['last_name'],
     "first_name": g_vidal['first_name']})
julian['genres'].append({"type": g_historical_fiction['type']})
julian['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(julian)

chike_and_the_river = CreateBook(
    "Chike and the River",
    "https://images.penguinrandomhouse.com/cover/9780307473868",
    "Eleven-year-old Chike longs to cross the Niger River to the city of \
    Asaba, but he doesn’t have the sixpence he needs to pay for the ferry \
    ride. With the help of his friend S.M.O.G., he embarks on a series of \
    adventures to help him get there. Along the way, he is exposed to a range \
    of new experiences that are both thrilling and terrifying, from eating \
    his first skewer of suya under the shade of a mango tree, to visiting the \
    village magician who promises to double the money in his pocket. Once he \
    finally makes it across the river, Chike realizes that life on the other \
    side is far different from his expectations, and he must find the courage \
    within him to make it home.<br/>Chike and the River is a magical tale of \
    boundaries, bravery, and growth, by Chinua Achebe, one of the world’s \
    most beloved and admired storytellers."
).__dict__
chike_and_the_river['authors'].append(
    {"last_name": c_achebe['last_name'],
     "first_name": c_achebe['first_name']})
chike_and_the_river['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(chike_and_the_river)

anthills_of_the_savannah = CreateBook(
    "Anthills of the Savannah",
    "https://images.penguinrandomhouse.com/cover/9780385260459",
    "In the fictional West African nation of Kangan, newly independent of \
    British rule, the hopes and dreams of democracy have been quashed by a \
    fierce military dictatorship. Chris Oriko is a member of the president’s \
    cabinet for life, and one of the leader’s oldest friends. When the \
    president is charged with censoring the opportunistic editor of the state-\
    run newspaper–another childhood friend–Chris’s loyalty and ideology are \
    put to the test. The fate of Kangan hangs in the balance as tensions rise \
    and a devious plot is set in motion to silence a firebrand critic."
).__dict__
anthills_of_the_savannah['authors'].append(
    {"last_name": c_achebe['last_name'],
     "first_name": c_achebe['first_name']})
anthills_of_the_savannah['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(anthills_of_the_savannah)

a_man_of_the_people = CreateBook(
    "A Man of the People",
    "https://images.penguinrandomhouse.com/cover/9780385086165",
    "As Minister for Culture, former school teacher M. A. Nanga is a man of \
    the people, as cynical as he is charming, and a roguish opportunist. When \
    Odili, an idealistic young teacher, visits his former instructor at the \
    ministry, the division between them is vast. But in the eat-and-let-eat \
    atmosphere, Odili’s idealism soon collides with his lusts—and the two \
    men’s personal and political tauntings threaten to send their country \
    into chaos. When Odili launches a vicious campaign against his former \
    mentor for the same seat in an election, their mutual animosity drives \
    the country to revolution.<br/>Published, prophetically, just days before \
    Nigeria’s first attempted coup in 1966, A Man of the People is an \
    essential part of Achebe’s body of work."
).__dict__
a_man_of_the_people['authors'].append(
    {"last_name": c_achebe['last_name'],
     "first_name": c_achebe['first_name']})
a_man_of_the_people['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(a_man_of_the_people)

girls_at_war = CreateBook(
    "Girls at War",
    "https://images.penguinrandomhouse.com/cover/9780385418966",
    "Twelve stories by the internationally renowned novelist which recreate \
    with energy and authenticity the major social and political issues that \
    confront contemporary Africans on a daily basis."
).__dict__
girls_at_war['authors'].append(
    {"last_name": c_achebe['last_name'],
     "first_name": c_achebe['first_name']})
girls_at_war['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(girls_at_war)

arrow_of_god = CreateBook(
    "Arrow of God",
    "https://images.penguinrandomhouse.com/cover/9780385014809",
    "When Things Fall Apart ends, colonial rule has been introduced to \
    Umuofia, and the character of the nation, its values, freedoms, religious \
    and socio-political foundations have substantially and irrevocably been \
    altered. Arrow of God, the second novel in Chinua Achebe’s The African \
    Trilogy, moves the historical narrative forward. This time, the action \
    revolves around Ezeulu, the headstrong chief priest of the god Ulu, which \
    is worshipped by the six villages of Umuaro. The novel is a meditation on \
    the nature, uses, and responsibility of power and leadership. Ezeulu \
    finds that his authority is increasingly under threat from rivals within \
    his nation and functionaries of the newly established British colonial \
    government. Yet he sees himself as untouchable. He is forced, with tragic \
    consequences, to reconcile conflicting impulses in his own nature—a need \
    to serve the protecting deity of his Umuaro people; a desire to retain \
    control over their religious observances; and a need to gain increased \
    personal power by pushing his authority to the limits. He ultimately \
    fails as he leads his people to their own destruction, and consequently, \
    his personal tragedy arises. Arrow of God is an unforgettable portrayal \
    of the loss of faith, and the downfall of a man in a society forever \
    altered by colonialism."
).__dict__
arrow_of_god['authors'].append(
    {"last_name": c_achebe['last_name'],
     "first_name": c_achebe['first_name']})
arrow_of_god['genres'].append({"type": g_historical_fiction['type']})
arrow_of_god['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(arrow_of_god)

the_autograph_man = CreateBook(
    "The Autograph Man",
    "https://images.penguinrandomhouse.com/cover/9780375703874",
    "Alex-Li Tandem sells autographs. His business is to hunt for names on \
    paper, collect them, sell them, and occasionally fake them—all to give \
    the people what they want: a little piece of Fame. But what does Alex \
    want? Only the return of his father, the end of religion, something for \
    his headache, three different girls, infinite grace, and the rare \
    autograph of forties movie actress Kitty Alexander. With fries.<br/>The \
    Autograph Man is a deeply funny existential tour around the hollow \
    trappings of modernity: celebrity, cinema, and the ugly triumph of symbol \
    over experience. It offers further proof that Zadie Smith is one of the \
    most staggeringly talented writers of her generation. Look for her new \
    book Swing Time, coming November 2016."
).__dict__
the_autograph_man['authors'].append(
    {"last_name": z_smith['last_name'],
     "first_name": z_smith['first_name']})
the_autograph_man['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_autograph_man)

white_teeth = CreateBook(
    "White Teeth",
    "https://images.penguinrandomhouse.com/cover/9780375703867",
    "Zadie Smith’s dazzling debut caught critics grasping for comparisons and deciding on everyone from Charles Dickens to Salman Rushdie to John Irving and Martin Amis. But the truth is that Zadie Smith’s voice is remarkably, fluently, and altogether wonderfully her own.").__dict__
white_teeth['authors'].append(
    {"last_name": z_smith['last_name'],
     "first_name": z_smith['first_name']})
white_teeth['genres'].append({"type": g_literary_fiction['type']})
white_teeth['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(white_teeth)

nw = CreateBook(
    "NW",
    "https://images.penguinrandomhouse.com/cover/9780143123934",
    "Set in northwest London, Zadie Smith’s brilliant tragicomic novel follows four locals—Leah, Natalie, Felix, and Nathan—as they try to make adult lives outside of Caldwell, the council estate of their childhood. In private houses and public parks, at work and at play, these Londoners inhabit a complicated place, as beautiful as it is brutal, where the thoroughfares hide the back alleys and taking the high road can sometimes lead you to a dead end. Depicting the modern urban zone—familiar to city-dwellers everywhere—NW is a quietly devastating novel of encounters, mercurial and vital, like the city itself."
).__dict__
nw['authors'].append({"last_name": z_smith['last_name'],
                      "first_name": z_smith['first_name']})
nw['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(nw)

feel_free = CreateBook(
    "Feel Free",
    "https://images.penguinrandomhouse.com/cover/9781594206252",
    "Since she burst spectacularly into view with her debut novel almost two decades ago, Zadie Smith has established herself not just as one of the world’s preeminent fiction writers, but also a brilliant and singular essayist. She contributes regularly to The New Yorker and the New York Review of Books on a range of subjects, and each piece of hers is a literary event in its own right.<br/>Arranged into five sections–In the World, In the Audience, In the Gallery, On the Bookshelf, and Feel Free–this new collection poses questions we immediately recognize. What is The Social Network–and Facebook itself–really about? “It’s a cruel portrait of us: 500 million sentient people entrapped in the recent careless thoughts of a Harvard sophomore.” Why do we love libraries? “Well-run libraries are filled with people because what a good library offers cannot be easily found elsewhere: an indoor public space in which you do not have to buy anything in order to stay.” What will we tell our granddaughters about our collective failure to address global warming? “So I might say to her, look: the thing you have to appreciate is that we’d just been through a century of relativism and deconstruction, in which we were informed that most of our fondest-held principles were either uncertain or simple wishful thinking, and in many areas of our lives we had already been asked to accept that nothing is essential and everything changes–and this had taken the fight out of us somewhat.”<br/>Gathering in one place for the first time previously unpublished work, as well as already classic essays, such as, “Joy,” and, “Find Your Beach,” Feel Free offers a survey of important recent events in culture and politics, as well as Smith’s own life. Equally at home in the world of good books and bad politics, Brooklyn-born rappers and the work of Swiss novelists, she is by turns wry, heartfelt, indignant, and incisive–and never any less than perfect company. This is literary journalism at its zenith."
).__dict__
feel_free['authors'].append(
    {"last_name": z_smith['last_name'],
     "first_name": z_smith['first_name']})
feel_free['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(feel_free)

swing_time = CreateBook(
    "Swing Time",
    "https://images.penguinrandomhouse.com/cover/9780143111641",
    "An ambitious, exuberant new novel moving from North West London to West Africa, from the multi-award-winning author of White Teeth and On Beauty.<br/>Two brown girls dream of being dancers—but only one, Tracey, has talent. The other has ideas: about rhythm and time, about black bodies and black music, what constitutes a tribe, or makes a person truly free. It’s a close but complicated childhood friendship that ends abruptly in their early twenties, never to be revisited, but never quite forgotten, either.<br/>Tracey makes it to the chorus line but struggles with adult life, while her friend leaves the old neighborhood behind, traveling the world as an assistant to a famous singer, Aimee, observing close up how the one percent live.<br/>But when Aimee develops grand philanthropic ambitions, the story moves from London to West Africa, where diaspora tourists travel back in time to find their roots, young men risk their lives to escape into a different future, the women dance just like Tracey—the same twists, the same shakes—and the origins of a profound inequality are not a matter of distant history, but a present dance to the music of time."
).__dict__
swing_time['authors'].append(
    {"last_name": z_smith['last_name'],
     "first_name": z_smith['first_name']})
swing_time['genres'].append({"type": g_literary_fiction['type']})
swing_time['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(swing_time)

slaughterhouse_five = CreateBook(
    "Slaughterhouse-Five",
    "https://images.penguinrandomhouse.com/cover/9780385333849",
    "Slaughterhouse-Five, an American classic, is one of the world’s great antiwar books. Centering on the infamous firebombing of Dresden, Billy Pilgrim’s odyssey through time reflects the mythic journey of our own fractured lives as we search for meaning in what we fear most. ").__dict__
slaughterhouse_five['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
slaughterhouse_five['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(slaughterhouse_five)

the_sirens_of_titan = CreateBook(
    "The Sirens of Titan",
    "https://images.penguinrandomhouse.com/cover/9780385333498",
    "The Sirens of Titan is an outrageous romp through space, time, and morality. The richest, most depraved man on Earth, Malachi Constant, is offered a chance to take a space journey to distant worlds with a beautiful woman at his side. Of course there’ s a catch to the invitation–and a prophetic vision about the purpose of human life that only Vonnegut has the courage to tell.").__dict__
the_sirens_of_titan['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
the_sirens_of_titan['genres'].append({"type": g_literary_fiction['type']})
the_sirens_of_titan['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(the_sirens_of_titan)

god_bless_you_mr_rosewater = CreateBook(
    "God Bless You, Mr. Rosewater",
    "https://images.penguinrandomhouse.com/cover/9780385333474",
    "Eliot Rosewater—drunk, volunteer fireman, and President of the fabulously rich Rosewater Foundation—is about to attempt a noble experiment with human nature . . . with a little help from writer Kilgore Trout. God Bless You, Mr. Rosewater is Kurt Vonnegut’s funniest satire, an etched-in-acid portrayal of the greed, hypocrisy, and follies of the flesh we are all heir to.").__dict__
god_bless_you_mr_rosewater['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
god_bless_you_mr_rosewater['genres'].append(
    {"type": g_literary_fiction['type']})
book_catalog.append(god_bless_you_mr_rosewater)

cats_cradle = CreateBook(
    "Cat’s Cradle",
    "https://images.penguinrandomhouse.com/cover/9780385333481",
    "Cat’s Cradle is Kurt Vonnegut’s satirical commentary on modern man and his madness. An apocalyptic tale of this planet’s ultimate fate, it features a midget as the protagonist, a complete, original theology created by a calypso singer, and a vision of the future that is at once blackly fatalistic and hilariously funny. A book that left an indelible mark on an entire generation of readers, Cat’s Cradle is one of the twentieth century’s most important works—and Vonnegut at his very best."
).__dict__
cats_cradle['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
cats_cradle['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(cats_cradle)

player_piano = CreateBook(
    "Player Piano",
    "https://images.penguinrandomhouse.com/cover/9780385333788",
    "Kurt Vonnegut’s first novel spins the chilling tale of engineer Paul Proteus, who must find a way to live in a world dominated by a supercomputer and run completely by machines. Paul’s rebellion is vintage Vonnegut—wildly funny, deadly serious, and terrifyingly close to reality.").__dict__
player_piano['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
player_piano['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(player_piano)

wampeters_foma_granfalloons = CreateBook(
    "Wampeters, Foma & Granfalloons",
    "https://images.penguinrandomhouse.com/cover/9780385333818",
    "Wampeters, Foma & Granfalloons is a rare opportunity to experience Kurt Vonnegut speaking in his own voice about his own life, his views of the world, his writing, and the writing of others. An indignant, outrageous, witty, deeply felt collection of reviews, essays, and speeches, this is a window not only into Vonnegut’s mind but also into his heart.").__dict__
wampeters_foma_granfalloons['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
wampeters_foma_granfalloons['genres'].append(
    {"type": g_biography_memoir['type']})
book_catalog.append(wampeters_foma_granfalloons)

palm_sunday = CreateBook(
    "Palm Sunday",
    "https://images.penguinrandomhouse.com/cover/9780385334266",
    "In this self-portrait by an American genius, Kurt Vonnegut writes with beguiling wit and poignant wisdom about his favorite comedians, country music, a dead friend, a dead marriage, and various cockamamie aspects of his all-too-human journey through life. This is a work that resonates with Vonnegut’s singular voice: the magic sound of a born storyteller mesmerizing us with truth.").__dict__
palm_sunday['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
palm_sunday['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(palm_sunday)

breakfast_of_champions = CreateBook(
    "Breakfast of Champions",
    "https://images.penguinrandomhouse.com/cover/9780385334204",
    "In Breakfast of Champions, one of Kurt Vonnegut’s most beloved characters, the aging writer Kilgore Trout, finds to his horror that a Midwest car dealer is taking his fiction as truth. What follows is murderously funny satire, as Vonnegut looks at war, sex, racism, success, politics, and pollution in America and reminds us how to see the truth.").__dict__
breakfast_of_champions['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
breakfast_of_champions['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(breakfast_of_champions)

deadeye_dick = CreateBook(
    "Deadeye Dick",
    "https://images.penguinrandomhouse.com/cover/9780385334174",
    "Deadeye Dick is Kurt Vonnegut’s funny, chillingly satirical look at the death of innocence. Amid a true Vonnegutian host of horrors—a double murder, a fatal dose of radioactivity, a decapitation, an annihilation of a city by a neutron bomb—Rudy Waltz, aka Deadeye Dick, takes us along on a zany search for absolution and happiness. Here is a tale of crime and punishment that makes us rethink what we believe . . . and who we say we are.").__dict__
deadeye_dick['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
deadeye_dick['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(deadeye_dick)

while_mortals_sleep = CreateBook(
    "While Mortals Sleep",
    "https://images.penguinrandomhouse.com/cover/9780385343749",
    "These previously unpublished, beautifully rendered works of fiction are a testament to Kurt Vonnegut’s unique blend of observation and imagination. Here are stories of men and machines, art and artifice, and how ideals of fortune, fame, and love take curious twists in ordinary lives.<br/>An ambitious builder of roads fritters away his free time with miniature trains—until the women in his life crash his fantasy land. Trapped in a stenography pool, a young dreamer receives a call from a robber on the run, who presents her with a strange proposition. A crusty newspaperman is forced onto a committee to judge Christmas displays—a job that leads him to a suspiciously ostentatious ex-con and then a miracle. Featuring a Foreword by Dave Eggers, While Mortals Sleep is a poignant reflection of our world as it is and as it could be."
).__dict__
while_mortals_sleep['authors'].append(
    {"last_name": k_vonnegut['last_name'],
     "first_name": k_vonnegut['first_name']})
while_mortals_sleep['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(while_mortals_sleep)

the_jerusalem_syndrome = CreateBook(
    "The Jerusalem Syndrome",
    "https://images.penguinrandomhouse.com/cover/9780767908108",
    "The Jerusalem Syndrome is a genuine psychological phenomenon that often strikes visitors to the Holy Land_the delusion that they are suddenly direct vessels for the voice of God. Marc Maron seems to have a distinctly American version of the Jerusalem Syndrome, which has led him on a lifelong quest for religious significance and revelation in the most unlikely of places.<br/>Maron riffs on Beat phenomena with its sacred texts, established rituals, and prescribed pilgrimages. He spends some time exploring the dark side of things, as his obsessions with cocaine (known to Maron as “magic powder”), conspiracy theories, and famous self-destructive comedians convince him that the gates of hell open beneath Los Angeles. As his quest matures, he reveals the religious aspects of Corporate America, pontificating on the timeless beauty of the Coca-Cola logo and even taking a trip to the Philip Morris cigarette factory, where the workers puff their own products with a zealot-like fervor. The culmination of Maron’s Jerusalem Syndrome comes during his own tour of the Holy Land, where, with Sony camcorder glued to his eye socket, he comes face-to-face with his own ambiguous relationship to Judaism and reaches the brink of spiritual revelation_or is it nervous breakdown?"
).__dict__
the_jerusalem_syndrome['authors'].append(
    {"last_name": m_maron['last_name'],
     "first_name": m_maron['first_name']})
the_jerusalem_syndrome['genres'].append({"type": g_humor['type']})
book_catalog.append(the_jerusalem_syndrome)

attempting_normal = CreateBook(
    "Attempting Normal",
    "https://images.penguinrandomhouse.com/cover/9780812982787",
    "Marc Maron is “a master of spinning humor out of anguish” (Bookforum), even when that anguish is pretty clearly self-inflicted. In Attempting Normal, he threads together twenty-five stories from his life and near-death, from his first comedy road trips (with a fugitive junkie comic with a missing tooth) to his love affair with feral animals (his cat rescues are bloody epics) to his surprisingly moving tales of lust, heartbreak, and hope.  The stories are united by Maron’s thrilling storytelling style—intensely smart, disarmingly honest, and explosively funny. Together, they add up to a hilarious and moving tale of failing, flailing, and finding a way."
).__dict__
attempting_normal['authors'].append(
    {"last_name": m_maron['last_name'],
     "first_name": m_maron['first_name']})
attempting_normal['genres'].append({"type": g_humor['type']})
book_catalog.append(attempting_normal)

artemis = CreateBook(
    "Artemis",
    "https://images.penguinrandomhouse.com/cover/9780553448146",
    "Jasmine Bashara never signed up to be a hero. She just wanted to get rich.<br/>Not crazy, eccentric-billionaire rich, like many of the visitors to her hometown of Artemis, humanity’s first and only lunar colony. Just rich enough to move out of her coffin-sized apartment and eat something better than flavored algae. Rich enough to pay off a debt she’s owed for a long time.<br/>So when a chance at a huge score finally comes her way, Jazz can’t say no. Sure, it requires her to graduate from small-time smuggler to full-on criminal mastermind. And it calls for a particular combination of cunning, technical skills, and large explosions—not to mention sheer brazen swagger. But Jazz has never run into a challenge her intellect can’t handle, and she figures she’s got the ‘swagger’ part down.<br/>The trouble is, engineering the perfect crime is just the start of Jazz’s problems. Because her little heist is about to land her in the middle of a conspiracy for control of Artemis itself.<br/>Trapped between competing forces, pursued by a killer and the law alike, even Jazz has to admit she’s in way over her head. She’ll have to hatch a truly spectacular scheme to have a chance at staying alive and saving her city.<br/>Jazz is no hero, but she is a very good criminal.<br/>That’ll have to do. "
).__dict__
artemis['authors'].append(
    {"last_name": a_weir['last_name'],
     "first_name": a_weir['first_name']})
artemis['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(artemis)

the_martian = CreateBook(
    "The Martian",
    "https://images.penguinrandomhouse.com/cover/9781101905005",
    "Six days ago, astronaut Mark Watney became one of the first people to walk on Mars.<br/>Now, he’s sure he’ll be the first person to die there.<br/>After a dust storm nearly kills him and forces his crew to evacuate while thinking him dead, Mark finds himself stranded and completely alone with no way to even signal Earth that he’s alive—and even if he could get word out, his supplies would be gone long before a rescue could arrive.<br/>Chances are, though, he won’t have time to starve to death. The damaged machinery, unforgiving environment, or plain-old “human error” are much more likely to kill him first.<br/>But Mark isn’t ready to give up yet. Drawing on his ingenuity, his engineering skills—and a relentless, dogged refusal to quit—he steadfastly confronts one seemingly insurmountable obstacle after the next. Will his resourcefulness be enough to overcome the impossible odds against him?"
).__dict__
the_martian['authors'].append(
    {"last_name": a_weir['last_name'],
     "first_name": a_weir['first_name']})
the_martian['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(the_martian)

ready_player_one = CreateBook(
    "Ready Player One",
    "https://images.penguinrandomhouse.com/cover/9780804190138",
    "In the year 2045, reality is an ugly place. The only time teenage Wade Watts really feels alive is when he’s jacked into the virtual utopia known as the OASIS. Wade’s devoted his life to studying the puzzles hidden within this world’s digital confines—puzzles that are based on their creator’s obsession with the pop culture of decades past and that promise massive power and fortune to whoever can unlock them.<br/>But when Wade stumbles upon the first clue, he finds himself beset by players willing to kill to take this ultimate prize. The race is on, and if Wade’s going to survive, he’ll have to win—and confront the real world he’s always been so desperate to escape."
).__dict__
ready_player_one['authors'].append(
    {"last_name": e_cline['last_name'],
     "first_name": e_cline['first_name']})
ready_player_one['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(ready_player_one)

armada = CreateBook(
    "Armada",
    "https://images.penguinrandomhouse.com/cover/9780804137270",
    "From the author of Ready Player One, a rollicking alien invasion thriller that embraces and subverts science-fiction conventions as only Ernest Cline can.<br/>Zack Lightman has never much cared for reality. He vastly prefers the countless science-fiction movies, books, and videogames he’s spent his life consuming. And too often, he catches himself wishing that some fantastic, impossible, world-altering event could arrive to whisk him off on a grand spacefaring adventure.<br/>So when he sees the flying saucer, he’s sure his years of escapism have finally tipped over into madness.<br/>Especially because the alien ship he’s staring at is straight out of his favorite videogame, a flight simulator callled Armada–in which gamers just happen to be protecting Earth from alien invaders.<br/>As impossible as it seems, what Zack’s seeing is all too real. And it’s just the first in a blur of revlations that will force him to question everything he thought he knew about Earth’s history, its future, even his own life–and to play the hero for real, with humanity’s life in the balance.<br/>But even through the terror and exhilaration, he can’t help thinking: Doesn’t something about this scenario feel a little bit like…well…fiction?<br/>At once reinventing and paying homage to science-fiction classics, Armada is a rollicking, surprising thriller, a coming-of-age adventure, and an alien invasion tale like nothing you’ve ever read before."
).__dict__
armada['authors'].append(
    {"last_name": e_cline['last_name'],
     "first_name": e_cline['first_name']})
armada['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(armada)

the_lost_world_a_novel = CreateBook(
    "The Lost World: A Novel",
    "https://images.penguinrandomhouse.com/cover/9780345538994",
    "It is now six years since the secret disaster at Jurassic Park, six years since the extraordinary dream of science and imagination came to a crashing end—the dinosaurs destroyed, the park dismantled, and the island indefinitely closed to the public.<br/>There are rumors that something has survived. . . .").__dict__
the_lost_world_a_novel['authors'].append(
    {"last_name": m_crichton['last_name'],
     "first_name": m_crichton['first_name']})
the_lost_world_a_novel['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(the_lost_world_a_novel)

terminal_man = CreateBook(
    "Terminal Man",
    "https://images.penguinrandomhouse.com/cover/9780804171298",
    "From the bestselling author of Jurassic Park, Timeline, and Sphere comes a neurological thriller about the dangers of cutting-edge medical experimentation.<br/>Harry Benson suffers from violent seizures. So violent that he often blackouts when they take hold. Shortly after severely beating two men during an episode, the police escort Benson to a Los Angeles hospital for treatment. There, Dr. Roger McPherson, head of the prestigious Neuropsychiatric Research Unit, is convinced he can cure Benson with an experimental procedure that would place electrodes deep in his brain’s pleasure centers, effectively short-circuiting Harry’s seizures with pulses of bliss. The surgery is successful, but while Benson is in recovery, he discovers how to trigger the pulses himself. To make matters worse his violent impulses have only grown, and he soon escapes the hospital with a deadly agenda. . ."
).__dict__
terminal_man['authors'].append(
    {"last_name": m_crichton['last_name'],
     "first_name": m_crichton['first_name']})
terminal_man['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(terminal_man)

jurassic_park = CreateBook(
    "Jurassic Park",
    "https://images.penguinrandomhouse.com/cover/9780345538987",
    "An astonishing technique for recovering and cloning dinosaur DNA has been discovered. Now humankind’s most thrilling fantasies have come true. Creatures extinct for eons roam Jurassic Park with their awesome presence and profound mystery, and all the world can visit them—for a price.<br/>Until something goes wrong. . . .<br/>In Jurassic Park, Michael Crichton taps all his mesmerizing talent and scientific brilliance to create his most electrifying technothriller."
).__dict__
jurassic_park['authors'].append(
    {"last_name": m_crichton['last_name'],
     "first_name": m_crichton['first_name']})
jurassic_park['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(jurassic_park)

the_blind_assassin = CreateBook(
    "The Blind Assassin",
    "https://images.penguinrandomhouse.com/cover/9780385720953",
    "In The Blind Assassin, Margaret Atwood weaves together strands of gothic suspense, romance, and science fiction into one utterly spellbinding narrative. The novel begins with the mysterious death—a possible suicide—of a young woman named Laura Chase in 1945. Decades later, Laura’s sister Iris recounts her memories of their childhood, and of the dramatic deaths that have punctuated their wealthy, eccentric family’s history. Intertwined with Iris’s account are chapters from the scandalous novel that made Laura famous, in which two illicit lovers amuse each other by spinning a tale of a blind killer on a distant planet. These richly layered stories-within-stories gradually illuminate the secrets that have long haunted the Chase family, coming together in a brilliant and astonishing final twist."
).__dict__
the_blind_assassin['authors'].append(
    {"last_name": m_atwood['last_name'],
     "first_name": m_atwood['first_name']})
the_blind_assassin['genres'].append({"type": g_science_fiction['type']})
book_catalog.append(the_blind_assassin)

marthas_american_food = CreateBook(
    "Martha’s American Food",
    "https://images.penguinrandomhouse.com/cover/9780307405081",
    "Martha Stewart, who has so significantly influenced the American table, collects her favorite national dishes–as well as the stories and traditions behind them–in this love letter to American food featuring 200 recipes.<br/>These are recipes that will delight you with nostalgia, inspire you, and teach you about our nation by way of its regions and their distinctive flavors. Above all, these are time-honored recipes that you will turn to again and again.").__dict__
marthas_american_food['authors'].append(
    {"last_name": m_stewart['last_name'],
     "first_name": m_stewart['first_name']})
marthas_american_food['genres'].append({"type": g_cooking['type']})
book_catalog.append(marthas_american_food)

martha_stewarts_appetizers = CreateBook(
    "Martha Stewart’s Appetizers",
    "https://images.penguinrandomhouse.com/cover/9780307954626",
    "With more than 200 recipes, successfully cook snacks, starters, small plates, stylish bites, and sips for any occasion.<br/>Hors d’oeuvres made modern: Today’s style of entertaining calls for fuss-free party foods that are easy to make and just as delicious as ever. With more than 200 recipes for tasty pre-dinner bites, substantial small plates, special-occasion finger foods, and quick snacks to enjoy with drinks, Martha Stewart’s Appetizers is the new go-to guide for any type of get-together.").__dict__
martha_stewarts_appetizers['authors'].append(
    {"last_name": m_stewart['last_name'],
     "first_name": m_stewart['first_name']})
martha_stewarts_appetizers['genres'].append({"type": g_cooking['type']})
book_catalog.append(martha_stewarts_appetizers)

go_tell_it_on_the_mountain = CreateBook(
    "Go Tell It on the Mountain",
    "https://images.penguinrandomhouse.com/cover/9780375701870",
    "“Mountain,” Baldwin said, “is the book I had to write if I was ever going to write anything else.” Go Tell It on the Mountain, originally published in 1953, is Baldwin’s first major work, a novel that has established itself as an American classic. With lyrical precision, psychological directness, resonating symbolic power, and a rage that is at once unrelenting and compassionate, Baldwin chronicles a fourteen-year-old boy’s discovery one Saturday in March of 1935 of the terms of his identity as the stepson of the minister of a Pentecostal storefront church in Harlem. Baldwin’s rendering of his protagonist’s spiritual, sexual, and moral struggle toward self-invention opened new possibilities in the American language and in the way Americans understand themselves."
).__dict__
go_tell_it_on_the_mountain['authors'].append(
    {"last_name": j_baldwin['last_name'],
     "first_name": j_baldwin['first_name']})
go_tell_it_on_the_mountain['genres'].append(
    {"type": g_literary_fiction['type']})
book_catalog.append(go_tell_it_on_the_mountain)

the_devil_finds_work = CreateBook(
    "The Devil Finds Work",
    "https://images.penguinrandomhouse.com/cover/9780307275950",
    "Baldwin’s personal reflections on movies gathered here in a book-length essay are also a probing appraisal of American racial politics. Offering an incisive look at racism in American movies and a vision of America’s self-delusions and deceptions, Baldwin challenges the underlying assumptions in such films as In the Heat of the Night, Guess Who’s Coming to Dinner, and The Exorcist. Here are our loves and hates, biases and cruelties, fears and ignorance reflected by the films that have entertained us and shaped our consciousness. And here too is the stunning prose of a writer whose passion never diminished his struggle for equality, justice, and social change."
).__dict__
the_devil_finds_work['authors'].append(
    {"last_name": j_baldwin['last_name'],
     "first_name": j_baldwin['first_name']})
the_devil_finds_work['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(the_devil_finds_work)

the_fire_next_time = CreateBook(
    "The Fire Next Time",
    "https://images.penguinrandomhouse.com/cover/9780679744726",
    "A national bestseller when it first appeared in 1963, The Fire Next Time galvanized the nation and gave passionate voice to the emerging civil rights movement. At once a powerful evocation of James Baldwin’s early life in Harlem and a disturbing examination of the consequences of racial injustice, the book is an intensely personal and provocative document. It consists of two “letters,” written on the occasion of the centennial of the Emancipation Proclamation, that exhort Americans, both black and white, to attack the terrible legacy of racism. Described by The New York Times Book Review as “sermon, ultimatum, confession, deposition, testament, and chronicle…all presented in searing, brilliant prose,” The Fire Next Time stands as a classic of our literature."
).__dict__
the_fire_next_time['authors'].append(
    {"last_name": j_baldwin['last_name'],
     "first_name": j_baldwin['first_name']})
the_fire_next_time['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(the_fire_next_time)

i_am_not_your_negro = CreateBook(
    "I Am Not Your Negro",
    "https://images.penguinrandomhouse.com/cover/9780525434696",
    "To compose his stunning documentary film I Am Not Your Negro, acclaimed filmmaker Raoul Peck mined James Baldwin’s published and unpublished oeuvre, selecting passages from his books, essays, letters, notes, and interviews that are every bit as incisive and pertinent now as they have ever been. Weaving these texts together, Peck brilliantly imagines the book that Baldwin never wrote. In his final years, Baldwin had envisioned a book about his three assassinated friends, Medgar Evers, Malcolm X, and Martin Luther King. His deeply personal notes for the project have never been published before. Peck’s film uses them to jump through time, juxtaposing Baldwin’s private words with his public statements, in a blazing examination of the tragic history of race in America."
).__dict__
i_am_not_your_negro['authors'].append(
    {"last_name": j_baldwin['last_name'],
     "first_name": j_baldwin['first_name']})
i_am_not_your_negro['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(i_am_not_your_negro)

giovannis_room = CreateBook(
    "Giovanni’s Room",
    "https://images.penguinrandomhouse.com/cover/9781101907740",
    "James Baldwin’s groundbreaking novel about love and the fear of love is set among the bohemian bars and nightclubs of 1950s Paris.<br/>David is a young American expatriate who has just proposed marriage to his girlfriend, Hella. While she is away on a trip, David meets a bartender named Giovanni to whom he is drawn in spite of himself. Soon the two are spending the night in Giovanni’s curtainless room, which he keeps dark to protect their privacy. But Hella’s return to Paris brings the affair to a crisis, one that rapidly spirals into tragedy. Caught between his repressed desires and conventional morality, David struggles for self-knowledge during one long, dark night—“the night which is leading me to the most terrible morning of my life.” With sharp, probing insight, Giovanni’s Room tells an impassioned, deeply moving story that lays bare the unspoken complexities of the human heart."
).__dict__
giovannis_room['authors'].append(
    {"last_name": j_baldwin['last_name'],
     "first_name": j_baldwin['first_name']})
giovannis_room['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(giovannis_room)

marcel_the_shell_the_most_surprised_ive_ever_been = CreateBook(
    "Marcel the Shell: the Most Surprised I’ve Ever Been",
                                                               "https://images.penguinrandomhouse.com/cover/9781595144560",
                                                               "One thing about a new day–you really never know where it will go, even if you know where it starts.<br/>Marcel the Shell with Shoes On is walking on the blanket when he is unexpectedly launched high into the air. Tumbling through space, the bird’s-eye view offers our small friend not only a glimpse of the important things in life–his beloved Nana who sleeps in a fancy French bread, a stinky shoe, and a monstrous baby–but also a much bigger picture. Sometimes the most wonderful discoveries are the ones we least expect.").__dict__
marcel_the_shell_the_most_surprised_ive_ever_been['authors'].append(
    {"last_name": j_slate['last_name'],
     "first_name": j_slate['first_name']})
marcel_the_shell_the_most_surprised_ive_ever_been['authors'].append(
    {"last_name": d_camp['last_name'],
     "first_name": d_camp['first_name']})
marcel_the_shell_the_most_surprised_ive_ever_been['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(marcel_the_shell_the_most_surprised_ive_ever_been)

marcel_the_shell_with_shoes_on = CreateBook(
    "Marcel the Shell with Shoes On",
    "https://images.penguinrandomhouse.com/cover/9781595144553",
    "Millions of people have fallen in love with Marcel. Now the tiny shell with shoes and a big heart is transitioning from online sensation to classic picture book character, and readers can learn more about this adorable creature and his wonderfully peculiar world.<br/>From wearing a lentil as a hat to hang-gliding on a Dorito, Marcel is able to find magic in the everyday. He may be small, but he knows he has a lot of good qualities. He may not be able to lift anything by himself, but when he needs help, he calls upon his family. He may never be able own a real dog . . . but he has a pretty awesome imagination.").__dict__
marcel_the_shell_with_shoes_on['authors'].append(
    {"last_name": j_slate['last_name'],
     "first_name": j_slate['first_name']})
marcel_the_shell_with_shoes_on['authors'].append(
    {"last_name": d_camp['last_name'],
     "first_name": d_camp['first_name']})
marcel_the_shell_with_shoes_on['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(marcel_the_shell_with_shoes_on)

horton_hatches_the_egg = CreateBook(
    "Horton Hatches the Egg",
    "https://images.penguinrandomhouse.com/cover/9780394800776",
    "Generations of children have fallen in love with Horton the elephant!<br/>“I meant what I said, and I said what I meant. . . .<br/>An elephant’s faithful, one hundred per cent!”<br/>Horton is kind and trustworthy, but unfortunately, the lazy bird Mayzie takes advantage of his good nature when she leaves Horton to watch her unhatched egg. Told with Dr. Seuss’s signature rhymes and trademark illustrations, this is a tale that will be enjoyed over and over, by reader and listener alike. And don’t miss another delightful tale about this beloved pachyderm: Horton Hears a Who!"
).__dict__
horton_hatches_the_egg['authors'].append(
    {"last_name": d_seuss['last_name'],
     "first_name": d_seuss['first_name']})
horton_hatches_the_egg['genres'].append({"type": g_children_picture['type']})
book_catalog.append(horton_hatches_the_egg)

green_eggs_and_ham = CreateBook(
    "Green Eggs and Ham",
    "https://images.penguinrandomhouse.com/cover/9780394800165",
    "“Do you like green eggs and ham?” asks Sam-I-am in this Beginner Book by Dr. Seuss. In a house or with a mouse? In a boat or with a goat? On a train or in a tree? Sam keeps asking persistently. With unmistakable characters and signature rhymes, Dr. Seuss’s beloved favorite has cemented its place as a children’s classic. In this most famous of cumulative tales, the list of places to enjoy green eggs and ham, and friends to enjoy them with, gets longer and longer. Follow Sam-I-am as he insists that this unusual treat is indeed a delectable snack to be savored everywhere and in every way.<br/>Originally created by Dr. Seuss, Beginner Books encourage children to read all by themselves, with simple words and illustrations that give clues to their meaning."
).__dict__
green_eggs_and_ham['authors'].append(
    {"last_name": d_seuss['last_name'],
     "first_name": d_seuss['first_name']})
green_eggs_and_ham['genres'].append({"type": g_children_picture['type']})
book_catalog.append(green_eggs_and_ham)

one_fish_two_fish_red_fish_blue_fish = CreateBook(
    "One Fish Two Fish Red Fish Blue Fish",
    "https://images.penguinrandomhouse.com/cover/9780394800134",
    "“From there to here, from here to there, funny things are everywhere” . . . So begins this classic Beginner Book by Dr. Seuss. Beginning with just five fish and continuing into flights of fancy, One Fish Two Fish Red Fish Blue Fish celebrates how much fun imagination can be. From the can-opening Zans to the boxing Gox to the winking Yink who drinks pink ink, the silly rhymes and colorful cast of characters create an entertaining approach to reading that will have every child giggling from morning to night: “Today is gone. Today was fun. Tomorrow is another one.”<br/>Originally created by Dr. Seuss, Beginner Books encourage children to read all by themselves, with simple words and illustrations that give clues to their meaning."
).__dict__
one_fish_two_fish_red_fish_blue_fish['authors'].append(
    {"last_name": d_seuss['last_name'],
     "first_name": d_seuss['first_name']})
one_fish_two_fish_red_fish_blue_fish['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(one_fish_two_fish_red_fish_blue_fish)

horton_and_the_kwuggerbug_and_more_lost_stories = CreateBook(
    "Horton and the Kwuggerbug and more Lost Stories",
    "https://images.penguinrandomhouse.com/cover/9780385382984",
    "A follow-up to The Bippolo Seed and Other Lost Stories by Dr. Seuss!<br/>A new Dr. Seuss book! This follow-up to The Bippolo Seed and Other Lost Stories features familiar Seussian faces and places—including Horton the Elephant, Marco, Mulberry Street, and a Grinch—as well as an introduction by renowned Seuss scholar Charles D. Cohen. Seuss fans will learn more about Horton’s integrity, Marco’s amazing imagination, a narrowly avoided disaster on Mullbery Street, and a devious Grinch. With a color palette enhanced beyond that of the magazines in which the stories originally appeared, this new volume of “lost” tales is a perfect gift for young readers and a must-have for Seuss collectors of all ages!").__dict__
horton_and_the_kwuggerbug_and_more_lost_stories['authors'].append(
    {"last_name": d_seuss['last_name'],
     "first_name": d_seuss['first_name']})
horton_and_the_kwuggerbug_and_more_lost_stories['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(horton_and_the_kwuggerbug_and_more_lost_stories)

daisy_head_mayzie = CreateBook(
    "Daisy-Head Mayzie",
    "https://images.penguinrandomhouse.com/cover/9780553539004",
    "Daisy goes back to her roots!<br/>Think you know Daisy-Head Mayzie? Think again! With all-new illustrations and a revised plot based on Dr. Seuss’s original screenplay and signature-style sketches, the timeless tale of Mayzie McGrew—a girl who suddenly sprouts a daisy from her head—is sweeter, funnier, and . . . well . . . more Seussian than ever!<br/>Some things, however, remain the same: In the same zany way that the Cat wreaks havoc in The Cat in the Hat, the darling blossom that springs from Mayzie’s head sets off a series of madcap reactions that will leave young readers (and their lucky parents) giggling with glee. An ideal comic choice for celebrating those qualities that make each of us unique, this brand-new edition of Daisy-Head Mayzie is perfect just the way it is!"
).__dict__
daisy_head_mayzie['authors'].append(
    {"last_name": d_seuss['last_name'],
     "first_name": d_seuss['first_name']})
daisy_head_mayzie['genres'].append({"type": g_children_picture['type']})
book_catalog.append(daisy_head_mayzie)

fox_in_socks = CreateBook(
    "Fox in Socks",
    "https://images.penguinrandomhouse.com/cover/9780553513363",
    "A beloved Bright and Early Board Book by Dr. Seuss, now in a larger trim size!<br/>A sturdy board book edition of Dr. Seuss’s Fox in Socks, now available in a bigger trim perfect for babies and toddlers! This abridged version of the classic Beginner Book features a tricky fox in socks and the progressively more difficult tongue-twisting games he plays on his exasperated friend Knox. Ideal for read-aloud, this beloved classic will have babies of all ages laughing with—and at—their parents as they struggle, like Knox, to blab such blibber blubber as muddle puddle tweetle poodle beetle noodle bottle paddle battle! A perfect gift for baby showers, birthdays, and happy occasions of all kinds!"
).__dict__
fox_in_socks['authors'].append(
    {"last_name": d_seuss['last_name'],
     "first_name": d_seuss['first_name']})
fox_in_socks['genres'].append({"type": g_children_picture['type']})
book_catalog.append(fox_in_socks)


assume_the_worst = CreateBook(
    "Assume the Worst",
    "https://images.penguinrandomhouse.com/cover/9780525655015",
    "This is Oh, the Places You’ll Never Go–the ultimate hilarious, cynical, but absolutely realistic view of a college graduate’s future. And what he or she can or can’t do about it.<br/>“This commencement address will never be given, because graduation speakers are supposed to offer encouragement and inspiration. That’s not what you need. You need a warning.”<br/>So begins Carl Hiaasen’s attempt to prepare young men and women for their future. And who better to warn them about their precarious paths forward than Carl Hiaasen? The answer, after reading Assume the Worst, is: Nobody.<br/>And who better to illustrate–and with those illustrations, expand upon and cement Hiaasen’s cynical point of view–than Roz Chast, best-selling author/illustrator and National Book Award winner? The answer again is easy: Nobody.<br/>Following the format of Anna Quindlen’s commencement address (Being Perfect) and George Saunders’s commencement address (Congratulations, by the way), the collaboration of Hiaasen and Chast might look typical from the outside, but inside it is anything but.<br/>This book is bound to be a classic, sold year after year come graduation time. Although it’s also a good gift for anyone starting a job, getting married, or recently released from prison. Because it is not just funny. It is, in its own Hiaasen way, extremely wise and even hopeful. Well, it might not be full of hope, but there are certainly enough slivers of the stuff in there to more than keep us all going."
).__dict__
assume_the_worst['authors'].append(
    {"last_name": c_hiaasen['last_name'],
     "first_name": c_hiaasen['first_name']})
assume_the_worst['authors'].append(
    {"last_name": r_chast['last_name'],
     "first_name": r_chast['first_name']})
assume_the_worst['genres'].append({"type": g_humor['type']})
assume_the_worst['genres'].append({"type": g_philosophy['type']})
book_catalog.append(assume_the_worst)

chomp = CreateBook(
    "Chomp",
    "https://images.penguinrandomhouse.com/cover/9780375868276",
    "The hysterical #1 New York Times bestseller from Newbery honoree Carl Hiaasen featuring gators, snakes, bats that bite, and reality show hosts gone wild!<br/>When Wahoo Cray’s dad—a professional animal wrangler—takes a job with a reality TV show called Expedition Survival!, Wahoo figures he’ll have to do a bit of wrangling himself to keep his father from killing Derek Badger, the show’s inept and egotistical star. But the job keeps getting more complicated: Derek Badger insists on using wild animals for his stunts; and Wahoo’s acquired a shadow named Tuna—a girl who’s sporting a shiner courtesy of her father and needs a place to hide out.<br/>They’ve only been on location in the Everglades for a day before Derek gets bitten by a bat and goes missing in a storm. Search parties head out and promptly get lost themselves. And then Tuna’s dad shows up with a gun . . .<br/>It’s anyone’s guess who will actually survive Expedition Survival. . . "
).__dict__
chomp['authors'].append(
    {"last_name": c_hiaasen['last_name'],
     "first_name": c_hiaasen['first_name']})
chomp['genres'].append({"type": g_children_picture['type']})
book_catalog.append(chomp)

razor_girl = CreateBook(
    "Razor Girl",
    "https://images.penguinrandomhouse.com/cover/9780345804907",
    "A lovable con woman and a disgraced detective team up to find a redneck reality TV star in this raucous and razor-sharp new novel from Carl Hiaasen, the bestselling author of Bad Monkey.<br/>Merry Mansfield, the eponymous Razor Girl, specializes in kidnapping for the mob. Her preferred method is rear-ending her targets and asking them for a ride. Her latest mark is Martin Trebeaux, owner of a private beach renourishment company who has delivered substandard sand to a mob hotel. But there’s just one problem: Razor Girl hits the wrong guy. Instead, she ends up with Lane Coolman, talent manager for Buck Nance, the star of a reality TV show about a family of Cajun rooster farmers. Buck Nance, left to perform standup at a Key West bar without his handler, makes enough off-color jokes to incite a brawl, then flees for his life and vanishes. "
).__dict__
razor_girl['authors'].append(
    {"last_name": c_hiaasen['last_name'],
     "first_name": c_hiaasen['first_name']})
razor_girl['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(razor_girl)

how_to_change_your_mind = CreateBook(
    "How to Change Your Mind",
    "https://images.penguinrandomhouse.com/cover/9781594204227",
    "The #1 New York Times bestseller.<br/>A brilliant and brave investigation into the medical and scientific revolution taking place around psychedelic drugs–and the spellbinding story of his own life-changing psychedelic experiences").__dict__
how_to_change_your_mind['authors'].append(
    {"last_name": m_pollan['last_name'],
     "first_name": m_pollan['first_name']})
how_to_change_your_mind['genres'].append({"type": g_philosophy['type']})
how_to_change_your_mind['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(how_to_change_your_mind)

the_female_persuasion = CreateBook(
    "The Female Persuasion",
    "https://images.penguinrandomhouse.com/cover/9781594488405",
    "Greer Kadetsky is a shy college freshman when she meets the woman she hopes will change her life. Faith Frank, dazzlingly persuasive and elegant at sixty-three, has been a central pillar of the women’s movement for decades, a figure who inspires others to influence the world. Upon hearing Faith speak for the first time, Greer—madly in love with her boyfriend, Cory, but still full of longing for an ambition that she can’t quite place—feels her inner world light up. And then, astonishingly, Faith invites Greer to make something out of that sense of purpose, leading Greer down the most exciting path of her life as it winds toward and away from her meant-to-be love story with Cory and the future she’d always imagined."
).__dict__
the_female_persuasion['authors'].append(
    {"last_name": m_wollitzer['last_name'],
     "first_name": m_wollitzer['first_name']})
the_female_persuasion['genres'].append({"type": g_womens_fiction['type']})
the_female_persuasion['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_female_persuasion)

the_underground_railroad = CreateBook(
    "The Underground Railroad",
    "https://images.penguinrandomhouse.com/cover/9780345804327",
    "Cora is a young slave on a cotton plantation in Georgia. An outcast even among her fellow Africans, she is on the cusp of womanhood—where greater pain awaits. And so when Caesar, a slave who has recently arrived from Virginia, urges her to join him on the Underground Railroad, she seizes the opportunity and escapes with him. In Colson Whitehead’s ingenious conception, the Underground Railroad is no mere metaphor: engineers and conductors operate a secret network of actual tracks and tunnels beneath the Southern soil. Cora embarks on a harrowing flight from one state to the next, encountering, like Gulliver, strange yet familiar iterations of her own world at each stop. As Whitehead brilliantly re-creates the terrors of the antebellum era, he weaves in the saga of our nation, from the brutal abduction of Africans to the unfulfilled promises of the present day. The Underground Railroad is both the gripping tale of one woman’s will to escape the horrors of bondage—and a powerful meditation on the history we all share."
).__dict__
the_underground_railroad['authors'].append(
    {"last_name": c_whitehead['last_name'],
     "first_name": c_whitehead['first_name']})
the_underground_railroad['genres'].append({"type": g_literary_fiction['type']})
the_underground_railroad['genres'].append(
    {"type": g_historical_fiction['type']})
book_catalog.append(the_underground_railroad)

sag_harbor = CreateBook(
    "Sag Harbor",
    "https://images.penguinrandomhouse.com/cover/9780307455161",
    "From the Pulitzer-Prize winning author of The Underground Railroad: a tender, hilarious, and supremely original novel about coming-of-age in the 80s.<br/>Benji Cooper is one of the few black students at an elite prep school in Manhattan. But every summer, Benji escapes to the Hamptons, to Sag Harbor, where a small community of African American professionals have built a world of their own.<br/>The summer of ’85 won’t be without its usual trials and tribulations, of course. There will be complicated new handshakes to fumble through and state-of-the-art profanity to master. Benji will be tested by contests big and small, by his misshapen haircut (which seems to have a will of its own), by the New Coke Tragedy, and by his secret Lite FM addiction. But maybe, just maybe, this summer might be one for the ages."
).__dict__
sag_harbor['authors'].append(
    {"last_name": c_whitehead['last_name'],
     "first_name": c_whitehead['first_name']})
sag_harbor['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(sag_harbor)

the_noble_hustle = CreateBook(
    "The Noble Hustle",
    "https://images.penguinrandomhouse.com/cover/9780345804334",
    "From the #1 New York Times bestselling author of The Underground Railroad<br/>In 2011, Grantland magazine gave bestselling novelist Colson Whitehead $10,000 to play at the World Series of Poker in Las Vegas. It was the assignment of a lifetime, except for one hitch—he’d never played in a casino tournament before. With just six weeks to train, our humble narrator took the Greyhound to Atlantic City to learn the ways of high-stakes Texas Hold’em.<br/>Poker culture, he discovered, is marked by joy, heartbreak, and grizzled veterans playing against teenage hotshots weaned on Internet gambling. Not to mention the not-to-be overlooked issue of coordinating Port Authority bus schedules with your kid’s drop-off and pickup at school. Finally arriving in Vegas for the multimillion-dollar tournament, Whitehead brilliantly details his progress, both literal and existential, through the event’s antes and turns, through its gritty moments of calculation, hope, and spectacle. Entertaining, ironic, and strangely profound, this epic search for meaning at the World Series of Poker is a sure bet."
).__dict__
the_noble_hustle['authors'].append(
    {"last_name": c_whitehead['last_name'],
     "first_name": c_whitehead['first_name']})
the_noble_hustle['genres'].append({"type": g_biography_memoir['type']})
the_noble_hustle['genres'].append({"type": g_humor['type']})
book_catalog.append(the_noble_hustle)

apex_hides_the_hurt = CreateBook(
    "Apex Hides the Hurt",
    "https://images.penguinrandomhouse.com/cover/9781400031269",
    "This New York Times Notable Book from the #1 New York Times bestselling author of The Underground Railroad is a brisk, comic tour de force about identity, history, and the adhesive bandage industry.<br/>The town of Winthrop has decided it needs a new name. The resident software millionaire wants to call it New Prospera; the mayor wants to return to the original choice of the founding black settlers; and the town’s aristocracy sees no reason to change the name at all. What they need, they realize, is a nomenclature consultant. And, it turns out, the consultant needs them. But in a culture overwhelmed by marketing, the name is everything and our hero’s efforts may result in not just a new name for the town but a new and subtler truth about it as well."
).__dict__
apex_hides_the_hurt['authors'].append(
    {"last_name": c_whitehead['last_name'],
     "first_name": c_whitehead['first_name']})
apex_hides_the_hurt['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(apex_hides_the_hurt)

you_cant_spell_america_without_me = CreateBook(
    "You Can’t Spell America Without Me",
    "https://images.penguinrandomhouse.com/cover/9780525521990",
    "Political satire as deeper truth: Donald Trump’s presidential memoir, as recorded by two world-renowned Trump scholars, and experts on greatness generally").__dict__
you_cant_spell_america_without_me['authors'].append(
    {"last_name": a_baldwin['last_name'],
     "first_name": a_baldwin['first_name']})
you_cant_spell_america_without_me['authors'].append(
    {"last_name": k_andersen['last_name'],
     "first_name": k_andersen['first_name']})
you_cant_spell_america_without_me['genres'].append({"type": g_humor['type']})
book_catalog.append(you_cant_spell_america_without_me)

dinner_in_an_instant = CreateBook(
    "Dinner in an Instant",
    "https://images.penguinrandomhouse.com/cover/9781524762964",
    "Dinner in an Instant gives home cooks recipes for elevated dinners that never sacrifice convenience. Beloved for her flawless recipes, Melissa Clark turns her imagination to the countertop appliances that have won American hearts from coast to coast. Recipes include Fresh Coconut Yogurt, Japanese Beef Curry, Osso Buco, Smoky Lentils, Green Persian Rice with Tahdig, and Lemon Verbena Crème Brulee.<br/>Dinner in an Instant provides instructions when possible for making the same dish on both the pressure cooker and slow cooker settings, allowing home cooks flexibility. Symbols guide the reader toward Paleo, Vegan, Vegetarian, and Gluten Free dinners."
).__dict__
dinner_in_an_instant['authors'].append(
    {"last_name": m_clark['last_name'],
     "first_name": m_clark['first_name']})
dinner_in_an_instant['genres'].append({"type": g_cooking['type']})
book_catalog.append(dinner_in_an_instant)

turtles_all_the_way_down = CreateBook(
    "Turtles All the Way Down",
    "https://images.penguinrandomhouse.com/cover/9780525555384",
    "It’s quite rare to find someone who sees the same world you see.<br/>Sixteen-year-old Aza never intended to pursue the mystery of fugitive billionaire Russell Pickett, but there’s a hundred-thousand-dollar reward at stake and her Best and Most Fearless Friend, Daisy, is eager to investigate. So together, they navigate the short distance and broad divides that separate them from Russell Pickett’s son, Davis.<br/>Aza is trying. She is trying to be a good daughter, a good friend, a good student, and maybe even a good detective, while also living within the ever-tightening spiral of her own thoughts.<br/>In his long-awaited return, John Green, the acclaimed, award-winning author of Looking for Alaska and The Fault in Our Stars, shares Aza’s story with shattering, unflinching clarity in this brilliant novel of love, resilience, and the power of lifelong friendship."
).__dict__
turtles_all_the_way_down['authors'].append(
    {"last_name": j_green['last_name'],
     "first_name": j_green['first_name']})
turtles_all_the_way_down['genres'].append({"type": g_teen_fiction['type']})
book_catalog.append(turtles_all_the_way_down)

grant = CreateBook(
    "Grant",
    "https://images.penguinrandomhouse.com/cover/9781594204876",
    "Pulitzer Prize winner Ron Chernow returns with a sweeping and dramatic portrait of one of our most compelling generals and presidents, Ulysses S. Grant.<br/>Ulysses S. Grant’s life has typically been misunderstood. All too often he is caricatured as a chronic loser and an inept businessman, or as the triumphant but brutal Union general of the Civil War. But these stereotypes don’t come close to capturing him, as Chernow shows in his masterful biography, the first to provide a complete understanding of the general and president whose fortunes rose and fell with dizzying speed and frequency."
).__dict__
grant['authors'].append(
    {"last_name": r_chernow['last_name'],
     "first_name": r_chernow['first_name']})
grant['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(grant)

endurance = CreateBook(
    "Endurance",
    "https://images.penguinrandomhouse.com/cover/9781524731595",
    "A stunning, personal memoir from the astronaut and modern-day hero who spent a record-breaking year aboard the International Space Station—a message of hope for the future that will inspire for generations to come.").__dict__
endurance['authors'].append(
    {"last_name": s_kelly['last_name'],
     "first_name": s_kelly['first_name']})
endurance['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(endurance)

power = CreateBook(
    "We Were Eight Years in Power",
    "https://images.penguinrandomhouse.com/cover/9780399590566",
    "“We were eight years in power” was the lament of Reconstruction-era black politicians as the American experiment in multiracial democracy ended with the return of white supremacist rule in the South. In this sweeping collection of new and selected essays, Ta-Nehisi Coates explores the tragic echoes of that history in our own time: the unprecedented election of a black president followed by a vicious backlash that fueled the election of the man Coates argues is America’s “first white president.”").__dict__
power['authors'].append(
    {"last_name": t_coates['last_name'],
     "first_name": t_coates['first_name']})
power['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(power)

between_world = CreateBook(
    "Between the World and Me",
    "https://images.penguinrandomhouse.com/cover/9780812993547",
    "In a profound work that pivots from the biggest questions about American history and ideals to the most intimate concerns of a father for his son, Ta-Nehisi Coates offers a powerful new framework for understanding our nation’s history and current crisis. Americans have built an empire on the idea of “race,” a falsehood that damages us all but falls most heavily on the bodies of black women and men—bodies exploited through slavery and segregation, and, today, threatened, locked up, and murdered out of all proportion. What is it like to inhabit a black body and find a way to live within it? And how can we all honestly reckon with this fraught history and free ourselves from its burden?"
).__dict__
between_world['authors'].append(
    {"last_name": t_coates['last_name'],
     "first_name": t_coates['first_name']})
between_world['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(between_world)

the_purloining_of_prince_oleomargarine = CreateBook(
    "The Purloining of Prince Oleomargarine",
    "https://images.penguinrandomhouse.com/cover/9780553523225",
    "A never-before-published, previously unfinished Mark Twain children’s story is brought to life by Philip and Erin Stead, creators of the Caldecott Medal-winning A Sick Day for Amos McGee.<br/>In a hotel in Paris one evening in 1879, Mark Twain sat with his young daughters, who begged their father for a story. Twain began telling them the tale of Johnny, a poor boy in possession of some magical seeds. Later, Twain would jot down some rough notes about the story, but the tale was left unfinished . . . until now.").__dict__
the_purloining_of_prince_oleomargarine['authors'].append(
    {"last_name": m_twain['last_name'],
     "first_name": m_twain['first_name']})
the_purloining_of_prince_oleomargarine['authors'].append(
    {"last_name": p_stead['last_name'],
     "first_name": p_stead['first_name']})
the_purloining_of_prince_oleomargarine['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(the_purloining_of_prince_oleomargarine)

little_fires_everywhere = CreateBook(
    "Little Fires Everywhere",
    "https://images.penguinrandomhouse.com/cover/9780735224292",
    "From the bestselling author of Everything I Never Told You, a riveting novel that traces the intertwined fates of the picture-perfect Richardson family and the enigmatic mother and daughter who upend their lives.<br/>In Shaker Heights, a placid, progressive suburb of Cleveland, everything is planned – from the layout of the winding roads, to the colors of the houses, to the successful lives its residents will go on to lead. And no one embodies this spirit more than Elena Richardson, whose guiding principle is playing by the rules.").__dict__
little_fires_everywhere['authors'].append(
    {"last_name": c_ng['last_name'],
     "first_name": c_ng['first_name']})
little_fires_everywhere['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(little_fires_everywhere)

everything_i_never_told_you = CreateBook(
    "Everything I Never Told You",
    "https://images.penguinrandomhouse.com/cover/9780143127550",
    "“Lydia is dead. But they don’t know this yet.” So begins this exquisite novel about a Chinese American family living in 1970s small-town Ohio. Lydia is the favorite child of Marilyn and James Lee, and her parents are determined that she will fulfill the dreams they were unable to pursue. But when Lydia’s body is found in the local lake, the delicate balancing act that has been keeping the Lee family together is destroyed, tumbling them into chaos. A profoundly moving story of family, secrets, and longing, Everything I Never Told You is both a gripping page-turner and a sensitive family portrait, uncovering the ways in which mothers and daughters, fathers and sons, and husbands and wives struggle, all their lives, to understand one another."
).__dict__
everything_i_never_told_you['authors'].append(
    {"last_name": c_ng['last_name'],
     "first_name": c_ng['first_name']})
everything_i_never_told_you['genres'].append(
    {"type": g_literary_fiction['type']})
book_catalog.append(everything_i_never_told_you)

autumn = CreateBook(
    "Autumn",
    "https://images.penguinrandomhouse.com/cover/9780399563300",
    "From the author of the monumental My Struggle series, Karl Ove Knausgaard, one of the masters of contemporary literature and a genius of observation and introspection, comes the first in a new autobiographical quartet based on the four seasons.").__dict__
autumn['authors'].append(
    {"last_name": k_knausgaard['last_name'],
     "first_name": k_knausgaard['first_name']})
autumn['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(autumn)

girls_who_code = CreateBook(
    "Girls Who Code",
    "https://images.penguinrandomhouse.com/cover/9780425287552",
    "Part how-to, part girl-empowerment, and all fun, from the leader of the movement championed by Sheryl Sandberg, Malala Yousafzai, and John Legend.<br/>Since 2012, the organization Girls Who Code has taught computing skills to and inspired over 40,000 girls across America. Now its founder, Reshma Saujani, wants to inspire you to be a girl who codes! Bursting with dynamic artwork, down-to-earth explanations of coding principles, and real-life stories of girls and women working at places like Pixar and NASA, this graphically animated book shows what a huge role computer science plays in our lives and how much fun it can be. No matter your interest—sports, the arts, baking, student government, social justice—coding can help you do what you love and make your dreams come true. Whether you’re a girl who’s never coded before, a girl who codes, or a parent raising one, this entertaining book, printed in bold two-color and featuring art on every page, will have you itching to create your own apps, games, and robots to make the world a better place."
).__dict__
girls_who_code['authors'].append(
    {"last_name": r_saujani['last_name'],
     "first_name": r_saujani['first_name']})
girls_who_code['genres'].append({"type": g_children_picture['type']})
book_catalog.append(girls_who_code)

behold_the_dreamers = CreateBook(
    "Behold the Dreamers",
    "https://images.penguinrandomhouse.com/cover/9780525509714",
    "Jende Jonga, a Cameroonian immigrant living in Harlem, has come to the United States to provide a better life for himself, his wife, Neni, and their six-year-old son. In the fall of 2007, Jende can hardly believe his luck when he lands a job as a chauffeur for Clark Edwards, a senior executive at Lehman Brothers. Clark demands punctuality, discretion, and loyalty—and Jende is eager to please. Clark’s wife, Cindy, even offers Neni temporary work at the Edwardses’ summer home in the Hamptons. With these opportunities, Jende and Neni can at last gain a foothold in America and imagine a brighter future."
).__dict__
behold_the_dreamers['authors'].append(
    {"last_name": i_mbue['last_name'],
     "first_name": i_mbue['first_name']})
behold_the_dreamers['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(behold_the_dreamers)

dragons_love_tacos = CreateBook(
    "Dragons Love Tacos",
    "https://images.penguinrandomhouse.com/cover/9780803736801",
    "A #1 New York Times bestselling phenomenon, this deliciously funny read-aloud from the creators of Robo-Sauce and Secret Pizza Party will make you laugh until spicy salsa comes out of your nose.<br/>Dragons love tacos. They love chicken tacos, beef tacos, great big tacos, and teeny tiny tacos. So if you want to lure a bunch of dragons to your party, you should definitely serve tacos. Buckets and buckets of tacos. Unfortunately, where there are tacos, there is also salsa. And if a dragon accidentally eats spicy salsa . . . oh, boy. You’re in red-hot trouble."
).__dict__
dragons_love_tacos['authors'].append(
    {"last_name": a_rubin['last_name'],
     "first_name": a_rubin['first_name']})
dragons_love_tacos['authors'].append(
    {"last_name": d_salmieri['last_name'],
     "first_name": d_salmieri['first_name']})
dragons_love_tacos['genres'].append({"type": g_children_picture['type']})
book_catalog.append(dragons_love_tacos)

dragons_love_tacos_2 = CreateBook(
    "Dragons Love Tacos 2: The Sequel",
    "https://images.penguinrandomhouse.com/cover/9780525428886",
    "The hilarious sequel to the smokin’ hot New York Times best seller, perfect for story time<br/>News alert! It has just been discovered that there are NO MORE TACOS left anywhere in the world. This is a huge problem because, as you know, dragons love tacos. If only there was a way for the dragons to travel back in time, to before tacos went extinct. Then they could grab lots of tacos and bring them back! It’s the perfect plan, as long as there’s no spicy salsa. You remember what happened last time . . .<br/>The award-winning creators of Robo-Sauce and Secret Pizza Party return with a gut-bustingly hilarious companion to the bestselling phenomenon Dragons Love Tacos."
).__dict__
dragons_love_tacos_2['authors'].append(
    {"last_name": a_rubin['last_name'],
     "first_name": a_rubin['first_name']})
dragons_love_tacos_2['authors'].append(
    {"last_name": d_salmieri['last_name'],
     "first_name": d_salmieri['first_name']})
dragons_love_tacos_2['genres'].append({"type": g_children_picture['type']})
book_catalog.append(dragons_love_tacos_2)

robo_sauce = CreateBook(
    "Robo-Sauce",
    "https://images.penguinrandomhouse.com/cover/9780525428879",
    "Fans of the best-selling Dragons Love Tacos will devour Adam Rubin and Daniel Salmieri’s newest story, a hilarious picture book about robots that magically transforms into a super shiny metal ROBO-BOOK.<br/>FACT: Robots are awesome. They have lasers for eyes, rockets for feet, and supercomputers for brains! Plus, robots never have to eat steamed beans or take baths, or go to bed. If only there were some sort of magical “Robo-Sauce” that turned squishy little humans into giant awesome robots… Well, now there is."
).__dict__
robo_sauce['authors'].append(
    {"last_name": a_rubin['last_name'],
     "first_name": a_rubin['first_name']})
robo_sauce['authors'].append(
    {"last_name": d_salmieri['last_name'],
     "first_name": d_salmieri['first_name']})
robo_sauce['genres'].append({"type": g_children_picture['type']})
book_catalog.append(robo_sauce)

south_and_west = CreateBook(
    "South and West",
    "https://images.penguinrandomhouse.com/cover/9780525434191",
    "Joan Didion has always kept notebooks—of overheard dialogue, interviews, drafts of essays, copies of articles. South and West gives us two extended excerpts from notebooks she kept in the 1970s; read together, they form a piercing view of the American political and cultural landscape.<br/>“Notes on the South” traces a road trip that she and her husband, John Gregory Dunne, took through Louisiana, Mississippi, and Alabama. Her acute observations about the small towns they pass through, her interviews with local figures, and their preoccupation with race, class, and heritage suggest a South largely unchanged today. “California Notes” began as an assignment from Rolling Stone on the Patty Hearst trial. Though Didion never wrote the piece, the time she spent watching the trial in San Francisco triggered thoughts about the West and her own upbringing in Sacramento. Here we not only see Didion’s signature irony and imagination in play, we’re also granted an illuminating glimpse into her mind and process."
).__dict__
south_and_west['authors'].append(
    {"last_name": j_didion['last_name'],
     "first_name": j_didion['first_name']})
south_and_west['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(south_and_west)

democracy = CreateBook(
    "Democracy",
    "https://images.penguinrandomhouse.com/cover/9780679754855",
    "Inez Victor knows that the major casualty of the political life is memory. But the people around Inez have made careers out of losing track. Her senator husband wants to forget the failure of his last bid for the presidency. Her husband’s handler would like the press to forget that Inez’s father is a murderer. And, in 1975, the year in which much of this bitterly funny novel is set, America is doing its best to lose track of its one-time client, the lethally hemorrhaging republic of South Vietnam.As conceived by Joan Didion, these personages and events constitute the terminal fallout of democracy, a fallout that also includes fact-finding junkets, senatorial groupies, the international arms market, and the Orwellian newspeak of the political class. Moving deftly from Honolulu to Jakarta, between romance, farce, and tragedy, Democracy is a tour de force from a writer who can dissect an entire society with a single phrase."
).__dict__
democracy['authors'].append(
    {"last_name": j_didion['last_name'],
     "first_name": j_didion['first_name']})
democracy['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(democracy)

where_i_was_from = CreateBook(
    "Where I Was From",
    "https://images.penguinrandomhouse.com/cover/9780679752868",
    "In her moving and insightful new book, Joan Didion reassesses parts of her life, her work, her history and ours. A native Californian, Didion applies her scalpel-like intelligence to the state’s ethic of ruthless self-sufficiency in order to examine that ethic’s often tenuous relationship to reality.<br/>Combining history and reportage, memoir and literary criticism, Where I Was From explores California’s romances with land and water; its unacknowledged debts to railroads, aerospace, and big government; the disjunction between its code of individualism and its fetish for prisons. Whether she is writing about her pioneer ancestors or privileged sexual predators, robber barons or writers (not excluding herself), Didion is an unparalleled observer, and her book is at once intellectually provocative and deeply personal."
).__dict__
where_i_was_from['authors'].append(
    {"last_name": j_didion['last_name'],
     "first_name": j_didion['first_name']})
where_i_was_from['genres'].append({"type": g_biography_memoir['type']})
book_catalog.append(where_i_was_from)

alton_brown_everydaycook = CreateBook(
    "Alton Brown: EveryDayCook",
    "https://images.penguinrandomhouse.com/cover/9781101885710",
    "My name is Alton Brown, and I wrote this book. It’s my first in a few years because I’ve been a little busy with TV stuff and interwebs stuff and live stage show stuff. Sure, I’ve been cooking, but it’s been mostly to feed myself and people in my immediate vicinity—which is really what a cook is supposed to do, right? Well, one day I was sitting around trying to organize my recipes, and I realized that I should put them into a personal collection. One thing led to another, and here’s EveryDayCook. There’s still plenty of science and hopefully some humor in here (my agent says that’s my “wheelhouse”), but unlike in my other books, a lot of attention went into the photos, which were all taken on my iPhone (take that, Instagram) and are suitable for framing. As for the recipes, which are arranged by time of day, they’re pretty darned tasty."
).__dict__
alton_brown_everydaycook['authors'].append(
    {"last_name": a_brown['last_name'],
     "first_name": a_brown['first_name']})
alton_brown_everydaycook['genres'].append({"type": g_cooking['type']})
book_catalog.append(alton_brown_everydaycook)


lidias_mastering_the_art_of_italian_cuisine = CreateBook(
    "Lidia’s Mastering the Art of Italian Cuisine",
    "https://images.penguinrandomhouse.com/cover/9780385349468",
    "From the Emmy-winning host of Lidia’s Kitchen, best-selling author, and beloved ambassador for Italian culinary traditions in America comes the ultimate master class: a beautifully produced definitive guide to Italian cooking, coauthored with her daughter, Tanya—covering everything from ingredients to techniques to tools, plus more than 400 delectable recipes.<br/>Teaching has always been Lidia’s passion, and in this magnificent book she gives us the full benefit of that passion and of her deep, comprehensive understanding of what it takes to create delicious Italian meals. With this book, readers will learn all the techniques needed to master Italian cooking. Lidia introduces us to the full range of standard ingredients—meats and fish, vegetables and fruits, grains, spices and condiments—and how to buy, store, clean, and cook with them. The 400 recipes run the full gamut from classics like risotto alla milanese and Tagliatelle with Mushroom Sauce to Lidia’s always-satisfying originals like Bread and Prune Gnocchi and Beet Ravioli in Poppy Seed Sauce. She gives us a comprehensive guide to the tools every kitchen should have to produce the best results. And she has even included a glossary of cuisine-related words and phrases that will prove indispensable for cooking, as well as for traveling and dining in Italy. There is no other book like this; it is the one book on Italian cuisine that every cook will need."
).__dict__
lidias_mastering_the_art_of_italian_cuisine['authors'].append(
    {"last_name": l_bastianich['last_name'],
     "first_name": l_bastianich['first_name']})
lidias_mastering_the_art_of_italian_cuisine['authors'].append(
    {"last_name": t_manuali['last_name'],
     "first_name": t_manuali['first_name']})
lidias_mastering_the_art_of_italian_cuisine['genres'].append(
    {"type": g_cooking['type']})
book_catalog.append(lidias_mastering_the_art_of_italian_cuisine)

lidias_italy_in_america = CreateBook(
    "Lidia’s Italy in America",
    "https://images.penguinrandomhouse.com/cover/9780385349468",
    "From one of America’s most beloved chefs and authors, a road trip into the heart of Italian American cooking today—from Chicago deep-dish pizza to the Bronx’s eggplant parm—celebrating the communities that redefined what we know as Italian food.<br/>As she explores this utterly delectable and distinctive cuisine, Lidia shows us that every kitchen is different, every Italian community distinct, and little clues are buried in each dish: the Sicilian-style semolina bread and briny olives in New Orleans Muffuletta Sandwiches, the Neapolitan crust of New York pizza, and mushrooms (abundant in the United States, but scarce in Italy) stuffed with breadcrumbs, just as peppers or tomatoes are. Lidia shows us how this cuisine is an original American creation and gives recognition where it is long overdue to the many industrious Italians across the country who have honored the traditions of their homeland in a delicious new style."
).__dict__
lidias_italy_in_america['authors'].append(
    {"last_name": l_bastianich['last_name'],
     "first_name": l_bastianich['first_name']})
lidias_italy_in_america['authors'].append(
    {"last_name": t_manuali['last_name'],
     "first_name": t_manuali['first_name']})
lidias_italy_in_america['genres'].append({"type": g_cooking['type']})
book_catalog.append(lidias_italy_in_america)

lidias_family_table = CreateBook(
    "Lidia’s Family Table",
    "https://images.penguinrandomhouse.com/cover/9781400040353",
    "From one of America best-loved and most-admired chefs, an instructive and creative collection of over 200 recipes that bring simple, delicious Italian cooking to the family table, with imaginative ideas for variations and improvisations.<br/>Lidia’s Family Table features hundreds of fabulous new dishes that will appeal both to Lidia’s loyal following, who have come to rely on her wonderfully detailed recipes, and to the more adventurous cook ready to experiment.").__dict__
lidias_family_table['authors'].append(
    {"last_name": l_bastianich['last_name'],
     "first_name": l_bastianich['first_name']})
lidias_family_table['genres'].append({"type": g_cooking['type']})
book_catalog.append(lidias_family_table)

llama_llama_i_love_you = CreateBook(
    "Llama Llama I Love You",
    "https://images.penguinrandomhouse.com/cover/9780698156517",
    "Nothing could be sweeter than Valentine’s Day with Llama Llama! Llama Llama shows his friends and family how much he loves them with heart-shaped cards and lots of hugs.").__dict__
llama_llama_i_love_you['authors'].append(
    {"last_name": a_dewdney['last_name'],
     "first_name": a_dewdney['first_name']})
llama_llama_i_love_you['genres'].append({"type": g_children_picture['type']})
book_catalog.append(llama_llama_i_love_you)

llama_llama_loves_to_read = CreateBook(
    "Llama Llama Loves to Read",
    "https://images.penguinrandomhouse.com/cover/9780670013975",
    "Anna Dewdney’s Bestselling Llama Llama series continues with Llama learning to read!<br/>Anna Dewdney’s beloved Llama Llama is growing up and learning to read! Throughout the school day, the teacher helps Llama Llama and the other children practice their letters, shows word cards, reads stories, and brings them to the library where they can all choose a favorite book. By the end of the day, Llama Llama is recognizing words and can’t wait to show Mama Llama that he’s becoming a reader!").__dict__
llama_llama_loves_to_read['authors'].append(
    {"last_name": a_dewdney['last_name'],
     "first_name": a_dewdney['first_name']})
llama_llama_loves_to_read['authors'].append(
    {"last_name": r_duncan['last_name'],
     "first_name": r_duncan['first_name']})
llama_llama_loves_to_read['genres'].append(
    {"type": g_children_picture['type']})
book_catalog.append(llama_llama_loves_to_read)

hag_seed = CreateBook(
    "Hag-Seed",
    "https://images.penguinrandomhouse.com/cover/9780804141314",
    "William Shakespeare’s The Tempest retold as Hag-Seed<br/>Felix is at the top of his game as Artistic Director of the Makeshiweg Theatre Festival. His productions have amazed and confounded. Now he’s staging a Tempest like no other: not only will it boost his reputation, it will heal emotional wounds.<br/>Or that was the plan. Instead, after an act of unforeseen treachery, Felix is living in exile in a backwoods hovel, haunted by memories of his beloved lost daughter, Miranda. And also brewing revenge.<br/>After twelve years, revenge finally arrives in the shape of a theatre course at a nearby prison. Here, Felix and his inmate actors will put on his Tempest and snare the traitors who destroyed him. It’s magic! But will it remake Felix as his enemies fall?"
).__dict__
hag_seed['authors'].append(
    {"last_name": m_atwood['last_name'],
     "first_name": m_atwood['first_name']})
hag_seed['genres'].append({"type": g_literary_fiction['type']})
hag_seed['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(hag_seed)

the_tent = CreateBook(
    "The Tent",
    "https://images.penguinrandomhouse.com/cover/9781400097012",
    "A delightful mélange of short fiction, here the Booker Prize-winning author pushes against form once again, with meditations on warlords, pet heaven, and aging homemakers. In these pieces, Margaret Atwood gives a sly pep talk to the ambitious young; writes about the disconcerting experience of looking at old photos of ourselves; and examines the boons and banes of orphanhood. Accompanied by her own playful illustrations, Atwood’s droll humor and keen insight make each piece full of clarity and grace. Prescient and personal, delectable and tart, The Tent reflects one of our wittiest authors at her best."
).__dict__
the_tent['authors'].append(
    {"last_name": m_atwood['last_name'],
     "first_name": m_atwood['first_name']})
the_tent['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_tent)

moral_disorder = CreateBook(
    "Moral Disorder",
    "https://images.penguinrandomhouse.com/cover/9780385721646",
    "A brilliant collection of connected short stories following the life of a single woman, from the #1 New York Times bestselling author of The Handmaid’s Tale.<br/>In these eleven tales, Margaret Atwood brings to life the story of one remarkable character, following her from girlhood in the 1930s, through her coming-of-age in the 50s and 60s, and into the present day where, no longer young, she reflects on the new state of the world. Each story focuses on the ways relationships transform a life: a woman’s complex love for a married man, the grief upon the death of parents and the joy with the birth of children, and the realization of what growing old with someone you love really means. By turns funny, lyrical, incisive, earthy, shocking, and deeply personal, Moral Disorder displays Atwood’s celebrated storytelling gifts and unmistakable style to their best advantage."
).__dict__
moral_disorder['authors'].append(
    {"last_name": m_atwood['last_name'],
     "first_name": m_atwood['first_name']})
moral_disorder['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(moral_disorder)

good_bones_and_simple_murders = CreateBook(
    "Good Bones and Simple Murders",
    "https://images.penguinrandomhouse.com/cover/9780307798534",
    "In this collection of short works that defy easy  categorization, Margaret Atwood displays, in  condensed and crystallized form, the trademark wit and  viruosity of her best-selling novels, brilliant  stories, and insightful poetry. Among the jewels  gathered here are Gertrude offering Hamlet a piece  of her mind, the real truth about the Little Red  Hen, a reincarnated bat explaining how Bram Stoker  got Dracula all wrong, and the  five methods of making a man (such as the  \"Traditional Method\": \"Take some dust off  the ground. Form. Breathe into the nostrils the  breath of life. Simple, but effective!\")  There are parables, monologues, prose poems, condensed  science fiction, reconfigured fairy tales, and  other miniature masterpieces–punctuated with  charming illustrations by the author. A must for her  fans, and a wonderful gift for all who savor the art  of exquisite prose, Good Bones And Simple  Murders marks the first time these  writings have been available in a trade edition in the  United States."
).__dict__
good_bones_and_simple_murders['authors'].append(
    {"last_name": m_atwood['last_name'],
     "first_name": m_atwood['first_name']})
good_bones_and_simple_murders['genres'].append(
    {"type": g_literary_fiction['type']})
book_catalog.append(good_bones_and_simple_murders)

heroes_of_the_frontier = CreateBook(
    "Heroes of the Frontier",
    "https://images.penguinrandomhouse.com/cover/9781101974636",
    "Josie and her children’s father have split up, she’s been sued by a former patient and lost her dental practice, and she’s grieving the death of a young man senselessly killed shortly after enlisting. When her ex asks to take the children to meet his new fiancée’s family, Josie makes a run for it to Alaska with her kids, Paul and Ana. At first their trip feels like a vacation: they see bears and bison, they eat hot dogs cooked on a bonfire, and they spend nights parked along icy cold rivers in dark forests. But as they drive in their rattling old RV, pushed north by the ubiquitous wildfires, Josie is chased by enemies both real and imagined, and past mistakes pursue her tiny family, even to the very edge of civilization. A captivating, often hilarious novel of family, loss, wilderness, and the curse of a violent America, Heroes of the Frontier is a powerful examination of our contemporary life and a rousing story of adventure."
).__dict__
heroes_of_the_frontier['authors'].append(
    {"last_name": d_eggers['last_name'],
     "first_name": d_eggers['first_name']})
heroes_of_the_frontier['genres'].append({"type": g_womens_fiction['type']})
book_catalog.append(heroes_of_the_frontier)

the_circle = CreateBook(
    "The Circle",
    "https://images.penguinrandomhouse.com/cover/9780345807298",  # NOQA
    "Now a Major Motion Picture starring Emma Watson and Tom Hanks. A bestselling dystopian novel that tackles surveillance, privacy and the frightening intrusions of technology in our lives.<br/>When Mae Holland is hired to work for the Circle, the world’s most powerful internet company, she feels she’s been given the opportunity of a lifetime. The Circle, run out of a sprawling California campus, links users’ personal emails, social media, banking, and purchasing with their universal operating system, resulting in one online identity and a new age of civility and transparency. As Mae tours the open-plan office spaces, the towering glass dining facilities, the cozy dorms for those who spend nights at work, she is thrilled with the company’s modernity and activity. There are parties that last through the night, there are famous musicians playing on the lawn, there are athletic activities and clubs and brunches, and even an aquarium of rare fish retrieved from the Marianas Trench by the CEO. Mae can’t believe her luck, her great fortune to work for the most influential company in the world—even as life beyond the campus grows distant, even as a strange encounter with a colleague leaves her shaken, even as her role at the Circle becomes increasingly public. What begins as the captivating story of one woman’s ambition and idealism soon becomes a heart-racing novel of suspense, raising questions about memory, history, privacy, democracy, and the limits of human knowledge.").__dict__
the_circle['authors'].append(
    {"last_name": d_eggers['last_name'],
     "first_name": d_eggers['first_name']})
the_circle['genres'].append({"type": g_literary_fiction['type']})
book_catalog.append(the_circle)


def add_book(book):
    new_book = Book(title=book['title'], cover=book['cover'],
                    description=book['description'])
    session.add(new_book)
    session.commit()

    for genre in book['genres']:
        try:
            genre_search = session.query(Genre).filter_by(
                type=genre['type']).first()
            if not genre_search:
                new_genre = Genre(type=genre['type'])
                session.add(new_genre)
                session.commit()
                genre_search = session.query(Genre).filter_by(
                    type=genre['type']).first()
            new_book.genres.append(genre_search)
        except Exception as e:
            print "{}: {}".format(genre['type'], e)

    for author in book['authors']:
        try:
            author_search = session.query(Author).filter_by(
                last_name=author['last_name'], first_name=author['first_name']).first()
            new_book.authors.append(author_search)
            session.commit()
            print "Added {} to {}".format(author_search.last_name, new_book.title)
        except Exception as e:
            print "{} {}: {}".format(author['first_name'], author['last_name'], e)


def add_genres(genres):
    """Add genre types to the database
    Arguments: Takes a single string or list of multiple genre types
    """
    for genre in genres:
        new_genre = Genre(type=genre['type'])
        session.add(new_genre)
        session.commit()


def add_authors(authors):
    """Add authors to the database
    Arguments: Takes a list of authors
    """
    for author in authors:
        new_author = Author(
            last_name=author['last_name'],
            first_name=author['first_name'],
            bio=author['bio'])
        session.add(new_author)
        session.commit()


if __name__ == '__main__':
    # Add genre categories to the database
    add_genres(genre_catalog)
    print "Added genres, woot woot!"

    # Add authors to the database
    add_authors(author_catalog)
    print "Added authors, woot woot!"

    # Add books to the database
    for book in book_catalog:
        add_book(book)
    print "Added books, woot woot!"
