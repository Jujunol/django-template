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
                <div className="card-panel">
                    <h1>Django App Template</h1>

                    <h5>Installed Pip Packages</h5>
                    <ul className="collection">
                        <li className="collection-item">Django - Backend Framework</li>
                        <li className="collection-item">Jinja2 - Templating Engine (better than Django's)</li>
                        <li className="collection-item">Python-Decouple - .env var handler for Django</li>
                    </ul>

                    <h5>Installed Node Packages</h5>
                    <ul className="collection">
                        <li className="collection-item">Babel - There's a few of these to write nice clean code in Javascript</li>
                        <li className="collection-item">React - For react apps</li>
                        <li className="collection-item">Css-loader - interprets @import and url() like import/require() and will resolve them</li>
                        <li className="collection-item">Sass-loader - converts sass and scss into plain css</li>
                        <li className="collection-item">Node-sass - Also transpilation of scss and css to transpile faster</li>
                        <li className="collection-item">Webpack - A build system used to build our assets</li>
                    </ul>
                </div>
            </div>
        );
    }
}

ReactDom.render(
    <App />,
    document.getElementById('app')
);

material.AutoInit();