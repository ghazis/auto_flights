const path = require('path');
const wm = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = wm.merge(common, {
   mode: 'production'
});