const axios = require('axios')
const cheerio = require('cheerio')

module.exports = {
  getLinks: async url => {
    const response = await axios.get(url)
    const $ = cheerio.load(response.data)

    $('.resultado').each(function (i, el) {
      console.log(i, $(this).text());
      
      //console.log(el.html());
    })
  }
}