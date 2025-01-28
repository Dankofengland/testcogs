import discord
from redbot.core import commands
import random

class CallOfDuty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.phrases = [
            "Stay frosty.",
            "Mission accomplished, good work.",
            "Time to earn your bread, grunts.",
            "We're Oscar Mike!",
            "Soap, this is going to get rough.",
            "You know the drill.",
            "Keep your eyes open.",
            "They think they can win with numbers?",
            "All in a day's work.",
            "Victory is ours.",
        ]

    @commands.command(name="callofduty")
    async def call_of_duty(self, ctx):
        """Reply with a random Call of Duty character phrase."""
        phrase = random.choice(self.phrases)
        await ctx.send(phrase)
