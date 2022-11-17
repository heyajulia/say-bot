# say-bot

This is the code of a Mastodon bot that converts posts to speech.

## Current state

Currently, it converts [this post by me discussing the bot][post] from text to speech. The "bot" side of things is not
yet implemented because:

1. I want to make sure I get everything as close to 100% right as possible from the get-go (see the thread above to read
   my thinking about it)...
2. ...but mostly because I haven't been able to find a great free text-to-speech program. The ones I was able to find
   sound quite robotic, which makes sense, though I think the bot's usefulness as an accessiblity aid is limited if the
   voice it uses is difficult to understand. Run the code or [listen to this clip][clip] and you'll hear what I mean.

   If you know of a replacement that produces more natural speech, please let me know.

   (This is not to say that I think the people who made Festival aren't very talented or that it's useless; I just don't
   think it's applicable in this scenario.)

## Contributing

You can hack on the code using [Visual Studio Code][code]. To run the bot, execute `poetry run python3 src/main.py` in
the integrated terminal. If you'd like to contribute to the code but don't know how, don't be afraid to reach out! I'd
love to help you.

Contributions that _aren't_ code, like thinking about how the bot should work are also tremendously helpful.

## Contact

If you want to contact me, I'd prefer it if you opened an issue on GitHub. You can also find me on Mastodon as
[@julia@mastodon.lol][me].

## License

This code is in the public domain. See [the license](./LICENSE.md) for details.

[post]: https://mastodon.lol/@julia/109357872779540083
[clip]: https://voca.ro/19kDh0fB4ZEy
[code]: https://code.visualstudio.com
[me]: https://mastodon.lol/@julia
