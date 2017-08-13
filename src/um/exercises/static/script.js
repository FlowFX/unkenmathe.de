let md = require('markdown-it')('commonmark');
let mk = require('markdown-it-katex');

md.use(mk);

let input = process.argv[2];

console.log(md.render(input));
