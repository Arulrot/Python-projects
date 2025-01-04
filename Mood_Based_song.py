def mood_music_recommender():
    # Predefined playlists for different moods
    playlist = {
        "happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Uptown Funk - Bruno Mars"],
        "sad": ["Someone Like You - Adele", "Let Her Go - Passenger", "Fix You - Coldplay"],
        "energetic": ["Eye of the Tiger - Survivor", "Lose Yourself - Eminem", "Stronger - Kanye West"],
        "relaxed": ["Weightless - Marconi Union", "Sunset Lover - Petit Biscuit", "Perfect - Ed Sheeran"]
    }

    # Ask the user about their mood
    print("Welcome to the Mood-Based Music Recommender!")
    print("Available moods: happy, sad, energetic, relaxed")
    mood = input("How are you feeling today? ").lower()

    # Recommend songs based on mood
    if mood in playlist:
        print(f"\nHere are some {mood} songs for you:")
        for song in playlist[mood]:
            print(f"- {song}")
    else:
        print("\nSorry, I don't recognize that mood. Try one of these: happy, sad, energetic, relaxed.")

# Run the program
mood_music_recommender()
