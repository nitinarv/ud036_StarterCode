import media
import fresh_tomatoes

# instance of Movie that contains all details of the toystory movie
toy_story = media.Movie(
    "Toy Story",
    "This is a movie about toys coming to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
first_blood = media.Movie(
    "First Blood",
    "A vietnam war veteran returns home to his small town." +
    "Suffering from PTSD and irked by the local police force's prejudice" +
    "and insensitivities sets on a war path with them.",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/First_blood_poster.jpg",
    "https://www.youtube.com/watch?v=rjptQSfuTy8")
fight_club = media.Movie(
    "Fight Club",
    "A regular salaried man suffering from multiple personality disorder" +
    " is put on a path of self discovery and " +
    "rediscovers himself and finds love.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")
bourne_identity = media.Movie(
    "Bourne Identity",
    "Jason bourne is a spy who has lost is memory and the" +
    " story is about him finding back about who he really is.",
    "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
    "https://www.youtube.com/watch?v=cD-uQreIwEk")
avatar = media.Movie(
    "Avatar",
    "A handicapped marine deployed on an alien planet to fight" +
    " for the humans but then later turns into a messaiah and " +
    "savior of the Natives",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie(
    "School of rock",
    "A jobless rockband member desperate for work becomes " +
    "a school teacher and then makes a school rock band.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=LqEszt5wG9I")
batman_rises = media.Movie(
    "Batman Rises",
    "The story of the masked vigilante of Gotham city " +
    "coming out of retirement to save the city " +
    "once again for the last time.",
    "https://upload.wikimedia.org/wikipedia" +
    "/en/8/83/Dark_knight_rises_poster.jpg",
    "https://www.youtube.com/watch?v=g8evyE9TuYk")
skyfall = media.Movie(
    "Skyfall",
    "James Bond has to revisit his past " +
    "and history to save the life of 'M' as " +
    "the deamons of her past return to haunt her",
    "https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
    "https://www.youtube.com/watch?v=6kw1UVovByw")
lock_stock_and_two_smoking_barrels = media.Movie(
    "Lock Stock And Two Smoking Barrels",
    "A comedy of two child hood friends who are crooks " +
    "and get caught up in a card game raket and now has " +
    "to payback to the honchos.",
    "https://upload.wikimedia.org/wikipedia/en/e/e9/Lock" +
    "%2C_Stock_and_Two_Smoking_Barrels_2.jpg",
    "https://www.youtube.com/watch?v=KZh33gGK3Y8")

movies = [
    first_blood,
    bourne_identity,
    fight_club,
    batman_rises,
    skyfall,
    lock_stock_and_two_smoking_barrels]

fresh_tomatoes.open_movies_page(movies)
