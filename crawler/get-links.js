const axios = require('axios')
const Url = require('url')

module.exports = url => {
  const { host } = Url.parse(url)
  const extractor = require(`./sites/${host}.js`)
  extractor.getLinks(url)
}
  