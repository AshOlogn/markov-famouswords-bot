# markov-famouswords-bot
This is a Reddit bot that uses Markov chains to randomly generate text resembling speeches/works by significant figures in response to "trigger" words in comments.

## Using the Bot
To trigger the bot's text generation, type !<person's name> somewhere in a comment on the subreddit that the bot is monitoring. For example, to trigger a response using Abraham Lincoln's text, write a comment containing ``!lincoln`` in the subreddit being monitored by the bot.

The following people are already supported by the bot (but you can add more):
* Martin Luther King, Jr. (``!mlk``)
* Winston Churchill (``!churchill``)
* Abraham Lincoln (``!lincoln``)
* Karl Marx (``!marx``)
* Jordan Peterson (``!jordanp``)

## Running the Bot
Before you run the bot, you have to first register it on Reddit's website (https://www.reddit.com/prefs/apps/). Then type in the personal use script in the field ``client_id``, the secret id in ``client_secret``, a descriptive name in ``user_agent``, and your Reddit username and password in the appropriate fields in the blank spaces found in the ``main`` function of the Python script.

To run the bot, type either of the possible commands shown below:
`python markov_speech.py <subreddit>` or
`python markov_speech.py <subreddit> <history_length> <output_size>`,
where `<history_length>` and `<output_size>` are integers, and ``<subreddit>`` is the name of the subreddit you want monitored.

## Adding People
To let your bot generate text for more people, add their associated trigger word (usually shortened form of their name or their last name) without the exclamation point to the file ``_people.txt`` and create a text file of the form ``<trigger_word>.txt`` containing sample text. 

For example, to add Darth Vader to the list of people, you would add some variant of ``vader`` to ``_people.txt`` and create a file ``vader.txt`` containing his quotes/monologues. This would enable the bot to respond with random text based on Vader quotes to comments containing ``!vader``.

If you want to temporarily remove a person from the list, you can "comment out" that person's line in ``_people.txt``, like ``//lincoln`` or ``// mlk``.

