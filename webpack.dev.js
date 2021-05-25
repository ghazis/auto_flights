const path = require('path');
const wm = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = wm.merge(common, {
   mode: 'development',
   devServer: {
      hot: true,
      historyApiFallback: true,
      contentBase: path.join(__dirname, 'dist'),
      host:'0.0.0.0',
      port:8080
   }
});