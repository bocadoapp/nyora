const Queue = require('bull')
const getLinks = require('./get-links')

const urls = [
  'https://www.recetasgratis.net/recetas-japonesas'
]
const queue = new Queue('crawler')
const crawl = (job, cb) => {
  console.log(job.data);
  return cb(null, 'haha')
  // return Promise.resolve('oeoeoe')
}

queue.process('crawl', 1, crawl)
queue.on('completed', (job, result) => {
  console.log('done', job.data, result);
})
// queue.add('crawl', urls[0], {})

getLinks(urls[0])
