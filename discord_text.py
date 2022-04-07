#Message d'arrivée

    embed=discord.Embed(title="Bonjour! Comment utiliser l'AnimeDuck?", 
                        description="L'AnimeDuck est un bot discord vous permettant de trouver un **Anime** à regarder pendant votre trajet en train! Pour faire fonctionner le bot, entrez la commande suivante :", 
                        color=0xefff14)

    embed.set_author(name="AnimeDuck",
                    icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfoD_B4vEoF5fJ848kNZYB7dtWCrIT85YmVw&usqp=CAU")

    embed.set_thumbnail(url="https://random-d.uk/api/randomimg")

    embed.set_footer(text="/getanime `Adresse + ville de départ` `Adresse + ville d'arrivée`")
                    
    await ctx.send(embed=embed)

#Message de /getanime

    embed=discord.Embed(title="Pour patienter pendant vos transports, nous vous proposons de regarder MANGA_NAME !", 
                        url="https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask", 
                        description="Votre voyage de DEPT_NAME à DEST_NAME dure environ TIME_TO_TRAVEL", 
                        color=0xefff14)

    embed.set_author(name="AnimeDuck", 
                    icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfoD_B4vEoF5fJ848kNZYB7dtWCrIT85YmVw&usqp=CAU")

    embed.set_thumbnail(url="")

    embed.set_footer(text="Nous vous remercions pour l'utilisation de notre bot! Passez un agréable voyage")

    await ctx.send(embed=embed)