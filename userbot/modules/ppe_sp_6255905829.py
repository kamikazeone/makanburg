@register(outgoing=True, pattern=r"^.gs (.*)")
async def gsearch(event):
    """ For .google command, do a Google search. """
    if not q_event.text[0].isalpha() and q_event.text[0] not in (
            "/", "#", "@", "!"):
    search_str = event.pattern_match.group(1)
	await event.edit("**Searching for "+search_str+" ...**")
	res = get("https://www.startpage.com/do/search?cmd=process_search&query={}".format(search_str), 'html')
	src = BeautifulSoup(res.text,'lxml')

	msg = "**Search Query** \n`"+search_str+"`\n**Results**\n"

	for result in src.find_all('a', {'class': 'w-gl__result-title'}):
		msg = msg + "⁍ ["+result.text+"]("+result['href']+")\n\n"

	await event.edit(msg,link_preview=False)	