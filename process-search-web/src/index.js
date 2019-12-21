import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';
import Admin from './App';
import './index.css';
import ProcessSearch from './process-search/ProcessSearch';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
    (<BrowserRouter>
        <Switch>
            <Route path="">
                <Admin>
                    <Route path="/process" component={ProcessSearch}/>
                </Admin>
            </Route>
        </Switch>
    </BrowserRouter>)
, document.getElementById('root'));

serviceWorker.unregister();
