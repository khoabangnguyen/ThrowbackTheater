import { useRouter } from 'next/router'
import Link from '@material-ui/core/Link';

const Home = () => {
  const router = useRouter()
  const { user } = router.query

  return (
    <div>
      <p>User: {user}</p>
      <Link href="movies">Go to movies</Link>
    </div>
  ) 
}

export default Home