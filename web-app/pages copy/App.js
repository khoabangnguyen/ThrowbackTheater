import React, { Component, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { useRouter } from 'next/router'


const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },

  link: {
    color: 'white'
  }
}));

function App() {
    const classes = useStyles();
    const router = useRouter();

    useEffect(() => {    
        // Update the document title using the browser API    
        router.push("/signin")  
    }, []);

    return (
        <div>
            {/* <Container maxWidth="xs">
            <div className={classes.paper}>
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                >
                <Link className={classes.link} href="/signin"> SIGN IN</Link>
                </Button>
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                >
                    <Link className={classes.link} href="/signup"> SIGN UP</Link>
                </Button>
                <Button onClick={() => {router.push("/signup")}}>
                    CLICK
                </Button>
                </div>
            </Container> */}
        </div>
    );
}

export default App;