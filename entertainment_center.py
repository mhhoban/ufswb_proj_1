import media
import fresh_tomatoes

# instantiate Movie object for "Aliens"
aliens = media.Movie('Aliens',
                     'The face suckers return',
                     'https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_'
                     'poster.jpg',
                     'https://www.youtube.com/watch?v=AW-7_HE98PY'
                     )

# instantiate Movie object for "Conan The Barbarian"
conan_the_barbarian = media.Movie('Conan',
                                  'Conan Slays.',
                                  'https://upload.wikimedia.org/wikipedia/en/'
                                  'c/cd/Conan_the_Barbarian_1982_film_poster'
                                  '.jpg',
                                  'https://www.youtube.com/watch?v=xwdYd_RdLCQ'
                                  )

# instantiate Movie object for "The Man From Earth"
man_from_earth = media.Movie('The Man From Earth',
                             'Cave man Professor lays'
                             'down knowledge',
                             'https://upload.wikimedia.org/wikipedia/en/3/3b/'
                             'The_Man_from_Earth.png',
                             'https://www.youtube.com/watch?v=lVMhEAI3pvg'
                             )

# instantiate Movie object for "Interview With The Vampire"
interview_with_a_vampire = media.Movie('Interview With The Vampire',
                                       'The Vampire Tells All',
                                       'https://upload.wikimedia.org/wikipedia'
                                       '/en/f/fe/InterviewwithaVampireMoviePos'
                                       'te.JPG',
                                       'https://www.youtube.com/watch?v=bDH7P'
                                       '0qvSMU'
                                       )

# instantiate Movie object for "Commando"
commando = media.Movie('Commando',
                       'Arnold plays Arnold.',
                       'https://upload.wikimedia.org/wikipedia/en/d/d9/Command'
                       'oposter.jpg',
                       'https://www.youtube.com/watch?v=mh-QUh69MCg'
                       )

# instantiate Movie object for "Army of Darkness"
army_of_darkness = media.Movie('Army of Darkness',
                               'Ash saves, then dooms, then saves the primitiv'
                               'e screw heads.',
                               'https://upload.wikimedia.org/wikipedia/en/4/46'
                               '/Army_of_Darkness_poster.jpg',
                               'https://www.youtube.com/watch?v=CZ-wU5RXw2o'
                               )

# create list of the movie objects created above
movies = [aliens, conan_the_barbarian, man_from_earth,
          interview_with_a_vampire, commando, army_of_darkness]

# pass the list of movie object into Fresh_Tomatoes and generate the website
# using the movie objects created above.
fresh_tomatoes.open_movies_page(movies)

