from aoctools.visualization import *
from aoctools.datastruct import vec
import aoctools.visualization as vis
from aoctools.textproc import getints

from random import random
from datetime import datetime
from json import load
from time import sleep


try:
    while True:
        now = datetime.today()

        with open(vis.__path__[0] + "\\aoc_title.txt", "r", encoding="utf-8") as f:
            title_str = f.read()
        with open("data/days.json", "r", encoding="utf-8") as f:
            days = load(f)

        days_summary = []
        tot_stars = 0
        for day, parts in days.items():
            i, *_ = getints(day)
            tot_stars += sum(parts.values())
            part1_star = Text("*", color=(AOC_YELLOW if parts["part1"] else AOC_GRAY))
            part2_star = Text("*", color=(AOC_YELLOW if parts["part2"] else AOC_GRAY))

            date = datetime(2022, 12, i, 6)
            dtime = date - now
            secs = dtime.seconds % 60
            mins = dtime.seconds % 3600 // 60
            hours = dtime.seconds // 3600
            days = dtime.days
            if days == -1:
                datestr = f"opened {60  - secs} seconds, {59 - mins} minute and {23 - hours} hours ago"
            elif days < 0:
                datestr = f"opened {1-days} days ago"
            elif days == 0:
                if hours == 0:
                    if mins == 0:
                        datestr = Text(f"opens in {secs} seconds!!!", bold=True)
                    else:
                        datestr = Text(f"opens in {mins} minutes and {secs} seconds!!")
                else:
                    datestr = Text(f"opens in {hours} hours, {mins} minutes and {secs} seconds!")
            elif days == 1:
                datestr = f"opens in {days} day and {hours} hours"
            else:
                datestr = f"opens in {days} days"

            summary = Text("Day ", str(i).rjust(2), ": " , part1_star, part2_star, " " * 10, Text(datestr, color=AOC_DARKER), "\n", color=AOC_WHITE)
            days_summary.append(summary)

        if tot_stars == 50:
            title_str = "".join(c if c != "$" or random() > 0.3 else "*" for c in title_str)

        title = highlight(title_str, r"/\$+/", Text(color=AOC_GREEN, bold=True))\
            .highlight(r"/[\\/|_]+/", Text(color=AOC_WHITE))\
            .highlight("*", Text(color=AOC_YELLOW, bold=True))


        status = statusbar("Total stars", tot_stars, 50, bg=AOC_GRAY, fg=AOC_YELLOW)
        summary = Text(
            title,
            "\n\n", 
            *days_summary,
            "\n",
            status,
            "\n")
        summary.set_bgcolor(AOC_BG)

        splash = TextBox(summary, vec(0,0))
        splash.pad(2)
        splash.indent(2)


        todaystr = Text("Today: ", now.strftime("%c"), color=AOC_WHITE, bg=AOC_BG)
        todaybxs = TextBox(todaystr, vec(splash.width() - todaystr.width(), 9))
        print_all(splash, todaybxs)
        sleep(0.2)
except KeyboardInterrupt:
    print(splash.bottom_right())

