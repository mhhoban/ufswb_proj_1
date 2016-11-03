import media
import fresh_tomatoes

aliens = media.Movie('Aliens', 'The face suckers return',
                     'https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg',
                     'https://www.youtube.com/watch?v=AW-7_HE98PY'
                     )

conan_the_barbarian = media.Movie('Conan', 'Conan Slays.',
                                  'https://upload.wikimedia.org/wikipedia/en/c/cd/Conan_the_Barbarian_1982_film_poster.jpg',
                                  'https://www.youtube.com/watch?v=xwdYd_RdLCQ'
                                  )

man_from_earth = media.Movie('The Man From Earth', 'Cave man Professor lays down knowledge',
                             'https://upload.wikimedia.org/wikipedia/en/3/3b/The_Man_from_Earth.png',
                             'https://www.youtube.com/watch?v=lVMhEAI3pvg'
                             )

movies = [aliens, conan_the_barbarian, man_from_earth]

fresh_tomatoes.open_movies_page(movies)

