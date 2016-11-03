import media
import fresh_tomatoes

aliens = media.Movie('Aliens', 'The face suckers return',
                     'https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg',
                     'https://www.youtube.com/watch?v=AW-7_HE98PY'
                     )

conan_the_barbarian = media.Movie('Conan', 'Conan Slays.',
                                  'https://upload.wikimedia.org/wikipedia/en/c/cd/Conan_the_'
                                  'Barbarian_1982_film_poster.jpg',
                                  'https://www.youtube.com/watch?v=xwdYd_RdLCQ'
                                  )

man_from_earth = media.Movie('The Man From Earth', 'Cave man Professor lays down knowledge',
                             'https://upload.wikimedia.org/wikipedia/en/3/3b/The_Man_from_Earth.png',
                             'https://www.youtube.com/watch?v=lVMhEAI3pvg'
                             )

interview_with_a_vampire = media.Movie('Interview With The Vampire', 'The Vampire Tells All',
                            'https://upload.wikimedia.org/wikipedia/en/f/fe/InterviewwithaVampireMoviePoste.JPG',
                            'https://www.youtube.com/watch?v=bDH7P0qvSMU'
                            )

commando = media.Movie('Commando', 'Arnold plays arnold.',
            'https://upload.wikimedia.org/wikipedia/en/d/d9/Commandoposter.jpg',
            'https://www.youtube.com/watch?v=mh-QUh69MCg'
            )

army_of_darkness = media.Movie('Army of Darkness', 'Ash saves, then dooms, then saves the primitive screw heads.',
                    'https://upload.wikimedia.org/wikipedia/en/4/46/Army_of_Darkness_poster.jpg',
                    'https://www.youtube.com/watch?v=CZ-wU5RXw2o'
                    )

movies = [aliens, conan_the_barbarian, man_from_earth, interview_with_a_vampire, commando, army_of_darkness]


fresh_tomatoes.open_movies_page(movies)

