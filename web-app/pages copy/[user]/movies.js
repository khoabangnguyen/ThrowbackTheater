import React, { useState, useEffect } from 'react';
import MediaCard from "../../components/movie";
import { useRouter } from 'next/router'

function View({ moviesList }) {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(true);
    const [movies, setMovies] = useState(moviesList)
  
    const router = useRouter();
    const { user } = router.query

    const fetchMovies = async () => {
      const res = await fetch("http://127.0.0.1:5000/classicsTest")
      const items = await res.json()
      const moviesList = items.movies

      setMovies(moviesList)
      setIsLoaded(true)
    }

    const nextMovie = () => {
      let newMovies = movies
      newMovies.shift()
      if (newMovies.length === 0) {
        setIsLoaded(false)
        fetchMovies()
      } else {
        setMovies([...newMovies])
      }
    }

    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <MediaCard movie={movies[0]} next={nextMovie}></MediaCard>
          Movies left in queue: {movies.length}
          {user}
        </div>
      );
    }
}


export async function getStaticProps({ params }) {
  const res = await fetch(`http://127.0.0.1:5000/getMovies?username=${params.user}`)
  const items = await res.json()
  const moviesList = items.movies

  return {props: {moviesList}}
}

export async function getStaticPaths() {
    const res = await fetch("http://127.0.0.1:5000/usernames")
    const items = await res.json()
    const usernames = items.usernames

    return {
        paths: Object.values(usernames).map(x => {return {params: { user: x}}}),
        // paths: usernames.map(x => {params: { user: x}}),
        fallback: false
      }   
}

export default View