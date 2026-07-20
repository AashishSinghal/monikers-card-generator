# Monikers OCR proofreading — review

- Corrections applied: **183**
- Uncertain (needs your eyes): **76**
- Rejected by guardrail (left as original): **0**

Names are shown as `Person`; clue text as `Text`. ~~struck~~ = removed, **bold** = added.

---
## Applied corrections

**#0 · Doge · Text**  
An Internet meme that shows a Shiba ~~lnu~~ **Inu** surrounded by colorful Comic Sans text that describes its inner monologue, such as "Wow." "Concern," and "so scare.'' There is much confuse over the name's pronunciation, yet it was recently used to brand a ~~Bitcoln~~ **Bitcoin** competitor.
  - `Shiba lnu` → `Shiba Inu` — lowercase l misread for capital I (Shiba Inu breed)
  - `Bitcoln` → `Bitcoin` — lowercase l misread for capital I

**#3 · Blacula · Text**  
The title character from a horror film about an 18th century African prince turned vampire. ~~locked~~ **Locked** in a coffin for two centuries by Count Dracula, the box was purchased as part of an estate by two interior decorators who accidentally set him loose in 70s Los Angeles.
  - `vampire. locked` → `vampire. Locked` — lost capital at sentence start after '. '

**#6 · A Furry · Text**  
A person who wears a full body animal suit, often for conventions, roleplaying, or personal recreation. Their use in ~~sexua I~~ **sexual** activity is a controversial topic in the community. In a recent survey, 37% reported that it was an important part of their interest in the activity.
  - `sexua I activity` → `sexual activity` — word wrongly split; 'l' scanned as separate 'I'

**#7 · Gallagher · Text**  
A prop comic famous for smashing watermelons with his trademark ~~Sledge-0-Matic.~~ **Sledge-O-Matic.** He once sued his brother for touring under the comedian's name and walked out of a Marc Maron interview when asked about the use of racist, homophobic, and xenophobic slurs in his act.
  - `Sledge-0-Matic` → `Sledge-O-Matic` — digit 0 misread for letter O

**#8 · Kobayashi · Text**  
A Japanese competitive eater who shocked the world in 2001 by eating 50 hot dogs and buns ~~(HOB)~~ **(HDB)** in 12 minutes at Nathan's Hot Dog Eating Contest, doubling the previous record. He once lost a hot dog eating contest (no buns) to a 1089 lb. Kodiak bear (31-50).
  - `(HOB)` → `(HDB)` — standard abbreviation for Hot Dogs and Buns is HDB; D likely scanned as O

**#10 · Sylvia Plath · Text**  
Poet, author, and wife of Ted Hughes, who was known for her confessional style of poetry as well as her novel The Bell Jar. She had a history of depression, leading to her suicide at 30 from carbon monoxide poisoning after sticking her head ~~Into~~ **into** an ~~un llt~~ **unlit** oven.
  - `un llt oven` → `unlit oven` — word wrongly split and 'i' scanned as 'l'
  - `head
Into` → `head
into` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#12 · Pablo Escobar · Text**  
A Colombian drug lord and "King of Cocaine," who at his peak trafficked 15 tons of the drug into the US per year. He was killed by authorities in a firefight in ~~Medellfn.~~ **Medellín.** According to a recent BBC report, a number of hippos from his menagerie still roam the Colombian countryside.
  - `Medellfn` → `Medellín` — accented í misread as 'f' (city is Medellín)

**#13 · El Chupacabra · Text**  
Literally "goat sucker," this legendary American ~~cryptld Is~~ **cryptid is** often described as a reptile-like creature that attacks and drinks the blood of sheep and other livestock. Most supposed sightings have been attributed to dogs or wolves afflicted by the skin disease mange.
  - `cryptld Is often` → `cryptid is often` — 'l' misread for 'i' in cryptid; 'Is' wrongly capitalized mid-sentence

**#19 · Hitler's Brain · Text**  
A trope first featured in a 60s sci-fi film, where Nazi scientists remove this organ from the ~~FClhrer's~~ **Führer's** head and hide it in the fictional South American country of Mandoras. The film currently holds an approval rating of 0% on the metareview site Rotten Tomatoes.
  - `FClhrer's` → `Führer's` — 'ü' misread as 'Cl' (der Führer)

**#22 · Che Guevara · Text**  
A Marxist leader in the Cuban Revolution, whose rebellious ~~Image~~ **image** has been commodified on T-shirts worldwide. The image, a high contrast version of the ~~Guerril lero~~ **Guerrillero** Heroico photograph by Alberto Korda, depicts him with mustache, beret, and implacable expression.
  - `rebellious Image` → `rebellious image` — mid-sentence word wrongly capitalized (OCR capital-I artifact)
  - `Guerril lero` → `Guerrillero` — word wrongly split

**#23 · A Velociraptor · Text**  
A bipedal, feathered carnivore from the Cretaceous Period. It is one of the most well-known dinosaurs due to its prominent role in the 1993 film Jurassic Park, where it was depicted inaccurately as large and featherless, but quite ~~acccurately~~ **accurately** as a clever girl.
  - `acccurately` → `accurately` — stray extra 'c'

**#25 · William Howard Taft · Text**  
Secretary of War, ~~1oth~~ **10th** Chief Justice of the Supreme Court, and most obese president in US history. It is unclear whether the story of his getting stuck in a White House bathtub is true, but it was confirmed that on at least one occasion, he caused it to overflow.
  - `1oth` → `10th` — letter o misread for digit 0 (Taft was 10th Chief Justice)

**#27 · Shirtless Vladimir Putin · Text**  
Former KGB officer and current President of Russia. Under his rule, Russia has grown increasingly undemocratic. He cultivates a rugged image in state media, being shown riding half-dressed on horseback and "discovering" two Ancient Greek urns ~~In~~ **in** the Black Sea.
  - `urns In the` → `urns in the` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#29 · Baby Jessica · Text**  
The subject of a 24-hour media frenzy in 1987 when she fell down a well, setting a precedent for how cable news networks cover small local tragedies. At the time, President Reagan claimed that "everybody in America became [her] godmothers and ~~godfathers.•~~ **godfathers."**
  - `godfathers.•"` → `godfathers."` — stray bullet character before closing quote

**#36 · Oscar Pistorius · Text**  
Sometimes known as "Blade Runner" or "the fastest man on no legs," this sprinter became the first double leg amputee to participate in the Olympics. He was subsequently charged with the murder of his girlfriend, but maintains that he confused her for an ~~Intruder.~~ **intruder.**
  - `an Intruder` → `an intruder` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#37 · Leeroy Jenkins · Text**  
A World of Warcraft player famous for going ~~all<~~ **AFK** while his guild planned a complicated raid, then proceeded to run into the encounter screaming his own name and getting his guildmates killed. After being called "stupid as ~~hel I,"~~ **hell,"** he cryptically replied "At least I have ~~chicken.•~~ **chicken."**
  - `going all<` → `going AFK` — corrupted token with stray '<'; Leeroy Jenkins lore is 'going AFK'
  - `hel I` → `hell` — word wrongly split; 'l' scanned as 'I'
  - `chicken.•"` → `chicken."` — stray bullet character before closing quote

**#39 · Elian Gonzalez · Text**  
A Cuban boy who was the subject of an ~~International Incident~~ **international incident** when his relatives attempted to keep him in the US against his father's wishes that he return to Cuba. A famous image from the event shows an armed border agent discovering the boy cowering in a closet.
  - `an International Incident` → `an international incident` — mid-sentence words wrongly capitalized (OCR capital-I artifact)

**#42 · Charlton Heston · Text**  
An actor and President of the NRA, who starred in such films as The Ten Commandments, The Omega Man, and Planet of the Apes, where he was known for lines such as "Take your stinking paws off me you damn dirty apes!" He became a vociferous gun advocate in the ~~BOs.~~ **80s.**
  - `in the BOs` → `in the 80s` — 8 misread as B and 0 as O

**#44 · Mr. Trololo · Text**  
The internet moniker of Eduard Khil, a Russian singer who became famous when his 1976 recording of ~~•1~~ **"I** Am Glad, 'Cause I'm Finally Returning Back Home" was uploaded to YouTube. Khil performs the song using nonsense syllable rather than the lyrics.
  - `•1 Am Glad` → `"I Am Glad` — stray bullet was opening quote; digit 1 misread for capital I

**#47 · A Communist · Text**  
A member of a political movement that believes in the common ownership of the means of production. The concept was first developed by the German political philosopher Karl Marx and became the national ideology of the Soviet Union ~~In~~ **in** the 20th century.
  - `Union In the` → `Union in the` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#50 · Richard Pryor · Text**  
A comedian once described by Jerry Seinfeld as "the Picasso of our profession," who was famous for his open discussion of race. In a ~~wellknown~~ **well-known** incident, while freebasing cocaine, he poured 151-proof rum over his body, lit a match, and ran down the street on fire.
  - `In a wellknown` → `In a well-known` — hyphen lost at line break, joining 'well-known'

**#52 · An Illusionist · Text**  
A performer of magic acts that often include demonstrating "impossible" tricks to a credulous audience. The term was preferred by the character Gob Bluth in the television series Arrested ~~Development.~~ **Development,** whose performances often went horribly wrong.
  - `Arrested Development.
whose` → `Arrested Development,
whose` — comma misread as period (clause continues with lowercase 'whose')

**#56 · Tonya Harding · Text**  
Olympic figure skater, professional boxer, sex tape star, land speed record holder for vintage gas coupes, and felon. She became a pariah after conspiring with her husband, Jeff Gillooly, to break competitor Nancy Kerrigan's leg by whacking ~~It~~ **it** with a telescopic baton.
  - `whacking It with` → `whacking it with` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#57 · A Mole · Text**  
An informant or spy recruited to report on a target government or organization from the inside. They ~~a re~~ **are** named after a small, subterranean species of mammal. The term was popularized by John Le Carre in Tinker, Tailor, Soldier, Spy, but was first used by Francis Bacon in 1626.
  - `They
a re named` → `They
are named` — word 'are' wrongly split

**#58 · Prince · Text**  
The "artist formerly known as," who released Purple Rain and the Batman soundtrack. In 2011, the website Heavy Table published illustrations of his refrigerator, which contained ~~S~~ **5** pounds of Dunk-a-roos, 18 varieties of mustard, Braunschweiger, and a quart of Yak's milk.
  - `contained S pounds` → `contained 5 pounds` — letter S misread for digit 5

**#62 · Anne Frank · Text**  
A wartime diarist and Holocaust victim. After visiting the famous site where her family hid from the Nazis for nearly two ~~yea rs,~~ **years,** the pop star Justin Bieber wrote, "Truly inspiring to be able to come here. Anne was a great girl. Hopefully she would have been a belieber."
  - `two yea rs` → `two years` — stray space split inside word

**#63 · Deep Blue · Text**  
An IBM computer that defeated chess champion Garry Kasparov 2-1, with 3 draws. Kasparov demanded a rematch after accusing IBM of cheating. They declined and decommissioned it following the match. Due to its small sample size, ~~It~~ **it** does not have an ELO rating.
  - `size,
It does` → `size,
it does` — mid-sentence 'it' wrongly capitalized (i misread as I)

**#67 · Pac-Man · Text**  
The hero and title character of an ~~BOs~~ **80s** arcade game, where he navigates mazes and eats pellets. power pellets, and fruit while avoiding ghosts. One of gaming's earliest breakout stars, he was soon usurped by his female counterpart in a far superior sequel.
  - `an
BOs arcade` → `an
80s arcade` — '80s' misread as 'BOs' (8->B, 0->O)

**#68 · Godzilla · Text**  
The King of the Monsters, who first appeared ~~In~~ **in** a series of Japanese films made in response to the atomic bombings of Hiroshima and Nagasaki. The monster typically has a reptilian look, walks on two legs, has a long tail. and has "nuclear breath."
  - `appeared In a` → `appeared in a` — mid-sentence 'in' wrongly capitalized

**#77 · A Grammar Nazi · Text**  
A person who enforces language rules to an unusually high degree. According to knowyourmeme.com. one of the earliest uses was in 1995, when a user on the newsgroup alt.gothic called someone out for correcting the use of the term "thusly" for ~~"thus.•~~ **"thus."**
  - `"thus.•"` → `"thus."` — removed stray bullet artifact adjacent to closing quote

**#79 · Hannibal Lector · Person**  
Hannibal ~~Lector~~ **Lecter**
  - `Lector` → `Lecter` — real name is Hannibal Lecter

**#81 · Dr. Henry Heimlich · Text**  
A surgeon credited with inventing a maneuver that prevents suffocation when a person is choking by jamming ~~YoUr~~ **your** fist into their abdomen. He also advocated for the technique be used to treat drowning (don't do it) and that malaria could treat cancer, Lyme disease, and HIV.
  - `jamming YoUr fist` → `jamming your fist` — garbled mixed-case 'YoUr'; mid-sentence 'your'

**#82 · The Shoe Bomber (Richard Reid) · Text**  
A would-be suicide bomber who tried and failed to blow up a plane with his casual footwear. He was caught trying to use a match to light a fuse mid-flight, explosive sneaker in his lap. The incident prompted the TSA to institute footwear screening at ~~al rports.~~ **airports.**
  - `at al rports` → `at airports` — 'airports' misread/split as 'al rports' (i->l plus stray space)

**#89 · Teddy Ruxpin · Text**  
A storytelling toy bear from the ~~BOs,~~ **80s,** who had an audio cassette deck in his body. Stories such as "The Wooly What's-It: Learning Can Be Fun!" and "Tweeg and the Bounders: You Have to Earn the Things Worth Having" tended to focus on promoting positive behavior.
  - `from the BOs,` → `from the 80s,` — '80s' misread as 'BOs' (8->B, 0->O)

**#91 · Your Mom · Text**  
The woman who gave birth to you and/or raised you. The word above or the actual name of your real-life caregiver are both ~~val id.~~ **valid.**
  - `both val id` → `both valid` — stray space split inside word

**#93 · The Eye of Sauron · Text**  
A manifestation of the title character in J.R.R. ~~Tolklen's~~ **Tolkien's** fantasy series The Lord of the Rings. Frodo describes it as "rimmed with fire, but was itself glazed, yellow as a cat's, watchful and intent, and the black slit of its pupil opened on a pit, a window into nothing."
  - `Tolklen's` → `Tolkien's` — 'Tolkien' misread as 'Tolklen' (i->l)

**#95 · Bloody Mary · Text**  
A legendary ghost who is said to be conjured ~~In~~ **in** a mirror by saying her name multiple times. Often attempted by young girls, the ghost is sometimes said to reveal the future and other times said to attempt to scratch the person's eyes out.
  - `conjured In a` → `conjured in a` — mid-sentence 'in' wrongly capitalized

**#97 · O.J. Simpson · Text**  
Former professional football player, actor, and ~~lsotoner~~ **Isotoner** spokesman. He was found not guilty of murder in one of the most public trials of the ~~2oth~~ **20th** century. He wrote a book about the case called If I Did It and is currently incarcerated for the theft of his own sports memorabilia.
  - `and lsotoner spokesman` → `and Isotoner spokesman` — brand 'Isotoner'; capital I misread as lowercase l
  - `the
2oth century` → `the
20th century` — '20th' misread as '2oth' (0->o)

**#99 · A Leper · Text**  
A person infected with Hansen's Disease, which sometimes results in the inability to feel pain and consequent loss of body parts. To prevent the spread of the disease, they were historically separated into isolated colonies-a practice still alive ~~In~~ **in** India and China.
  - `alive In India` → `alive in India` — mid-sentence 'in' wrongly capitalized

**#100 · Khan! · Text**  
A villain from the Star Trek franchise, who once controlled a portion of the earth during the Eugenics Wars of the 90s. Ricardo Montalban played the genetically engineered superhuman, delivering lines such as "Revenge is a dish that ~~Is~~ **is** best served cold."
  - `that
Is best` → `that
is best` — mid-sentence 'is' wrongly capitalized

**#102 · A California Raisin · Text**  
A member of a fictional R&B group composed of anthropomorphic dried grapes from the West Coast. They came to prominence in claymation form, singing a cover of "I Heard It Through the ~~Grapevine•~~ **Grapevine"** in an advertisement. They were also popular as plastic toys.
  - `Grapevine•
in` → `Grapevine"
in` — closing quote of song title garbled as bullet; opening quote present

**#104 · Aunt Jemima · Text**  
The pretty racist mascot of a line of pancake mixes and syrups by the Quaker Oats Company. Her character was derived from a minstrel show's mammy-like figure. Like Uncle Ben, she represents an idealized view of domestic servitude in southern ~~I ife.~~ **life.**
  - `southern I ife` → `southern life` — 'life' misread/split as 'I ife' (l->I plus stray space)

**#107 · A TSA Agent · Text**  
An employee of a ~~us~~ **US** Department of Homeland Security branch. Many of its employees are posted in airports to screen passengers and their property, including pat-downs and viewing x-rays. Their average salary is $25K-$38K per year, excluding swag.
  - `a us Department` → `a US Department` — small-caps US

**#108 · A Cylon · Text**  
A member of a robotic civilization in the Battlestar Galactica franchise. They were created somewhat by accident on Caprica and are unique in that they experience many common human emotions and are often not fully aware of their status as a robotic ~~llfeform.~~ **lifeform.**
  - `robotic llfeform` → `robotic lifeform` — 'lifeform' misread as 'llfeform' (i->l)

**#110 · Ba bar · Person**  
~~Ba bar~~ **Babar**
  - `Ba bar` → `Babar` — stray space split inside name

**#110 · Ba bar · Text**  
An elephant from the children's book by Jean de Brunhoff, who critics argue offers a justification for colonialism. In the book, he leaves the jungle, visits a city, returns in a green suit, introduces French civilization to his fellow elephants, and ~~Is~~ **is** crowned king.
  - `and Is crowned` → `and is crowned` — mid-sentence 'is' wrongly capitalized

**#117 · Count Chocula · Text**  
A vampire mascot from the General Mills Corporation's series of monster-based breakfast cereals. Like his ~~col leagues~~ **colleagues** Franken-Berry, Boo-Berry, Fruit Brute, and Yummy Mummy, his origin is a mystery. His tagline, "I vant to eat your cereal!" seems a little on the nose.
  - `his col leagues` → `his colleagues` — stray space split inside word

**#118 · Burning Man · Text**  
A 40-foot wooden effigy that is set on fire during a weeklong event in Nevada's Black Rock Desert. The organizers deny that it has any connection to similar wicker effigies that were built by ancient Druids for pagan Celtic rituals that some speculate ~~Involved~~ **involved** human sacrifice.
  - `speculate Involved` → `speculate involved` — mid-sentence 'involved' wrongly capitalized

**#121 · A Sherpa · Text**  
A member of a Nepalese ethnic group that resides ~~In~~ **in** the Himalayan mountain range. The term often refers to guides who assist climbers. Among the most famous of these in history was Tenzing Norgay, who reached the summit of Mount Everest with Edmund Hillary in 1953.
  - `resides In the` → `resides in the` — Capital I misread for lowercase i mid-sentence

**#123 · Ceiling Cat · Text**  
The subject of a famous internet photo showing a feline peeking out of a hole and, allegedly, "watching you ~~masturbate.•~~ **masturbate."** In 2010, a Redditor indicated that the hole was actually in a wall, claiming "This changes everything." The feline is said to have a rival in the basement.
  - `masturbate.•` → `masturbate."` — Bullet artifact for closing double-quote

**#127 · George Washington · Text**  
The 1st President of the ~~us.~~ **US.** John Adams claimed that his famed toothlessness was the result of cracking Brazil nuts. His false teeth were not made of wood, but hippopotamus and elephant ivory. He had a previous pair most likely made from, no ~~Joke,~~ **joke,** slave teeth.
  - `of the us.` → `of the US.` — OCR lowercased the acronym US
  - `no Joke,` → `no joke,` — Capital J misread for lowercase j mid-sentence

**#128 · The Lord of the Dance · Text**  
An Irish performer who came to prominence during the intermission of the 1994 ~~Eu rovision~~ **Eurovision** Song Contest. His show, Riverdance, melded tapping with Irish folk traditions, following his quest to defeat the dark lord Don Dorcha from destroying Planet Ireland.
  - `1994 Eu rovision Song` → `1994 Eurovision Song` — Word wrongly split by scan

**#129 · Goatse · Text**  
A shock site linking unsuspecting victims to the file ~~hello.Jpg,~~ **hello.jpg,** an image of a naked man stretching his anus several inches in diameter. The man's wedding band is clearly visible on his left ring finger. The site used the rare top-level domain for the Christmas Islands, ~~.ex.~~ **.cx.**
  - `hello.Jpg` → `hello.jpg` — Capital J misread for lowercase j in file extension
  - `, .ex.` → `, .cx.` — Christmas Island TLD is .cx; c misread as e

**#138 · Paula Deen · Text**  
A celebrity chef and former Food Network personality, who has received criticism for the excessive use of fat, ~~sa It,~~ **salt,** and sugar in her recipes. She was sued in 2013 for racial and sexual discrimination, such as using derogatory remarks toward African Americans.
  - `fat, sa It, and` → `fat, salt, and` — 'salt' wrongly split and lt misread as 'It'

**#142 · Damien Hirst · Text**  
The wealthiest artist in the world, who is best known for selling a huge dead tiger shark preserved in formaldehyde for more than $8M. He once argued that the 9/11 terrorists "need ~~congratulating•~~ **congratulating"** for "achieving something which nobody would have thought ~~possible.•~~ **possible."**
  - `congratulating• for` → `congratulating" for` — Bullet artifact for closing double-quote
  - `possible.•` → `possible."` — Bullet artifact for closing double-quote

**#144 · William Shatner · Text**  
A legendary ~~actor.~~ **actor,** who portrayed classic characters such as Captain Kirk, TJ ~~Hooker.~~ **Hooker,** the guy who saw a plane gremlin on The Twilight Zone, and the Priceline Negotiator. He also has a musical career that began with a spoken word performance of Elton John's "Rocket Man."
  - `A legendary actor. who` → `A legendary actor, who` — Comma misread as period (lowercase word follows)
  - `TJ Hooker. the` → `TJ Hooker, the` — Comma misread as period (lowercase word follows)

**#146 · Blackfish · Text**  
An orca at Seaworld who raised questions about animal captivity by killing 3 people. In 2010, ~~MOtley~~ **Motley** Crue founder Tommy Lee wrote to Seaworld's president stating that he knew humans still "get into the pool and masturbate him with a cow's vagina filled with hot ~~water.•~~ **water."**
  - `MOtley
Crue` → `Motley
Crue` — Capital O misread for lowercase o
  - `hot water.•` → `hot water."` — Bullet artifact for closing double-quote

**#150 · Humpty Dumpty · Text**  
A character from a nursery rhyme who falls off a wall and can't be put back together again. Typically portrayed as a humanoid egg, scholars have speculated that he represents Richard ~~111,~~ **III,** the humpback king who was defeated at Bosworth Field by Henry VII.
  - `Richard 111,` → `Richard III,` — Digits 111 misread for Roman numeral III

**#153 · Joe Camel · Text**  
The debonair, bipedal ungulate and mascot for an R.J. Reynolds brand of cigarettes. When ~~interna I~~ **internal** documents demonstrated that the company was targeting children as future smokers, the character was retired and replaced with a more traditional quadruped ~~In~~ **in** 1997.
  - `When interna I
documents` → `When internal
documents` — 'internal' wrongly split, l misread as I
  - `quadruped In 1997` → `quadruped in 1997` — Capital I misread for lowercase i

**#154 · Free Willy · Text**  
The title character from the ~~1gg3~~ **1993** film about a young boy's attempts to rescue a killer whale from its cruel life as an amusement park attraction. At the film's conclusion, he flees a whaling ship by jumping over a rock embankment and returns to his family.
  - `the 1gg3
film` → `the 1993
film` — Digits 99 misread as gg

**#159 · Kim Jong-ii · Person**  
Kim ~~Jong-ii~~ **Jong-il**
  - `Kim Jong-ii` → `Kim Jong-il` — Final lowercase l misread as i

**#162 · Alex Trebek with a mustache · Text**  
The host of the quiz show Jeopardy! for thirty years and counting. He has appeared self-deprecatingly as a version of himself in films and TV shows, including Seinfeld and Short Cuts. For the purposes of this card, he still has really great facial hair on his upper ~~llp.~~ **lip.**
  - `upper llp.` → `upper lip.` — 'lip' misread as 'llp'

**#168 · Josephine Baker · Text**  
A performer, civil rights activist, and the first black woman to star in a major film. She only performed for integrated audiences, though many of her acts, such as the exotic Danse Sauvage wearing a banana skirt, strike a contemporary viewer as ~~sti II~~ **still** pretty messed up racially.
  - `as sti II
pretty` → `as still
pretty` — 'still' wrongly split, ll misread as II

**#174 · Tom Selleck,s mustache · Person**  
Tom ~~Selleck,s~~ **Selleck's** mustache
  - `Tom Selleck,s` → `Tom Selleck's` — Apostrophe misread as comma

**#174 · Tom Selleck,s mustache · Text**  
The facial hair of this American actor and ~~sos~~ **80s** style ~~Icon.~~ **icon.** He ~~Is~~ **is** most famous for his title role in Magnum, P.I. as well as appearances in films such as Three Men and a Baby and Mr. Baseball. In addition to his upper lip decoration, his signature look included colorful Hawaiian shirts.
  - `and sos style Icon.` → `and 80s style icon.` — '80s' misread as 'sos'; capital I misread for lowercase i
  - `Icon. He Is most` → `icon. He is most` — Capital I misread for lowercase i

**#178 · Kevin Bacon · Text**  
An actor best known for the game based on six degrees of separation that bears his name, e.g. ~~Andr~~~ **André** the Giant and Christopher Guest appeared in The Princess Bride; Christopher Guest and this actor appeared in A Few Good Men; thus ~~Andr~~~ **André** the Giant's number is 2).
  - `e.g. Andr~ the` → `e.g. André the` — Tilde artifact for accented e (é)
  - `thus
Andr~ the` → `thus
André the` — Tilde artifact for accented e (é)

**#180 · The Shark from Jaws · Text**  
A man-eating great white that terrorizes the town of Amity Island in a film by Steven Spielberg. Not seen until well into the film, it is so large that Roy Scheider's character suggests the crew is "gonna need a bigger ~~boat.•~~ **boat."** It was nicknamed Bruce after Spielberg's lawyer.
  - `bigger boat.•` → `bigger boat."` — bullet char is OCR misread of closing quotation mark

**#183 · A T. Rex · Text**  
Meaning "lizard king," this species of bipedal carnivore lived ~~ln~~ **in** western North America during the Cretaceous Period. They are the most widely known dinosaur in the world due to their adorably tiny arms and footsteps that vibrate cups of water.
  - `lived ln western` → `lived in western` — lowercase l misread for i in 'in'

**#190 · Rick James · Text**  
A musician whose decadent, drug-fueled lifestyle is frequently parodied, notably in several "True Hollywood ~~Stories•~~ **Stories"** on The Chappelle Show. The popularity of depictions of his cocaine habits and use of the word "bitch" contributed to Chappelle leaving the show.
  - `Hollywood Stories•` → `Hollywood Stories"` — bullet char is OCR misread of closing quotation mark

**#191 · Gene Wilder · Text**  
The stage name of Jerome Silberman, who is best known for his collaboration with Mel Brooks in Blazing Saddles, The Producers, and other films. An image of him in Willy Wonka & the Chocolate Factory is used in the popular Condescending Wonka caption ~~onllne.~~ **online.**
  - `caption onllne.` → `caption online.` — double l misread; should be 'li' in 'online'

**#192 · A Werewolf · Text**  
A human who transforms into a hirsute, bloodthirsty creature. Known as lycanthropy, this change is often triggered by a ~~fu II~~ **full** moon. Suspected lycanthropes were persecuted in early modern Europe, and are now a staple figure in pop culture and party games.
  - `a fu II moon` → `a full moon` — 'full' split, ll misread as II

**#198 · A Nihilist · Text**  
Popularly, someone who believes in nothing. As a philosophical concept, a person who believes that major aspects of life or human inquiry are either not valid or do not exist. They are often portrayed as effete intellectuals, such as the wimpy German thugs ~~In~~ **in** The Big ~~Lebowskl.~~ **Lebowski.**
  - `thugs In The` → `thugs in The` — spurious capital I on 'in'
  - `Lebowskl.` → `Lebowski.` — trailing l misread for i

**#199 · Phineas Gage · Text**  
A 19th century railroad worker and frequent citation in undergraduate psychology papers. His left frontal lobe was severely damaged following an explosion that drove an iron spike through his skull. The damage resulted in a radical change ~~In~~ **in** his personality and behavior.
  - `In his` → `in his` — spurious capital I on 'in'

**#200 · Ricardo Montalban · Text**  
A Mexican actor who played Khan Noonien Singh in the original Star Trek series and Star Trek II: The Wrath of Khan. He was also known for his endorsement of the Chrysler ~~C6rdoba,~~ **Cordoba,** where he praised the ~~•tastefulness~~ **"tastefulness** of its ~~appearance•~~ **appearance"** and ~~Its~~ **its** "soft ~~Corl nth Ian leather.•~~ **Corinthian leather."**
  - `C6rdoba` → `Cordoba` — digit 6 misread for o (Chrysler Cordoba)
  - `•tastefulness of its appearance•` → `"tastefulness of its appearance"` — bullet chars are OCR misreads of quotation marks
  - `Its "soft` → `its "soft` — spurious capital I on 'its'
  - `Corl nth Ian` → `Corinthian` — 'Corinthian' broken into pieces with l/I misreads
  - `leather.•` → `leather."` — bullet char is OCR misread of closing quote

**#201 · A Redshirt · Text**  
A stock, semi-anonymous character who ~~Is Introduced~~ **is introduced** only to die soon after. The term derives from the costumes worn by extras in the original Star Trek television series who would accompany the lead actors to a hostile situation and be killed in order to heighten tension.
  - `who Is Introduced` → `who is introduced` — spurious capitals on 'is' and 'introduced'

**#202 · David Attenborough · Text**  
Widely known as the voice of nature documentaries, he is considered a national treasure in the UK (though he rejects the term). He is so beloved that his replacement with Sigourney Weaver as the narrator in the American version of Planet Earth caused protests ~~on line.~~ **online.**
  - `protests on line.` → `protests online.` — 'online' wrongly split into two words

**#204 · The Id · Text**  
One of ~~the~~ the three parts of Sigmund Freud's model of the psyche that constitute mental life. ~~Th is~~ **This** part contains a person's instincts and is the source of our impulse for sex and aggression. In adult life it becomes the most dark, inaccessible aspect of personality.
  - `One of the the three` → `One of the three` — duplicated word 'the'
  - `Th is part` → `This part` — 'This' wrongly split

**#207 · A Man from Nantucket · Text**  
A character from a famous limerick that references an island 30 miles south of Cape Cod. The limerick describes this person as being particularly well-endowed, with the most popular rhyming couplet being "Whose dick was so long he could suck ~~It.•~~ **it."**
  - `could suck It.•` → `could suck it."` — spurious capital I on 'it'; bullet is OCR misread of closing quote

**#208 · Bobby Fischer · Text**  
America's greatest chess player and one of its most famous racists. He defeated Boris Spassky in 1971 to become world champion. A recluse, he returned to the public eye in the 90s to invent a new Chess timing system and to be a public anti-Semite before dying ~~In~~ **in** Iceland ~~In~~ **in** 2008.
  - `dying In Iceland In 2008` → `dying in Iceland in 2008` — spurious capital I on both 'in'

**#209 · Rob Ford · Text**  
The disgraced mayor of Toronto who confessed to smoking crack "probably in one of my drunken stupors." Responding to ~~al legations~~ **allegations** of sexual harassment, he said, "It was said I want to eat her pussy. I would never do that. I've got more than enough to eat at home."
  - `to al legations` → `to allegations` — 'allegations' wrongly split

**#216 · A Horse-Sized Duck · Text**  
From a hypothetical scenario that poses the question of who ~~wou Id~~ **would** win in a fight: a single equine-sized fowl or fivescore fowl-sized equines. The question was made famous in a 2012 Reddit AMA with President Barack Obama. The comment received over 1,000 upvotes.
  - `who wou Id` → `who would` — 'would' split, I misread for l

**#220 · Tycho Brahe · Text**  
A Danish noble and astronomer. At 20, he lost part of ~~h ls~~ **his** nose ~~In~~ **in** a duel and wore a replacement made of silver and gold. He owned a pet elk and hired a psychic dwarf named Jepp. He is rumored to have died from refusing to leave a banquet to urinate, because etiquette.
  - `part of h ls nose In a duel` → `part of his nose in a duel` — 'his' split with l/i misread; spurious capital I on 'in'

**#226 · Robert Hamilton · Text**  
An American artist and self described "best totally unknown painter ~~In~~ **in** the world.'' His improvisational style was praised by modernist contemporaries, including Andrew Wyeth. Like his beloved jazz, Hamilton believed "the picture makes itself. When I'm finished, I don't know how the hell I did it.''
  - `painter In the` → `painter in the` — spurious capital I on 'in'

**#232 · Bartleby the Scrivener · Text**  
The title character from a short story by Herman Melville, who is employed to copy legal documents by hand. After gaining a reputation as a hard worker, he unexpectedly refuses to do any further work, instead repeating "I would prefer not to" to ~~al I~~ **all** requests.
  - `to al I requests.` → `to all requests.` — 'all' split, I misread for l

**#233 · Grape Lady · Text**  
A newscaster who falls from a platform after attempting to cheat during a light-hearted segment at Chateau Elan Winery. After falling out of frame, she is heard off camera making strange noises and saying, ~~·ow~~ **"ow** ow OW ... STOP STOP ... OOH OOH OOH .. .I can't breathe."
  - `saying, ·ow` → `saying, "ow` — middle-dot char is OCR misread of opening quotation mark

**#235 · Judas Iscariot · Text**  
One of Jesus's twelve apostles, who betrayed him for 30 pieces of silver. He famously revealed Jesus's identity to Roman soldiers by giving him a kiss, and his name is now synonymous with betraying a person or even an abstract set of ~~Ideals.~~ **ideals.**
  - `Ideals.` → `ideals.` — spurious capital I on 'ideals'

**#237 · Siri · Text**  
The name of Apple's personal assistant on ~~IOS~~ **iOS** operation system that interacts with users through natural language. It has spawned a popular Tumblr consisting of ironic interactions, such as the search "I have a gambling ~~addiction•~~ **addiction"** returning a list of nearby casinos.
  - `on IOS operation` → `on iOS operation` — 'iOS' miscapitalized as IOS
  - `addiction•` → `addiction"` — bullet char is OCR misread of closing quote

**#238 · Silvio Berlusconi · Text**  
The former Prime Minister of Italy, owner of A.C. Milan, and serial tax evader. He is notorious for soliciting prostitutes and for organizing a type of orgy known as a "bunga bunga," ~~It~~ **it** is rumored that the concept was introduced to him by Libyan dictator, Muammar Gaddafi.
  - `bunga," It is rumored` → `bunga," it is rumored` — spurious capital I on 'it' following comma

**#239 · The Dread Pirate Roberts · Text**  
The founder of the Silk Road, the "amazon.com of illegal drugs." His identity remains a mystery, though the name suggests it belongs to multiple people, since it was lifted from a character in ~~the~~ The Princess Bride, where a mythical brigand ~~Is~~ **is** actually a series of individuals.
  - `in the The Princess` → `in The Princess` — duplicated article 'the'
  - `brigand Is` → `brigand is` — spurious capital I on 'is'

**#241 · The Sorcerer's Apprentice · Text**  
The assistant to a wizard in Disney's Fantasia. Played by Mickey Mouse, he enchants a broom to fetch water. Unable to control the magic, a flood ensues. Each time he attempts to destroy the broom and end the spell, it splits in ~~ha If~~ **half** and continues its work at double pace.
  - `in ha If and` → `in half and` — OCR split 'half' into 'ha If'

**#244 · The 800 Pound Gorilla · Text**  
An idiom that describes a primate so powerful and heavy that it can ignore the rights of others. The original source is a riddle that asks where it sits ~~CA:~~ **(A:** Anywhere it wants.) This term is commonly confused with a similar expression about an elephant.
  - `where it sits CA:` → `where it sits (A:` — opening parenthesis misread as 'C'; closing ')' present later

**#245 · Charizard · Text**  
A species of ~~Pok~mon~~ **Pokémon** that resembles an orange dragon and is the evolved form of Charmeleon and the final evolution of Charmander. Despite its appearance, it is a fire/flying type, NOT a dragon type. Its Japanese name is Lizardon.
  - `Pok~mon` → `Pokémon` — tilde is mangled 'é'

**#246 · Portnoy · Text**  
The title character from a 1969 novel by ~~Phil Ip~~ **Philip** Roth that ~~Is~~ **is** told as an extended psychotherapy session by a young Jewish bachelor. The novel is notorious for its description of this character masturbating with a piece of raw liver, which his mother later serves for dinner.
  - `Phil Ip Roth` → `Philip Roth` — OCR split/misread of 'Philip'
  - `that Is told` → `that is told` — capital I for lowercase i

**#254 · Oprah's best friend (Gayle) · Text**  
The co-anchor of CBS This Morning and Editor-at-large for ~~0~~ **O** Magazine. She gained notoriety for her long-running relationship with a famous talk show host and "Queen of All Media." Despite being married to a man, there are persistent rumors that the two are lovers.
  - `for 0 Magazine` → `for O Magazine` — zero misread for letter O (Oprah's O Magazine)

**#255 · Skeletor · Text**  
The main villain in the Masters of the Universe fantasy world. He ~~ls~~ **is** the arch nemesis of He-Man and is typically shows with a blue humanoid body, bare skull, and purple hood. His goal is to learn the secrets of Castle Grayskull and use them to conquer the land of Eternia.
  - `He ls the` → `He is the` — 'ls' misread for 'is'

**#256 · Star Wars Kid · Text**  
The star of a viral video that shows a high school student ~~Imitating~~ **imitating** lightsaber moves using a golf ball retriever. The tape leaked online after being left in the basement of his school, leading to dozens of remixes featuring music and advanced special effects.
  - `student Imitating` → `student imitating` — capital-I mid-sentence

**#257 · A Merman · Text**  
The male version of the mythological creature that ~~Is~~ **is** a woman from the waist up but has a fish tail in place of legs. Their behaviors and abilities range across cultures, and include having green teeth, the ability to cure illnesses, seducing women, and holding tridents.
  - `that Is a woman` → `that is a woman` — capital I for lowercase i

**#258 · Montezuma · Text**  
The 9th tlatoani of Tenochtitlan and ruler of the Aztec Triple Alliance. During their first contact with Europeans, he was killed by conquistador Hernan Cortes's men as the fled his capital. His ~~"revenge•~~ **"revenge"** is a euphemism for contracting traveler's diarrhea in Mexico.
  - `His "revenge•` → `His "revenge"` — bullet misread of closing quotation mark

**#261 · The1% · Person**  
~~The1%~~ **The 1%**
  - `The1%` → `The 1%` — words wrongly joined by scan

**#263 · A Mormon · Text**  
A member of the Latter-Day Saints, inspired by the visions of 19th century American Joseph Smith. They were once infamous for some members practicing polygamy. Members taking part in endowment ceremonies wear special underwear called "temple ~~garments.•~~ **garments."**
  - `garments.•"` → `garments."` — stray bullet before closing quote removed

**#273 · Dr. Mario · Text**  
This ~~plumber-tu med-pharmacist~~ **plumber-turned-pharmacist** and title character of this Nintendo puzzle series. Clearly inspired by Tetris, the player organizes pills by color, ostensibly to eradicate viruses and definitely not to teach children how to raid their parent's medicine cabinet.
  - `plumber-tu med-pharmacist` → `plumber-turned-pharmacist` — OCR mangled 'turned' (rn->m plus stray space)

**#274 · A Troll Doll · Text**  
A plastic toy depicting a being with distinctive ~~tal I,~~ **tall,** bright, and fuzzy hair. They were the subject of fads throughout the 70s, ~~BOs,~~ **80s,** and 90s. The original version was carved by a poor Danish fisherman and woodcutter as a Christmas gift to his daughter.
  - `distinctive tal I,` → `distinctive tall,` — OCR split 'tall'
  - `70s, BOs, and 90s` → `70s, 80s, and 90s` — '80s' misread as 'BOs' (8->B, 0->O)

**#275 · A Dead Horse · Text**  
Useless to beat and effectively ~~unrldeable,~~ **unrideable,** this deceased animal is used in an idiom to explain that a point, once made, does not need to be re-stated. Similar the phrase, "To slay the ~~slain.•~~ **slain."** This animal is substituted with a dog in other parts of the English speaking world.
  - `unrldeable` → `unrideable` — 'l' misread for 'i'
  - `slain.•"` → `slain."` — stray bullet before closing quote removed

**#278 · Lady Gaga's meat dress · Text**  
A piece of raw beef worn by "Mother Monster" to the 2010 MTV Video Music Awards. The pop diva stated that she wore the item to highlight her distaste for the military's don't-ask-don't-tell ~~pol icy.~~ **policy.** The item was preserved by a taxidermist, who turned it into jerky.
  - `don't-tell pol icy` → `don't-tell policy` — OCR split 'policy'

**#279 · Kenny G · Text**  
A smooth jazz saxophonist, who is universally reviled by jazz aficionados while simultaneously being one of the best selling recording artists of ~~a II~~ **all** time. Using circular breathing, he set a world record for longest note recorded by holding an ~~E·flat~~ **E-flat** for 45 minutes and 47 seconds.
  - `of a II time` → `of all time` — OCR split/misread of 'all'
  - `an E·flat` → `an E-flat` — middle dot misread of hyphen

**#280 · Solange Knowles · Text**  
A singer, temporary member of Destiny's ~~Chi Id,~~ **Child,** and sister of Beyonce. In 2014, TMZ published security footage of her physically assaulting her brother-in-law, Jay-Z, who along with Beyonce, did not retaliate. The cause of her outburst remains unknown.
  - `Destiny's Chi Id` → `Destiny's Child` — OCR split 'Child'

**#281 · A Pug · Text**  
A short-snouted, ~~brachycephal ic~~ **brachycephalic** dog breed. Generations of inbreeding have led to compact breathing passages that leave them unable to regulate their body temperature by panting. Many airlines have restricted their transport due to in-air deaths.
  - `brachycephal ic` → `brachycephalic` — OCR split 'brachycephalic'

**#284 · Prancer · Text**  
One of the flying reindeer that pulls Santa's sleigh In "The ~~N lght~~ **Night** Before ~~Christmas.•~~ **Christmas."** His name is also used in a fitness method and internet meme by Joanna Rohrback that is a "springy, rhythmic way of moving forward, similar to a horse's gait and ideally induced by elation"
  - `The N lght Before` → `The Night Before` — OCR split/misread of 'Night'
  - `Christmas.•"` → `Christmas."` — stray bullet before closing quote removed

**#287 · Ch airy · Person**  
~~Ch airy~~ **Chairy**
  - `Ch airy` → `Chairy` — OCR split 'Chairy'

**#290 · Mother Teresa · Text**  
A missionary and Nobel Peace Prize winner who claimed "the world is being helped by the suffering of poor people." Her Home for the Dying Destitutes in ~~calcutta~~ **Calcutta** offered no significant medical care and only 7% of donations to her organization were directly used for charity.
  - `in calcutta` → `in Calcutta` — proper noun

**#292 · Lennie Small · Text**  
The large, mentally disabled friend of George ~~In~~ **in** Of Mice and Men. He loves petting soft things, but is unable to control his strength, accidentally killing a puppy and a woman. George shoots him at the end of the novel to protect him from an angry lynch mob.
  - `George In Of Mice` → `George in Of Mice` — capital-I mid-sentence

**#295 · The Obermensch · Person**  
The ~~Obermensch~~ **Übermensch**
  - `The Obermensch` → `The Übermensch` — OCR of Ü as O; Nietzsche term

**#296 · The Dude · Text**  
The nickname of Jeffrey Lebowski in the Coen Brothers film The Big Lebowski. Played by Jeff Bridges. he is depicted as an ~~unemplayed~~ **unemployed** slacker. pacifist, and bowler who drinks White Russians and listens to Creedence. He was based on the Seattle Seven member Jeff Dowd.
  - `an unemplayed` → `an unemployed` — 'a' misread for 'o' in 'unemployed'

**#301 · Kate Bush · Text**  
An English musician known for her ~~id losyncratlc~~ **idiosyncratic** vocal ~~del Ivery,~~ **delivery,** literary sensibility, hit singles such as "Wuthering Heights" and ~~"Babooshka. ·~~ **"Babooshka."** One of her Karate instructors has noted that many of her dance moves owe a debt to her martial arts training.
  - `id losyncratlc` → `idiosyncratic` — OCR l/i + stray space
  - `del Ivery` → `delivery` — OCR split + I/l
  - `Babooshka.
· One` → `Babooshka."
One` — stray · stood in for closing quote

**#302 · A Cyberbu lly · Person**  
A ~~Cyberbu lly~~ **Cyberbully**
  - `A Cyberbu lly` → `A Cyberbully` — OCR stray space

**#303 · A Never Nude · Text**  
The popular term for a gymnophobic, a person who fear nakedness. The condition was satirized on the show Arrested Development, where the character Tobias Fanke would wear cutoff jean shorts at all times. As of 2014, the condition is ~~sti II~~ **still** not recognized by the DSM.
  - `sti II not` → `still not` — OCR split
  - `` → `` — 'Fanke' is likely the character 'Tobias Fünke' (left unchanged — confirm)

**#311 · The Jesus · Text**  
An amateur bowler and alleged pederast ~~In~~ **in** the Coen Brothers film The Big Lebowski. Played by John Turturro, he speaks with a heavy Cuban accent, paints his pinky fingers red, wears a hairnet, refers to himself in the third person, and is not to be fucked with.
  - `pederast In the` → `pederast in the` — capital-I for i mid-sentence

**#313 · Right Said Fred · Text**  
A London-based band formed by the Fairbrassin brothers in 1989, who are famous for their hit, "I'm Too Sexy," which pokes fun at the fashion industry with such notable lines as "Yeah on the catwalk, yeah I ~~I~~ shake my little tush on the catwalk."
  - `yeah I I shake` → `yeah I shake` — OCR doubled I
  - `` → `` — 'Fairbrassin brothers' is likely 'Fairbrass brothers' (left unchanged — confirm)

**#315 · A Coke Mule · Text**  
A person who smuggles illicit drugs across national borders. While methods vary, one involves swallowing ~~late><~~ **latex** balloons filled with the substance, which is later recovered in their feces. Detection of this method is ~~difficu It~~ **difficult** and is often only found on ~~><-ray.~~ **x-ray.**
  - `late><` → `latex` — OCR >< read for x
  - `difficu It` → `difficult` — OCR split
  - `><-ray` → `x-ray` — OCR >< read for x

**#316 · The Ego · Text**  
One of ~~the~~ the three parts of Sigmund Freud's model of the psyche that constitute mental life. It plays an ~~e><ecutive~~ **executive** function, mediating between raw instinct and external reality, such as your ability to delay immediate pleasure for long term objectives.
  - `One of the the three` → `One of the three` — duplicated word
  - `an e><ecutive` → `an executive` — OCR >< read for x

**#317 · A Manic Pixie Dream Girl · Text**  
Described by Nathan Rabin as a "bubbly, shallow creature that exists solely in the imaginations of sensitive writer-directors to teach young men to embrace life and its infinite mysteries." Examples include Natalie Portman in Garden State and Zooey Deschanel ~~In~~ **in** everything.
  - `Deschanel In everything` → `Deschanel in everything` — capital-I for i

**#319 · A Pufferfish · Text**  
One of the most infamous and deadly culinary dishes. Known as Fugu in Japan. ~~its~~ **Its** preparation is strictly controlled, because its liver, ovaries, and eyes contain fatal levels of tetrodotoxin. These areas must be carefully removed to avoid asphyxiation and death.
  - `Japan. its preparation` → `Japan. Its preparation` — lost capital after period

**#321 · General Butt Naked · Text**  
A former leader for the Liberian warlord Roosevelt Johnson. He claimed that before battle "we would get drunk and drugged up, sacrifice a teenager, drink the blood, then strip down to our shoes and go into battle wearing colorful wigs and carrying imaginary ~~purses.•~~ **purses."**
  - `purses.•` → `purses."` — stray • stood in for closing quote

**#323 · Pharell's hat · Person**  
~~Pharell's~~ **Pharrell's** hat
  - `Pharell` → `Pharrell` — rapper is Pharrell Williams

**#324 · A Blue Man · Text**  
A member of a music collective starring a trio of humanoids played by musicians wearing bald caps and makeup. To meet demand, dozens of new performers have been recruited, a process satirized on the show Arrested Development with the would-be recruit Tobias ~~FOnke.~~ **Fünke.**
  - `Tobias FOnke` → `Tobias Fünke` — OCR of 'Fünke' (Arrested Development)

**#328 · MySpace Tom · Text**  
Cofounder of the world's most popular social networking ~~sitebefore~~ **site before** Facebook. He became instantly recognizable because all users who joined the site would automatically "friend" him. He sold the site for $580M to Rupert Murdoch's News Corporation.
  - `networking sitebefore` → `networking site before` — words joined by scan

**#330 · A Bottom · Text**  
In gay culture, a person who prefers penetration during intercourse, usually through the anus. A survey of nearly 56,000 profiles on gay.com found that 32% of ~~us~~ **US** respondents preferred bottom, 26% preferred top, and 42% preferred the versatile role.
  - `of us
respondents` → `of US
respondents` — small-caps US

**#334 · Dick Armey · Text**  
A former ~~us~~ **US** Congressman from Texas who was an important part of the Republican Revolution of the 90s and one of the co-creators of the infamous Contract with America. But for the purposes of this game, he really just has a very funny name.
  - `former us Congressman` → `former US Congressman` — small-caps US read as us

**#336 · A nOOb · Text**  
A term for a beginner or novice at an activity, often used ~~In~~ **in** reference to internet activity, such as online gaming or computer hacking. The term is spelled using leetspeak, the alphabet that uses alternative ASCII characters as a replacement for Latin letters.
  - `used In reference` → `used in reference` — capital-I for i

**#340 · Punxsutawney Phil · Text**  
A clairvoyant Pennsylvania groundhog, who uses the appearance of his own shadow to predict whether spring ~~wil I~~ **will** arrive early or whether there will be six more weeks of winter. His predictions have been correct 39% of the time, less than random guessing.
  - `wil I arrive` → `will arrive` — OCR split

**#344 · Aaron Burr · Text**  
The 3rd Vice President of the ~~us,~~ **US,** who shot Alexander Hamilton in a duel. He was famously the answer to question posed in a 1993 commercial directed by Michael Bay for the Got Milk? campaign, where a historian is unable to answer because his mouth ~~Is~~ **is** clogged with peanut butter.
  - `President of the us,` → `President of the US,` — small-caps US
  - `mouth
Is clogged` → `mouth
is clogged` — capital-I for i

**#351 · The Zodiac Killer · Text**  
A serial murderer whose identity is still unknown. His name is a reference to letters sent by him to newspapers that included a 408- character cipher, which he claimed revealed his identity. In one possible decoding, he claims that his victims will be his slaves ~~In~~ **in** the ~~afterl lfe.~~ **afterlife.**
  - `slaves In the` → `slaves in the` — capital-I for i
  - `afterl lfe` → `afterlife` — OCR split + l

**#352 · E.Honda · Person**  
~~E.Honda~~ **E. Honda**
  - `E.Honda` → `E. Honda` — missing space

**#353 · Carlton Banks · Text**  
The Fresh Prince of Bel-Air's cousin and Uncle Phil's heir. Played by Alfonso Ribeiro, he is depicted as a preppy ~~yaung~~ **young** Republican, who is probably best known for his spazzy dance to Tom Jones's song "It's Not Unusual" and being slapped on the back of the head.
  - `preppy yaung` → `preppy young` — OCR a for o

**#357 · Quetzalcoatl · Text**  
An ancient Mesoamerican god and flying reptile whose name means "feathered ~~serpent.•~~ **serpent."** It has been claimed since the 16th century that Aztec leader Montezuma II believed the appearance of Spanish conquistador ~~Hern~n Cort~s~~ **Hernán Cortés** signaled his return.
  - `serpent.•` → `serpent."` — stray • stood in for closing quote
  - `Hern~n Cort~s` → `Hernán Cortés` — OCR ~ for accented á/é

**#359 · Balki Bartokomous · Text**  
A character from the sitcom Perfect Strangers. He is a rustic from the island of Mypos, who Cousin Larry acclimates to big city Chicago. Features of the character include celebrating with the "dance of ~~joy•~~ **joy"** and exclaiming "Don't be ~~ridiculous•~~ **ridiculous"** when it is he who is being ridiculous.
  - `joy•
` → `joy"
` — stray • = closing quote
  - `ridiculous•
` → `ridiculous"
` — stray • = closing quote

**#362 · The astronaut who drove across the country wearing space diapers to kidnap her boyfriend · Text**  
A NASA employee who traveled from Houston to Orlando carrying, according to her wiki, "latex gloves, a black wig, BB pistol, pepper spray, a tan trench coat, 2-pound drilling hammer, rubber tubing, and plastic garbage ~~bags.•~~ **bags."** She denies wearing the undergarments ~~In~~ **in** question.
  - `bags.•` → `bags."` — bullet is OCR for closing quote
  - `undergarments In question` → `undergarments in question` — capital I OCR for lowercase i

**#365 · Colonel Angus · Text**  
A character from an SNL skit played by Christopher Walken. The humor Is derived from the character's gag name that refers to performing oral sex on a woman, e.g. "Sometimes [he] just rubs you the wrong ~~way•~~ **way"** and his stated preference for the Deep South.
  - `wrong way•` → `wrong way"` — bullet is OCR for closing quote

**#366 · Greedo · Text**  
A bounty hunter from the Star Wars franchise. In the original 1977 version of his confrontation with Han Solo at Chalmun's Spaceport Cantina, Han shoots and kills him before he fires a shot. In the film's rerelease, he takes the first shot and misses, leading to the meme "Han shot ~~first.•~~ **first."**
  - `first.•` → `first."` — bullet is OCR for closing quote

**#368 · Chris Hadfield · Text**  
A Canadian astronaut who became the face of NASA while commanding the ISS in 2013. He has a vast social media following, one of the most popular Reddit AMAs of all time, and a hit YouTube video of him covering Bowie's "Space ~~Oddity•~~ **Oddity"** while literally in space.
  - `Oddity•` → `Oddity"` — bullet is OCR for closing quote

**#369 · Admiral Ackbar · Text**  
A fish-like humanoid who commanded the Rebel Alliance's fleet in Star Wars: Episode VI. He planned a sneak attack on the second Death Star as it orbited the forest moon of Endor. Imperial forces knew of the impending assault, leading to his ~~Iconic II ne~~ **iconic line** "It's a trap!"
  - `Iconic II ne` → `iconic line` — "II ne" is OCR split of "line"; capital I OCR for i

**#374 · The Last Unicorn · Text**  
The single-horned title character from an ~~BOs~~ **80s** animated film, who discovers that she is the only remaining member of her species. Voiced by Mia Farrow, she is pursued by a creature ~~ca lied~~ **called** the Red Bull. Defeating him, she returns her kind back into the world.
  - `an BOs animated` → `an 80s animated` — BOs is OCR for 80s
  - `ca lied` → `called` — OCR split/misread of "called"

**#375 · Florida Man · Text**  
The combined exploits of folks from the Sunshine State, collected in a popular Twitter profile. Examples include someone who "Disguises Himself As 'The Sun: Steals Logo Towel" and someone who "Accidentally Shoots Himself in the Head While Celebrating New Year's ~~Eve.•~~ **Eve."**
  - `Eve.•` → `Eve."` — bullet is OCR for closing quote

**#378 · Samson · Text**  
A Biblical hero and proto-suicide bomber, who once slew an entire army with the jawbone of an ass. God commanded him not to cut his hair, but his lover Delilah was bribed into shaving it, leading to his imprisonment, blinding, and suicide by pulling down a ~~Phlllstlne~~ **Philistine** temple.
  - `Phlllstlne` → `Philistine` — multiple l OCR for i

**#379 · David Foster Wallace · Text**  
A writer best known for his novel Infinite Jest and essays on American culture.' Suffering from depression,• he hanged himself in 2008 after ceasing to take the antidepressant phenelzine. ~~(1]~~ **(1)** He covered a prolific ~~ranga~~ **range** of topics, from ~~cruln~~ **cruise** ship ~~cult\Jre~~ **culture** to tennis pro Roger ~~Faderer.~~ **Federer.** (2) His ~~fattier~~ **father** reports this was a lifelong condition.
  - `(1]` → `(1)` — bracket mismatch, footnote parenthesis
  - `ranga` → `range` — a OCR for e
  - `cruln ship cult\Jre` → `cruise ship culture` — OCR garble of "cruise ship culture"
  - `Faderer` → `Federer` — Roger Federer, a OCR for e
  - `fattier` → `father` — OCR misread of "father"

**#380 · A Honey Badger · Text**  
An animal, native to South Africa and related to the weasel, made popular by a YouTube video narrated by "Randall." This animal is now almost always described as "Badass" and ~~"Cra-zy.•~~ **"Cra-zy."** Furthermore, it's often noted that this animal don't care or really doesn't give a shit.
  - `Cra-zy.•` → `Cra-zy."` — bullet is OCR for closing quote

**#382 · Dr. Zaius · Text**  
An orangutan from the Planet of the Apes. Living ~~In~~ **in** the East Coast Ape City during the 40th century, he paradoxically serves as Minister of Science and Chief Defender of the Faith. He was immortalized in a song from The Simpsons that parodies Falco's "Rock Me Amadeus."
  - `Living In the East Coast` → `Living in the East Coast` — capital I OCR for lowercase i

**#383 · Sneezing Baby Panda · Text**  
The subject of a viral video first uploaded on YouTube ~~In~~ **in** 2006 and emblematic of cute culture. It stars a mother and infant from the fuzzy, bear-like species. The infant expels air from its nose to the surprise of the mother. The video has been viewed more than 200 million times.
  - `YouTube In 2006` → `YouTube in 2006` — capital I OCR for lowercase i

**#386 · Howard Hughes · Text**  
A business magnate and aviator, who set world air speed records and created the failed "Spruce ~~Goose.•~~ **Goose."** He suffered from extreme germophobia and OCD, leading to rumors of him refusing to cut his hair, wearing tissue boxes as shoes, and storing his urine in jars.
  - `Goose.•` → `Goose."` — bullet is OCR for closing quote

**#390 · Brian Boitano · Text**  
A figure skater who won Olympic gold ~~In~~ **in** 1988, but is perhaps now most famous as a semi-recurring character in the South Park franchise. In their feature film. the boys parody him as inspirational figure with a song that references 'What Would Jesus Do?"
  - `gold In 1988` → `gold in 1988` — capital I OCR for lowercase i

**#393 · Lisa "Left Eye,, Lopes · Person**  
Lisa "Left ~~Eye,,~~ **Eye"** Lopes
  - `Eye,,` → `Eye"` — double comma is OCR for closing quote

**#395 · Jacob the Jeweler · Text**  
Purveyor of ~~bli ng~~ **bling** to the rich and famous. He supplied Kanye West's Jesus Piece-and was asked by Kanye, in "Diamonds from Sierra Leone" not to lie about the source of his diamonds. He was sentenced to prison for his connection to the Detroit-based Black Mafia Family.
  - `bli ng` → `bling` — stray space inside word

**#396 · Levar Burton · Text**  
An actor who played the blind, VISOR-wearing Chief Engineer Geordi La Forge on Star Trek: The Next Generation. He is also the driving force behind Reading Rainbow, which recently raised slightly more than Monikers on ~~Klckstarter~~ **Kickstarter** ($5.4M).
  - `Klckstarter` → `Kickstarter` — l OCR for i

**#398 · Dick Cheney's pacemaker · Text**  
The device regulating the heart rhythms of the 46th Vice President of the US, who was infamous for expanding the powers of his office as well as shooting his best friend in the face. He had its ~~wire less~~ **wireless** services disabled to prevent terrorists from potentially ~~Interfering~~ **interfering** with ~~It.~~ **it.**
  - `wire less services` → `wireless services` — stray space inside word
  - `potentially Interfering with It.` → `potentially interfering with it.` — capital I OCR for lowercase i

**#399 · Zelda Fitzgerald · Text**  
A Jazz Age novelist and wife of the author of The Great Gatsby, who described her as the "first American ~~Flapper.•~~ **Flapper."** They were also one of the first celebrity couples of the 20th century, and their marriage was notorious for its ~~alcohol ism,~~ **alcoholism,** recriminations, and instability.
  - `Flapper.•` → `Flapper."` — bullet is OCR for closing quote
  - `alcohol ism` → `alcoholism` — stray space inside word

**#402 · Harriet Tubman · Text**  
An escaped slave who became a prominent abolitionist and spy during the Civil War. She rescued more than 70 slaves with the help of the Underground Railroad, earning her the nickname ~~"Moses.•~~ **"Moses."** Later in her life she became a prominent figure in the suffrage movement.
  - `Moses.•` → `Moses."` — bullet is OCR for closing quote

**#404 · Mrs. O'Leary's Cow · Text**  
The farm animal blamed for the Great Chicago Fire of 1871, who allegedly knocked over a lantern while being milked. The bovine and its owner were posthumously exonerated, though not before inspiring Brian Wilson to write a song about its ~~pyroki netic~~ **pyrokinetic** abilities.
  - `pyroki netic` → `pyrokinetic` — stray space inside word

**#408 · Archduke Franz Ferdinand · Text**  
The presumptive heir to the ~~Austro-Hungarlan~~ **Austro-Hungarian** Empire ~~untll~~ **until** his assassination in 1914. This acted as the catalyst for the beginning of World War I. He was an avid hunter. keeping a diary of nearly 300,000 kills-100,000 of which were displayed at his castle in Konopi~~.
  - `Austro-Hungarlan` → `Austro-Hungarian` — l OCR for i
  - `untll` → `until` — ll OCR for ti

**#409 · Clarence Thomas · Text**  
A Supreme Court Justice who is known for never questioning ~~appel I ants~~ **appellants** during oral arguments. His appointment was clouded by allegations of his sexual harassment, such as asking "Who has put pubic hair on my Coke?" and referencing the porn star Long Dong Silver.
  - `appel I ants` → `appellants` — OCR split/misread of "appellants"

**#418 · A Bassoonist · Text**  
A person who plays a large double reeded woodwind. Despite ~~Its~~ **its** warm, dark tone, it is often considered one of the most obscure instruments in the modern orchestra. Among its most famous passages is the Grandfather's Theme in Sergei Prokofiev's Peter and the Wolf.
  - `Despite Its warm` → `Despite its warm` — capital I OCR for lowercase i

**#419 · Grizzly Man (Timothy Treadwell) · Text**  
The eccentric subject of a Werner Herzog documentary, who lived with Alaskan bears for 13 summers and was "in love with [his] animal ~~friends.·~~ **friends."** In 2003, he and his girlfriend were killed and eaten by one of the bears-the first such death in the park's history.
  - `friends.·` → `friends."` — middle dot is OCR for closing quote

**#420 · Joyce Carol Oates · Text**  
An American novelist, playwright, and Princeton professor. Her works in "In a Region of ~~Ice•~~ **Ice"** and "A Garden of Earthly Delights" and nearly 40 other novels. Born in 1938, she ~~stil I~~ **still** writes in longhand and her productivity and discipline are legendary among writers.
  - `In a Region of Ice•` → `In a Region of Ice"` — • is OCR artifact for closing quote
  - `she stil I writes` → `she still writes` — wrongly split word; capital I for l

**#421 · John Philip Sousa · Text**  
A composer and conductor known as "The March ~~King.•~~ **King."** He created many marches still in use today, such as "The Stars and Stripes ~~Forever.•~~ **Forever."** He also designed a large brass instrument that wraps around the body of the musician, which he named after himself.
  - `The March King.•` → `The March King."` — • is OCR artifact for closing quote
  - `Stars and Stripes Forever.•` → `Stars and Stripes Forever."` — • is OCR artifact for closing quote

**#423 · Grizzly Adams · Text**  
A legendary 19th century mountain man, who was famous for fighting and capturing bears. During a "play fight" with one of his bears, his scalp was dislodged, leaving the brain tissue permanently exposed. He died after a monkey bit into the open wound, causing an ~~Infection.~~ **infection.**
  - `causing an Infection.` → `causing an infection.` — erroneous capital I mid-sentence

**#424 · Patient Zero · Text**  
The medical term for ~~Gai!tan~~ **Gaëtan** Dugas, a Canadian flight attendant who was among a group of homosexual men that traveled widely and were very sexually active, facilitating the early spread of the virus. This term now refers to the first case of a condition more generally.
  - `Gai!tan Dugas` → `Gaëtan Dugas` — diacritic mangled by OCR; real name Gaëtan

**#426 · A LARPer · Text**  
A person who assumes the persona of a character ~~In~~ **in** a ~~fl ct Iona I~~ **fictional** setting, often created by them. The concept was inspired by Dungeons & Dragons and other early roleplaying games, but spans genres from high fantasy to steampunk to zombie apocalypse.
  - `In a fl ct Iona I setting` → `in a fictional setting` — garbled OCR of 'fictional'; erroneous capital I

**#428 · Juan Valdez · Text**  
The fictional mascot of the National Federation of Coffee Growers of Colombia. With his mule Conchita, he is a national symbol for Colombian coffee. Played by Carlos ~~Sclinchez~~ **Sánchez** and others, his tagline, ~~iDisfrute~~ **¡Disfrute** de un buen cafe! has been widely parodied in pop culture.
  - `Carlos Sclinchez` → `Carlos Sánchez` — garbled OCR of actor name Sánchez
  - `iDisfrute` → `¡Disfrute` — leading 'i' is OCR of inverted exclamation ¡

**#433 · Marina Abramovic · Text**  
An artist known for her physically demanding performance pieces. In The Artist is Present, she sat staring at museumgoers silently for two months. Over her career, she has been groped, scalded, nearly stabbed, nearly raped, and nearly shot ~~durl ng~~ **during** performances.
  - `shot durl ng performances` → `shot during performances` — wrongly split; capital I for i

**#435 · Terri Schiavo · Text**  
The subject of a prolonged legal case over whether to terminate ~~I lfe~~ **life** support. Diagnosed as being in a persistent vegetative state by her doctors, her husband and ~~pa rents~~ **parents** battled over whether to remove her feeding tube, despite her having signed a "do not resuscitate" order.
  - `terminate I lfe` → `terminate life` — garbled OCR of 'life'
  - `husband and pa rents` → `husband and parents` — wrongly split word

**#436 · Mike Hunt · Text**  
A gag name that references female genitalia, used to trick a person ~~Into~~ **into** saying it without knowledge of the double meaning. While popularized by the film Porky's, its first use was by Jim Davidson & John Elmo in their series of prank ~~cal Is~~ **calls** to Jersey City's Tube Bar in the 70s.
  - `trick a person Into` → `trick a person into` — erroneous capital I mid-sentence
  - `prank cal Is to` → `prank calls to` — garbled OCR of 'calls'

**#439 · R. Kelly · Text**  
An R&B musician who recorded "I Believe I Can Fly" and "Trapped in the ~~Closet.•~~ **Closet."** In 2002, a video leaked of him allegedly urinating on an underage girl, according a 21-count indictment. He was found not guilty, though many still believe him to be a sexual predator.
  - `the Closet.•` → `the Closet."` — • is OCR artifact for closing quote

**#441 · Joan of Arc · Text**  
The Maid of ~~Orll!ans~~ **Orléans** and 15th century martyr who claimed God instructed her to take back France from the English. After predicting several military outcomes, she was given a substantial role in strategic decision-making. She was eventually captured and burned at the stake.
  - `The Maid of Orll!ans` → `The Maid of Orléans` — diacritic mangled by OCR; real name Orléans

**#447 · Schrodinger's Cat · Text**  
A thought experiment where this feline is both alive and dead due to quantum entanglement. It was originally used to critique an interpretation of quantum mechanics, but now appears often in popular culture, ranging from A Serious Man to ~~Vu-Gi-Ohl~~ **Yu-Gi-Oh!** GX.
  - `Vu-Gi-Ohl GX` → `Yu-Gi-Oh! GX` — V for Y OCR misread; 'Ohl' is 'Oh!'

**#448 · Mr. Wizard · Text**  
The eponymous host of a children's science show, who Bill Nye credited with creating a generation of US scientists. A popular ~~VouTube~~ **YouTube** supercut shows him being "a dick" to kids on the show, sarcastically asking questions like "Haven't you ever seen a sliced banana before?"
  - `A popular VouTube` → `A popular YouTube` — V for Y OCR misread

**#449 · Double Rainbow Guy · Text**  
The moniker of Paul ~~"Vosemitebear"~~ **"Yosemitebear"** Vasquez, a one-time MMA fighter (0-1) and ~~VouTube~~ **YouTube** star who reacts to prismatic ~~I ight,~~ **light,** noting that there are two of them and that they are ~~•so intense.•~~ **"so intense."** As he breaks down into tears he asks "What does this mean?"
  - `Paul "Vosemitebear"` → `Paul "Yosemitebear"` — V for Y OCR misread
  - `and VouTube star` → `and YouTube star` — V for Y OCR misread
  - `prismatic I ight` → `prismatic light` — garbled OCR of 'light'
  - `•so intense.•` → `"so intense."` — • is OCR artifact for quote marks

**#456 · Grumpy Cat · Text**  
The internet name for Tardar Sauce, a feline who gained celebrity due to her permanently negative expression. Her owner attributes her appearance to feline dwarfism as well as an underbite. In 2013, she appeared on the front pages of The Wall Street Journal & ~~NV~~ **NY** Magazine.
  - `NV Magazine` → `NY Magazine` — V for Y OCR misread

**#461 · A Reptilian · Text**  
A humanoid common in conspiracy theories about a race of shapeshifting lizard people who control governments around the world. On a 2011 radio show, Louis C.K. once repeatedly asked former ~~us~~ **US** Secretary of Defense Donald Rumsfeld ~~lf~~ **if** he was one of these.
  - `former us` → `former US` — lost capitalization of US
  - `Rumsfeld lf he` → `Rumsfeld if he` — 'lf' is OCR of 'if'

**#463 · A Boss · Text**  
An internet catchphrase that ~~signa Is~~ **signals** a person being like one of these, normally used after completing an activity with particular skill. The term originated in a song by Slim Thug and was featured in a subsequent parody version from the comedy group The Lonely Island.
  - `that signa Is` → `that signals` — garbled OCR of 'signals'

**#466 · Chris Farley · Text**  
An overweight comedian known for his iconic roles on TV and film. He portrayed a guy who "lives in a van down by the river," a "fat guy in a little ~~coat,»~~ **coat,"** and sometimes just a guy who falls down and breaks things. He died of a cocaine and morphine overdose at 33.
  - `little coat,»` → `little coat,"` — » is OCR artifact for closing quote

**#468 · Lil Bub · Text**  
A cat celebrity known for her "perma-kitten" appearance, whose tongue hangs out because of a short lower jaw and toothlessness. Her appetite is unaffected. Her owner, Mike, studied reiki to care for her and ~~cal Is~~ **calls** her "a fantastic waddler."
  - `her and cal Is her` → `her and calls her` — garbled OCR of 'calls'

**#470 · Sad Keanu · Text**  
A 2010 meme based on a photo of the actor known for his starring roles in Speed, Point Break, The ~~Matrhc,~~ **Matrix,** and other blockbusters. He is shown sitting on a bench by himself, eating a sandwich, and looking forlorn. The action figure of this comes ~~In~~ **in** two sizes: Teeny and Little.
  - `The
Matrhc, and` → `The
Matrix, and` — garbled OCR of 'Matrix'
  - `comes In two` → `comes in two` — erroneous capital I mid-sentence

**#471 · Xena, Warrior Princess · Text**  
The title character of the cult classic TV show starring New Zealand actor Lucy Lawless. The show was a spinoff of Hercules: The Legendary Journeys and featured her weekly adventures and pursuit of the ~~«greater~~ **"greater** good" in a mythological version of Ancient Greece.
  - `«greater good"` → `"greater good"` — « is OCR artifact for opening quote

**#474 · Ruth Bader Ginsburg · Text**  
A Supreme Court Justice known for her advocacy for women's rights and collection of jabots, a lace neck ruffle. She has a fervid online following, with tumblrs dedicated to images of her with captions such as ~~"Notorious•~~ **"Notorious"** and ~~«All~~ **"All** them fives need to listen when a ten is talking."
  - `"Notorious• and «All them` → `"Notorious" and "All them` — • and « are OCR artifacts for quote marks

---
## Uncertain — please confirm

**#8 · Kobayashi · Text**  
  - `(HOB)` → `(HDB)` — standard abbreviation for Hot Dogs and Buns is HDB; D likely scanned as O

**#10 · Sylvia Plath · Text**  
  - `un llt oven` → `unlit oven` — word wrongly split and 'i' scanned as 'l'
  - `head
Into` → `head
into` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#12 · Pablo Escobar · Text**  
  - `Medellfn` → `Medellín` — accented í misread as 'f' (city is Medellín)

**#13 · El Chupacabra · Text**  
  - `cryptld Is often` → `cryptid is often` — 'l' misread for 'i' in cryptid; 'Is' wrongly capitalized mid-sentence

**#19 · Hitler's Brain · Text**  
  - `FClhrer's` → `Führer's` — 'ü' misread as 'Cl' (der Führer)

**#22 · Che Guevara · Text**  
  - `rebellious Image` → `rebellious image` — mid-sentence word wrongly capitalized (OCR capital-I artifact)
  - `Guerril lero` → `Guerrillero` — word wrongly split

**#27 · Shirtless Vladimir Putin · Text**  
  - `urns In the` → `urns in the` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#29 · Baby Jessica · Text**  
  - `godfathers.•"` → `godfathers."` — stray bullet character before closing quote

**#36 · Oscar Pistorius · Text**  
  - `an Intruder` → `an intruder` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#37 · Leeroy Jenkins · Text**  
  - `going all<` → `going AFK` — corrupted token with stray '<'; Leeroy Jenkins lore is 'going AFK'
  - `hel I` → `hell` — word wrongly split; 'l' scanned as 'I'
  - `chicken.•"` → `chicken."` — stray bullet character before closing quote

**#39 · Elian Gonzalez · Text**  
  - `an International Incident` → `an international incident` — mid-sentence words wrongly capitalized (OCR capital-I artifact)

**#42 · Charlton Heston · Text**  
  - `in the BOs` → `in the 80s` — 8 misread as B and 0 as O

**#44 · Mr. Trololo · Text**  
  - `•1 Am Glad` → `"I Am Glad` — stray bullet was opening quote; digit 1 misread for capital I

**#47 · A Communist · Text**  
  - `Union In the` → `Union in the` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#50 · Richard Pryor · Text**  
  - `In a wellknown` → `In a well-known` — hyphen lost at line break, joining 'well-known'

**#52 · An Illusionist · Text**  
  - `Arrested Development.
whose` → `Arrested Development,
whose` — comma misread as period (clause continues with lowercase 'whose')

**#56 · Tonya Harding · Text**  
  - `whacking It with` → `whacking it with` — mid-sentence word wrongly capitalized (OCR capital-I artifact)

**#58 · Prince · Text**  
  - `contained S pounds` → `contained 5 pounds` — letter S misread for digit 5

**#69 · Man Hands · Text**  
  - `a beautiful women` → `a beautiful women` — flagged only, unchanged: 'a beautiful women' reads as 'woman' but e/a is not a standard OCR misread; likely original text

**#77 · A Grammar Nazi · Text**  
  - `"thus.•"` → `"thus."` — removed stray bullet artifact adjacent to closing quote

**#79 · Hannibal Lector · Person**  
  - `Lector` → `Lector` — flagged only, unchanged: real character is 'Lecter'; e/o not a standard OCR misread, may be the game's spelling

**#107 · A TSA Agent · Text**  
  - `a us Department` → `a us Department` — flagged only, unchanged: likely should be 'US' (other cards use 'US'), but lowercasing is not a clear OCR letter-misread

**#114 · Cthulhu · Text**  
  - `has the the arms` → `has the the arms` — flagged only, unchanged: duplicated 'the'; could be original typo, removing a word would change wording

**#116 · A Fainting Goat · Text**  
  - `formally knows as` → `formally knows as` — flagged only, unchanged: reads as 'known as'; s/n not a standard OCR misread, likely original typo

**#127 · George Washington · Text**  
  - `of the us.` → `of the US.` — OCR lowercased the acronym US
  - `no Joke,` → `no joke,` — Capital J misread for lowercase j mid-sentence

**#129 · Goatse · Text**  
  - `hello.Jpg` → `hello.jpg` — Capital J misread for lowercase j in file extension
  - `, .ex.` → `, .cx.` — Christmas Island TLD is .cx; c misread as e

**#144 · William Shatner · Text**  
  - `A legendary actor. who` → `A legendary actor, who` — Comma misread as period (lowercase word follows)
  - `TJ Hooker. the` → `TJ Hooker, the` — Comma misread as period (lowercase word follows)

**#174 · Tom Selleck,s mustache · Text**  
  - `and sos style Icon.` → `and 80s style icon.` — '80s' misread as 'sos'; capital I misread for lowercase i
  - `Icon. He Is most` → `icon. He is most` — Capital I misread for lowercase i

**#198 · A Nihilist · Text**  
  - `thugs In The` → `thugs in The` — spurious capital I on 'in'
  - `Lebowskl.` → `Lebowski.` — trailing l misread for i

**#199 · Phineas Gage · Text**  
  - `In his` → `in his` — spurious capital I on 'in'

**#200 · Ricardo Montalban · Text**  
  - `C6rdoba` → `Cordoba` — digit 6 misread for o (Chrysler Cordoba)
  - `•tastefulness of its appearance•` → `"tastefulness of its appearance"` — bullet chars are OCR misreads of quotation marks
  - `Its "soft` → `its "soft` — spurious capital I on 'its'
  - `Corl nth Ian` → `Corinthian` — 'Corinthian' broken into pieces with l/I misreads
  - `leather.•` → `leather."` — bullet char is OCR misread of closing quote

**#201 · A Redshirt · Text**  
  - `who Is Introduced` → `who is introduced` — spurious capitals on 'is' and 'introduced'

**#202 · David Attenborough · Text**  
  - `protests on line.` → `protests online.` — 'online' wrongly split into two words

**#204 · The Id · Text**  
  - `One of the the three` → `One of the three` — duplicated word 'the'
  - `Th is part` → `This part` — 'This' wrongly split

**#207 · A Man from Nantucket · Text**  
  - `could suck It.•` → `could suck it."` — spurious capital I on 'it'; bullet is OCR misread of closing quote

**#208 · Bobby Fischer · Text**  
  - `dying In Iceland In 2008` → `dying in Iceland in 2008` — spurious capital I on both 'in'

**#220 · Tycho Brahe · Text**  
  - `part of h ls nose In a duel` → `part of his nose in a duel` — 'his' split with l/i misread; spurious capital I on 'in'

**#226 · Robert Hamilton · Text**  
  - `painter In the` → `painter in the` — spurious capital I on 'in'

**#227 · Dramatic Chipmunk · Text**  
  - `elicit material` → `elicit material` — 'elicit' possibly should be 'illicit', but may be source's own wording; left unchanged

**#235 · Judas Iscariot · Text**  
  - `Ideals.` → `ideals.` — spurious capital I on 'ideals'

**#237 · Siri · Text**  
  - `on IOS operation` → `on iOS operation` — 'iOS' miscapitalized as IOS
  - `addiction•` → `addiction"` — bullet char is OCR misread of closing quote

**#238 · Silvio Berlusconi · Text**  
  - `bunga," It is rumored` → `bunga," it is rumored` — spurious capital I on 'it' following comma

**#239 · The Dread Pirate Roberts · Text**  
  - `in the The Princess` → `in The Princess` — duplicated article 'the'
  - `brigand Is` → `brigand is` — spurious capital I on 'is'

**#255 · Skeletor · Text**  
  - `He ls the` → `He is the` — 'ls' misread for 'is'

**#256 · Star Wars Kid · Text**  
  - `student Imitating` → `student Imitating` — flagged, left unchanged: 'Imitating' capital I mid-sentence, possibly should be 'imitating'

**#258 · Montezuma · Text**  
  - `His "revenge•` → `His "revenge"` — bullet misread of closing quotation mark

**#269 · The Superego · Text**  
  - `One of the the three` → `One of the the three` — flagged, left unchanged: duplicated 'the'

**#284 · Prancer · Text**  
  - `The N lght Before` → `The Night Before` — OCR split/misread of 'Night'
  - `Christmas.•"` → `Christmas."` — stray bullet before closing quote removed

**#285 · Hal-9000 · Person**  
  - `Hal-9000` → `Hal-9000` — flagged, left unchanged: character is commonly styled 'HAL 9000'

**#287 · Ch airy · Text**  
  - `An iconic characters` → `An iconic characters` — flagged, left unchanged: 'characters' possibly should be 'character'

**#288 · The elephant that Thomas Edison electrocuted (Topsy) · Text**  
  - `her trainer. she was` → `her trainer. she was` — flagged, left unchanged: period likely a comma, or 'she' should be capitalized

**#290 · Mother Teresa · Text**  
  - `in calcutta` → `in calcutta` — flagged, left unchanged: proper noun 'Calcutta' not capitalized

**#292 · Lennie Small · Text**  
  - `George In Of Mice` → `George In Of Mice` — flagged, left unchanged: 'In' possibly should be lowercase 'in'

**#295 · The Obermensch · Person**  
  - `Obermensch` → `Obermensch` — flagged, left unchanged: Nietzsche term is 'Übermensch/Ubermensch'

**#296 · The Dude · Text**  
  - `an unemplayed` → `an unemployed` — 'a' misread for 'o' in 'unemployed'

**#303 · A Never Nude · Text**  
  - `sti II not` → `still not` — OCR split
  - `` → `` — 'Fanke' is likely the character 'Tobias Fünke' (left unchanged — confirm)

**#313 · Right Said Fred · Text**  
  - `yeah I I shake` → `yeah I shake` — OCR doubled I
  - `` → `` — 'Fairbrassin brothers' is likely 'Fairbrass brothers' (left unchanged — confirm)

**#323 · Pharell's hat · Person**  
  - `` → `` — 'Pharell' is likely 'Pharrell' (Williams) (left unchanged — confirm)

**#330 · A Bottom · Text**  
  - `` → `` — '32% of us respondents' — 'us' is likely small-caps 'US' (left unchanged — confirm)

**#355 · Bees! · Text**  
  - `` → `` — 'hives knows as colonies' likely 'known as' (left unchanged — confirm)

**#362 · The astronaut who drove across the country wearing space diapers to kidnap her boyfriend · Text**  
  - `bags.•` → `bags."` — bullet is OCR for closing quote
  - `undergarments In question` → `undergarments in question` — capital I OCR for lowercase i

**#369 · Admiral Ackbar · Text**  
  - `Iconic II ne` → `iconic line` — "II ne" is OCR split of "line"; capital I OCR for i

**#379 · David Foster Wallace · Text**  
  - `(1]` → `(1)` — bracket mismatch, footnote parenthesis
  - `ranga` → `range` — a OCR for e
  - `cruln ship cult\Jre` → `cruise ship culture` — OCR garble of "cruise ship culture"
  - `Faderer` → `Federer` — Roger Federer, a OCR for e
  - `fattier` → `father` — OCR misread of "father"

**#382 · Dr. Zaius · Text**  
  - `Living In the East Coast` → `Living in the East Coast` — capital I OCR for lowercase i

**#383 · Sneezing Baby Panda · Text**  
  - `YouTube In 2006` → `YouTube in 2006` — capital I OCR for lowercase i

**#390 · Brian Boitano · Text**  
  - `gold In 1988` → `gold in 1988` — capital I OCR for lowercase i

**#398 · Dick Cheney's pacemaker · Text**  
  - `wire less services` → `wireless services` — stray space inside word
  - `potentially Interfering with It.` → `potentially interfering with it.` — capital I OCR for lowercase i

**#408 · Archduke Franz Ferdinand · Text**  
  - `Austro-Hungarlan` → `Austro-Hungarian` — l OCR for i
  - `untll` → `until` — ll OCR for ti

**#418 · A Bassoonist · Text**  
  - `Despite Its warm` → `Despite its warm` — capital I OCR for lowercase i

**#423 · Grizzly Adams · Text**  
  - `causing an Infection.` → `causing an infection.` — erroneous capital I mid-sentence

**#424 · Patient Zero · Text**  
  - `Gai!tan Dugas` → `Gaëtan Dugas` — diacritic mangled by OCR; real name Gaëtan

**#426 · A LARPer · Text**  
  - `In a fl ct Iona I setting` → `in a fictional setting` — garbled OCR of 'fictional'; erroneous capital I

**#428 · Juan Valdez · Text**  
  - `Carlos Sclinchez` → `Carlos Sánchez` — garbled OCR of actor name Sánchez
  - `iDisfrute` → `¡Disfrute` — leading 'i' is OCR of inverted exclamation ¡

**#436 · Mike Hunt · Text**  
  - `trick a person Into` → `trick a person into` — erroneous capital I mid-sentence
  - `prank cal Is to` → `prank calls to` — garbled OCR of 'calls'

**#441 · Joan of Arc · Text**  
  - `The Maid of Orll!ans` → `The Maid of Orléans` — diacritic mangled by OCR; real name Orléans

**#470 · Sad Keanu · Text**  
  - `The
Matrhc, and` → `The
Matrix, and` — garbled OCR of 'Matrix'
  - `comes In two` → `comes in two` — erroneous capital I mid-sentence
