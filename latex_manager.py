import re

class latex_manager():
    def __init__(self):
        ## TODO: Verify Latex Installation
        print "LaTeX loaded"

    def create_song(self, song):
        # Ci aspettiamo di ottenere un oggetto song
        title = song.title
        tone = song.tone
        mauthor = song.mauthor
        tauthor = song.tauthor
        year = song.year
        body = song.body
        
        latex_song = unicode()
        latex_song += "\\begin{song}{" + title + "}{" + tone + "}\n{" + mauthor + "}\n{" + tauthor + "}\n{" + year + "}" + "{}\n\n\\index{" + title + "}\n\n"

        for item in body:
            if(item.is_chorus()):
                latex_song += "\n\\begin{SBChorus}\n"
                latex_song += re.sub("\n", "\n\n", item.content())
                latex_song += "\n\\end{SBChorus}\n"
            else:
                latex_song += "\n\\begin{SBVerse}"
                latex_song += re.sub("\n" , "\n\n", item.content())
                latex_song += "\n\\end{SBVerse}\n"

        latex_song += "\n\\end{song}\n\n"
        
        latex_song = re.sub("\[", "\\Ch{", latex_song)
        latex_song = re.sub("\]", "}{}", latex_song)
        
        return latex_song
        
