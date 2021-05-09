import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import SignIn from './signin'
import SignUp from './signup'
import View from './classics'
import Home from './index'

export default function allRoutes() {
    return (
        <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/signin" component={SignIn} />
            <Route exact path="/signup" component={SignUp} />
            <Route exact path="/welcome" component={View} />
        </Switch> 
    );
}

