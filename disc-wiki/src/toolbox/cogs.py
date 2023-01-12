from discord.ext import commands

class GalleryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def oc_gallery(self, ctx, *args):
        """ #1
        Gallerie d'un OC (tous les arts le concernant)
        (Première page : statistiques)
        Sélecteur RP, Sélecteur joueur, Sélecteur OC (1-1) avec validation
        Boutons : <-5><-1><Auto/Manuel><+1><+5>
        """
        print("oc_gallery")  
        
    @commands.command()
    async def rp_gallery(self, ctx, *args):
        """ #1
        Gallerie d'un RP (events)
        (Première page : statistiques)
        Sélecteur RP (1-1) 
        Sélecteur type (FB,Illu,plot,mobile,bda,exe,fin)
        avec validation
        Boutons : <-5><-1><Auto/Manuel><+1><+5>
        """
        print("rp_gallery")   

class CharacterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rp_cast(self, ctx, *args):
        """ #1
        Cast d'un RP
        (Première page : statistiques)
        option "mono" pour inclure les monos, "pnj" pour inclure les pnj
        Sélecteur RP (1-1) 
        avec validation
        Boutons : <-5><-1><Switch général/Trivia (5 points)><+1><+5>
        Champs : Icone, Nom, Ultime, Age, DOB, taille, genre, joueur RP, rôle, Like/Dislike
        """
        print("rp_cast")    

    @commands.command()   
    async def player_cast(self, ctx, *args):
        """ #2
        Cast d'un joueur
        (Première page : statistiques)
        option "noplay"
        Sélecteur joueur
        avec validation
        Boutons : <-5><-1><Switch général/Trivia (5 points)><+1><+5>
        Champs : Icone, Nom, Ultime, Age, DOB, taille, genre, joueur RP, rôle, Like/Dislike
        """
        print("player_cast")
    
    @commands.command()
    async def custom_cast(self, ctx, *args):
        """ #3
        Filtre perso pour s'amuser
        (Première page : statistiques)
        Sélecteur filtre
        Sélecteur choix
        Affichage des filtres, validation
        Syntaxe de résultats (a définir)
        """
        print("custom_cast")      

class RpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rp_info(self, ctx, *args):
        """ #1
        Informations générales du RP
        (Première page : statistiques)
        Sélecteur RP avec validation
        Page 1 : dates, admins, MM (général)
        Page 2 : déroulé cases (events/BDA/Tueur)
        Page 3 : Outline du plot
        """
        print("rp_info") 
        
    @commands.command()
    async def rp_mobiles(self, ctx, *args):
        """ #2
        Description d'un mobile
        (Première page : statistiques)
        Sélecteur RP et mobile avec validation
        Page 1 : contexte, explication, éventuel lien vers vidéo
        Page 2 : déroulé
        """
        print("rp_mobiles")  
    
    @commands.command()
    async def rp_events(self, ctx, *args):
        """ #2
        Description des events
        (Première page : statistiques)
        Sélecteur RP et event avec validation
        Page 1 : contexte, explication, éventuel lien vers vidéo
        Page 2 : déroulé
        """
        print("rp_events") 

    @commands.command()
    async def rp_case(self, ctx, *args):
        """ #2
        Description des events
        (Première page : statistiques)
        Sélecteur RP et case avec validation
        Page 1 : contexte, explication générale
        Page 2 : BDA (1 page pour chaque BDA en +)
        Page 3 : Indices
        Page 4 : Déroulé case
        Page 5 : Déroulé meurtre
        Page 6 : Motivations tueur
        Page 7 : exe
        """
        print("rp_case") 

    @commands.command()
    async def rp_plot(self, ctx, *args):
        """ #2
        Description du plot
        (Première page : statistiques)
        Sélecteur RP et case avec validation
        Page 1 : contexte, explication générale
        Page 2 : Events qui s'inscrivent dans le plot
        Page 3 : Indices
        Page 4 : Déroulé case
        Page 5 : Déroulé events
        Page 6 : Motivations des PR (1 page à chaque fois)
        Page 7 : exe
        """
        print("rp_plot")  

class PlayerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def player_desc(self, ctx, *args):
        """ #2
        Décrit un joueur par ses RP
        Sélecteur joueur
        Page 1 : Description générale
        Infos de base + Nombre de RP, nombre de fois MM etc
        Page 2 : Contributions (?)
        """
        print("player_desc")  

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def show_playlist(self, ctx, *args):
        """ #3
        Affiche playlist (?)
        Sélecteur RP
        """
        print("show_playlist")  

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def add_element(self, ctx, *args):
        """ #1
        Ajout élément
        Accompagné d'un Json (?) pour spécifier les ajouts
        """
        print("admin_add")  
        
