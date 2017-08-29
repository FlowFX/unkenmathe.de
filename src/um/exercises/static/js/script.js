let md = require('markdown-it')({
  html: true,           // Enable HTML tags in source
  typographer:  true,   // Enable German quotes
  quotes: '„“‚‘'
});
let mk = require('markdown-it-katex');


md.use(mk);

let input = process.argv[2];

console.log(md.render(input));
