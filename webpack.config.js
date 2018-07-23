const devMode = process.env.NODE_ENV !== "production";
const path = require('path');

const LiveReloadPlugin = require('webpack-livereload-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: "./app/js/app.jsx",
    output: {
        path: path.resolve(__dirname, "static"),
        filename: "app.js"
    },
    module: {
        rules: [
            {
                test: /\.js.?$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: {
                    presets: ['react', 'env'],
                    plugins: ['transform-class-properties'],
                },
            },
            {
                test: /\.scss$/,
                exclude: /node_modules/,
                use: [
                    {loader: MiniCssExtractPlugin.loader},
                    {loader: "css-loader"},
                    {loader: "sass-loader"},
                ]
            },
        ],
    },
    optimization: {
        splitChunks: {
            cacheGroups: {
                styles: {
                    name: 'styles',
                    test: /\.css$/,
                    chunks: "all",
                    enforce: true,
                }
            }
        }
    },
    plugins: [
        new LiveReloadPlugin(),
        new MiniCssExtractPlugin({
            filename: "app.css",
        }),
    ],
};