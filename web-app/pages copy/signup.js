import { React, useState } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:5000/usernames")
  const items = await res.json()
  const usernames = items.usernames

  return {props: {usernames}}
}

export default function SignUp({ usernames }) {
  const classes = useStyles();

  const [userId, setId] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("")
  const [registered, setRegistered] = useState(false)

  const handleChange = (event) => {
    let id = event.target.id;
    if (id === "username") {
      setId(event.target.value)
    } else if (id === "password") {
      setPassword(event.target.value)
    } else {
      setConfirm(event.target.value)
    }
  }

  const validUsername = () => {
    return (!usernames.includes(userId))
  }

  const validPassword = () => {
    return true
  }

  const validConfirmPw = () => {
    return (confirm === password)
  }


  const noEmptyFields = () => {
    return (userId.length && password.length && confirm.length)
  }


  const validForm = () => {
    return (validUsername() && validPassword() && validConfirmPw())
  }


  const handleSubmit = async () => {
    event.preventDefault();
    const res = await fetch(`http://127.0.0.1:5000/createuser`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({username: userId, password: password})
          })
    const response = await res.json()
    const info = response.info
    if (info === "SUCCESS") {
      setRegistered(true)
    }
  }

  if (registered) {
    return (
    <Container component="main" maxWidth="sm">
      <div className={classes.paper}>
        <Typography component="h1" variant="h2">
            Registration success!
        </Typography>
        <Typography  variant="subtitle1">
            Welcome to Throwback Theater
        </Typography>
        <Link href="/signin" variant="body2">
              {"Sign in to start viewing your recommendations"}
        </Link>
      </div>
    </Container>
    )
  }
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <form className={classes.form} noValidate onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            // autoComplete="username"
            autoFocus
            onChange={handleChange}
            error = {!validUsername()}
            helperText = {validUsername() ? "" : "Username is empty / already taken"}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            // autoComplete="current-password"
            onChange={handleChange}
            error = {!validPassword()}
            helperText = {validPassword() ? "" : "Password can't be empty"}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="confirm_password"
            label="Confirm Password"
            type="password"
            id="confirm_password"
            // autoComplete="current-password"
            onChange={handleChange}
            error={!validConfirmPw()}
            helperText={validConfirmPw() ? "" : "Password doesn't match"}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            disabled={ !(validForm() && noEmptyFields()) }
          >
            Sign Up
          </Button>
          <Link href="/signin" variant="body2">
                {"Already have an account? Sign In"}
          </Link>
        </form>
      </div>
    </Container>
  );
}