import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # Sports Puzzle Clue Practice

        Use this short notebook to turn daily sports puzzles into a repeatable recall exercise.

        ## NFL player clues

        Start with position, then conference, team identity, and career history. Test the method with the daily [NFL Wordle player puzzle](https://wordlecup.today/en/nfl/).

        ## Football logo recall

        Separate shape, color, lettering, and regional symbols. Use the [football logo memory game](https://wordlecup.today/en/football/) for a focused visual drill.

        ## Basketball player profiles

        Group clues by position, era, franchise, and nationality. The [basketball player puzzle](https://wordlecup.today/en/basketball-wordle/) gives six attempts to apply the worksheet.

        ## Review routine

        1. Record the first two candidates.
        2. Cross out a candidate only when a clue conflicts.
        3. Note which clue changed the shortlist most.
        4. Save one error as tomorrow's review cue.
        """
    )
    return


if __name__ == "__main__":
    app.run()

