const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
   entry: './src/index.js',
   output: {
      filename: 'app.js',
      publicPath: '/',
      path: path.resolve(__dirname, 'dist')
   },
   plugins: [
     new HtmlWebpackPlugin({
       title: "Auto Flights",
       filename: 'index.html',
       template: 'src/index.template.html',
       chunksSortMode: 'none'
     }),
   ],
   module: {
      rules: [
         {
            test: /\.jsx?$/,
            loader: 'babel-loader',
            exclude: /node_modules/,
            query: {
               presets: ["es2015", "react"],
               plugins: ["transform-es2015-destructuring", "transform-object-rest-spread"]
            }
         },
         {
           test: /\.(s*)css$/,
           use: ['style-loader', 'css-loader', 'sass-loader']
         },
        {
          test: /\.(png|jpg|gif)$/,
          use: [
            {
              loader: 'url-loader',
              options: {
                name: '[name].[ext]',
                esModule: false
              }
            }
          ]
        }
      ]
   }
};