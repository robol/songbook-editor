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
        
        # We really have to assume that latex_song is unicode, 
        # or the write() function will eat us!
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
        
        # Transform chords in LaTeX Chords
        latex_song = re.sub("\[", "\\Ch{", latex_song)
        latex_song = re.sub("\](\w|\s)(\w|\s)(\w|\s)", self.quadra_to_chord_end, latex_song)
        latex_song = re.sub("\]", "}{}", latex_song)
        
        return latex_song
        
    def quadra_to_chord_end(self,m):
        st = "}{" + m.group(1) + m.group(2) + m.group(3) + "}"
        return st
