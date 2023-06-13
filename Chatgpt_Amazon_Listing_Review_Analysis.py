import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.organization = os.getenv("OPENAI_API_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


review_1 = """I was nervous buying these as I usually Like to try shoes on first.  I called and spoke to an Amazon rep and she was super helpful, so I thought free shipping back, ok I’ll try them, plus they were on sale with a coupon!!  When they first got here they were a Bit snug.  I sat on the sofa and reclined with them on and just wiggled my toes every now and then, they molded to my feet very nicely, with enough wool to cuddle and keep my feet warm.  I especially like how you can wear the flap up, I don’t wear socks, basically ever...so most slippers I had some of my leg exposed between my pants and slipper and that part was cold..not with these, the flap can rise up and it covers so nicely.I was also worried about the sole being too hard.  It’s not.  While it’s not a super bendable sole, it’s sturdy yet still flexible enough for comfort.As far as size..I wear a 9 in most shoes and slippers.  The nine fits me perfectly.  My foot tends to be a little wide but these are just right.Also want to add they have a super nice little piece/loop of leather on the back to help you pull them on.  I haven’t taken them off when I’m inside at all..these re lovely!If anything changes I’ll let you know...my only regret is they don’t have some arch support, but I really like these slippers!****❤️❤️ Just had to write back I think these are the best slippers I’ve owned.  They fur did flatten a little  but more conformed to my foot.  They are SO comfortable.  I usually can’t wear shoes or socks as my feet get too hot, these keep my feet warm with out sweating, they are super durable (as I spilled hot coffee grounds and rinsed them off). While at home they never leave my feet unless I'm in bed.  If the fur flattens too much I’ll add an insole but after constant wear since the day they arrived and the beating they take from me I have to say how super pleased I am am even after a few months...I’ll continue to buy these and I may add a second pair just because I am so happy with them!❤️❤️"""
review_2 = """I love these slippers.  They fit nicely, a size 8 was a size 8, they are comfortable, they are warm.  They are lovely.  I even ordered two other pairs.  Perfect for my new WFH shoes.  So why the one star rating?  Because I've had them barely a month and both shoes have holes in the toes!!! ALREADY!!!  Sure, I'm wearing them literally all day long cuz....COVID!!  WFH!!!  I go nowhere and I see nobody so I only wear slippers.  All day.  Every day.  Now, I'm sure that Dearfoam didn't plan on their products being worn 14-16 hours per day but in all fairness to me, it's not like I'm walking anywhere.  I'm sitting at my desk for a good chunk of it.  The rest of the time, they are on the floor next to me while I lounge on the couch.  Most workout they get is the daily traipse to the mail box to see if I got anything interesting.  I would expect that even with that, it should take longer than a month to get holes in the toes.  For $70, I'm less than impressed."""
review_3 = """Wore these once. Pulled them on gently and the paper-thin suede ripped. Needless to say, they’re going back"""
review_4 = """Okay, I feel like I'm in an alternate reality here?! I was so excited for these slippers and even ordered a size up so I could wear with fuzzy socks, and I literally couldn't get my foot in them. I thought I had forgotten to take out some cardboard, but no—I couldn't pull them on. My sister tried and she couldn't get them on either? Also, clumps of the fur kept flying off/shedding while I tried. I've owned Uggs and Minnetonkas before and have never had shedding this badly. I'm SO confused how everyone had such a positive experience, but hey, needed to share?"""
review_5 = """Buyer beware.These run small. I’m a very average size 8, and the 8 on these pinched my toes so bad I had to exchange for a 9. My heel now floats a bit when I walk, but I’m not going to be climbing any mountains in these, so I’m willing to deal. Regardless, that was strike one.There was a cosmetic blemish on the cuff, but since I was planning to wear them folded down, I figure I can deal with that too. However, that’s strike two.Two days, t-w-o days, after wearing them lightly around the house, the stitching tore on the right boot. I’m beyond bummed. Strike three.These do not have any support whatsoever, and the sole is glued in, so it’s not like you can exchange it for a sole with some fluff to it.The suede is very thin and the over quality is on par with $15 slippers you’d find at target. Like, why didn’t I just get another pair from there?? Because I was hoping for quality, last me 5 years, grown up pair of slippers, that’s why. Alas, these aren’t them.They are at best “ok” and look good on paper. However, in practice they are flimsy, sub par quality with an expensive price tag.The one pro: they are in fact warm.My advice: keep searching."""
review_6 = """These are amazingly soft and so comfortable. I wear a size 91/2 and I bought the 10’s and they fit nicely with socks or without, I prefer them without socks. I would say size up if you’re a half size. I won’t be taking these off unless absolutely necessary! They are worth every penny, and really keep your feet warm without sweating.They’re  mid priced slippers, which I had a hard time finding - all I could find were really cheap ones or super expensive ones. Glad I  sifted through the myriad of slippers that Amazon has and found these.I’m not sure why Amazon no longer allows me to post photos? But, they look exactly like their picture, so.....just buy them, you won’t be disappointed.Update: I’ve worn these slippers now for 7 months -every single day and ALL day long . I’ve given them quite the workout - I mean I’ve spilled all sorts of stuff all over them, including bacon grease! So they look a little beat up, but they are still going strong ! I do think new wool insoles are in order.Btw, in the meanwhile I purchased two pairs of Uggs - the Tasman and the Bailey Button 2 - both pairs went right back. They weren’t nearly as comfortable as these."""
review_7 = """I have several pairs of wool slippers, but for some reason my feet have been cold for the last couple of weeks. All my slippers are from LLBean.  It has been cold in North Carolina and I have a lot of tile floors. I decided I needed to buy a  warmer slipper. These are great. I wear a size 6W and purchased these in a size 6. They fit good in the foot part, but are a little tight on the upper part of my foot. I can stretch them a little, but I will just see if this happens naturally. Leather does stretch with time. My feet are  toasty warm. I know these will stretch out as time goes on and I am glad that I went with my usual size. Some people said they went up a size.  My only complaint is the tag that is sewn inside on the heel. It is a little annoying. Can’t understand why they would do that. It is stitched in and there is really no way to take it out. The tag would be much better on the outside of the slipper. I am happy with my purchase. I would order again."""
review_8 = """Typically wear a 9.5 but ordered a 10 based on the reviews and wanted to be able to wear socks with them. I have included a photo of where my toe is in the slippers without socks on. I’m not sure they’re worth $90 but they are nice for keeping my feet warm going outdoors around the house."""
review_9 = """I was definitely looking forward to these. Bought them in a size 9, black and they fit true to size. Snug but in a good way. I have always purchased the LL Bean slippers but was not impressed with how the shearling wore out. Hoping that doesn't happen with these, but I am a little skeptical because as I slipped them on, I did manage to pull out a couple of tufts of shearling without much effort. I very much like the back support which seems strong enough not to fold or droop over time as you slide your foot in.  I also like that they can be worn up, or folded down. My only complaint is that I wish my heel would not pop up every time I walk. Took a few days to get used to it."""
review_10 = """The media could not be loaded.                  Love them! Buy them!I am normally a 7.5 size shoe, I got the 7-8 size. I would size up if over a 7.5. they fit just perfectly on the toe area. I also have a wide feet. So warm and so comfortable. The shoe has a firmness to it, it does feel like a house "shoe". So luxurious, warm and comfy. I bought these with my own money not paid review."""

reviews = [review_1, 
review_2, 
review_3, 
review_4, 
review_5, 
review_6, 
review_7, 
review_8, 
review_9, 
review_10]


for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 
    
    What is the sentiment of the each product review, \ 
which is delimited with triple backticks? First, give your answer as a single word, either "positive" \
or "negative".\

    Summarize the review below in one key word each, delimited by triple \
     backticks in at most 5 key words per review\
    
    Provide them in JSON format with the following keys: "sentiment", \
    "key words". 
    
    Review: ```{reviews[i]}```
    """

    response = get_completion(prompt)
    print(i+1, response, "\n")

