import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  root: {
    maxWidth: 800
  },

  media: {
    width: 345,
    display: 'flex'
  },

  contentContainer: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: "flex-start"
  }, 

  content: {
  }
    
});

export default function MediaCard({ movie, next}) {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardActionArea className={classes.contentContainer}>
        <CardMedia className={classes.media} title={movie.title}>
            <img className={classes.media} src={"https://image.tmdb.org/t/p/original/"+movie.poster_path}></img>
        </CardMedia>
        <CardContent className={classes.content}>
          <Typography gutterBottom variant="h5" component="h2">
            {movie.title}
          </Typography>
          <Typography gutterBottom variant="body1" component="h2">
            "{movie.tagline}"
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Release Date: {movie.release_date}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Genres: {movie.genres.map(genre => genre.name).toString()}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Rating: {movie.vote_average}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Duration: {movie.runtime}m
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Synopsis:
            <br/>
            {movie.overview}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary" onClick={next}>
          Next
        </Button>
        <Button size="small" color="primary">
          Learn More
        </Button>
      </CardActions>
    </Card>
  );
}