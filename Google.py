from telethon import functions
from userbot.events import register

@register(outgoing=True, pattern=r"^.google (.*)")

async def gsearch(q_event):

    """ For .google command, Do a Google search. """

    if not q_event.text[0].isalpha() and q_event.text[0] not in (

            "/", "#", "@", "!"):

        await q_event.edit("PPE is Getting Information From Google Please Wait... ✍️🙇")

        match_ = q_event.pattern_match.group(1)

        match = quote_plus(match_)

        result = ""

        chrome_options = Options()

        chrome_options.add_argument("--headless")

        chrome_options.add_argument("--disable-dev-shm-usage")

        chrome_options.add_argument("--no-sandbox")

        chrome_options.add_argument("--disable-gpu")

        chrome_options.binary_location = GOOGLE_CHROME_BIN

        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)

        for i in search(match, stop=10):

            driver.get(i)

            title = driver.title

            result += f"🔎{title}\nLink: {i}\n\n"

        await q_event.edit(

            "Google Search Query:\n\n" + match_ + "\n\nResults:\n\n" + result,

            link_preview = False

            )

        if BOTLOG:

            await q_event.client.send_message(

                BOTLOG_CHATID,

                "Google Search query " + match_ + " was executed successfully",

            )