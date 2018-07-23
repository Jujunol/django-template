// don't let your IDE fool you, these imports are IMPORTANT
import $ from 'jquery';
import material from 'materialize-css';
import * as scss from '../scss/app.scss';

import React, {Component} from 'react';
import ReactDom from 'react-dom';

class App extends Component {
    render() {
        return (
            <div className="container">
                <h1>Content goes here</h1>
            </div>
        );
    }
}

ReactDom.render(
    <App />,
    document.getElementById('app')
);

material.AutoInit();