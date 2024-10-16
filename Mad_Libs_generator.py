def mad_libs():
    story="In a {adjective} land, there was a {noun} that loved to {verb}. One day, it found a magical {noun1} that granted wishes. Excited, it wished for a {adjective2} friend to join in its adventures. Together, they would {verb2} and explore the wonders of the world."
    print("Welcome to Simple Mad libs generator\n")
    adjective=input("Enter an adjective:")
    noun=input("Enter an noun:")
    verb=input("Enter a verb:")
    noun1=input("Enter a noun:")
    adjective2=input("Enter a adjective:")
    verb2=input("Enter a verb:")
    story=story.format(adjective=adjective,noun=noun,verb=verb,noun1=noun1,adjective2=adjective2,verb2=verb2)
    print("\n",story)

mad_libs()