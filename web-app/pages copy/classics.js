import React, { useState, useEffect } from 'react';
import MediaCard from "../components/movie"

function View({ moviesList }) {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(true);
    const [movies, setMovies] = useState(moviesList)
    // const [count, setCount] = useState(moviesList.length)
  
    const fetchMovies = async () => {
      const res = await fetch("http://127.0.0.1:5000/classicsTest")
      const items = await res.json()
      const moviesList = items.movies

      setMovies(moviesList)
      // setCount(moviesList.length)
      setIsLoaded(true)
    }

    const nextMovie = () => {
      let newMovies = movies
      newMovies.shift()
      // setCount(count-1)
      if (newMovies.length === 0) {
        setIsLoaded(false)
        fetchMovies()
      } else {
        setMovies([...newMovies])
      }
    }

    // Note: the empty deps array [] means
    // this useEffect will run once
    // similar to componentDidMount()
    // useEffect(() => {
    //   fetchMovies()
    // }, [isLoaded])

    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <MediaCard movie={movies[0]} next={nextMovie}></MediaCard>
          Movies left in queue: {movies.length}
        </div>
      );
    }
}


// function View({ moviesList }) {
//   const [movies, setMovies] = useState(moviesList)

//   return (
//     <div>
//       <MediaCard props={movies[0]}></MediaCard>
//     </div>

//   )
// }

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:5000/classics")
  const items = await res.json()
  const moviesList = items.movies

  return {props: {moviesList}}
}

export default View