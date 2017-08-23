// load custom CSS
import './style.css';

// initialize markdown-it and katex
let md = require('markdown-it')({
  html: true,           // Enable HTML tags in source
  typographer:  true,   // Enable German quotes
  quotes: '„“‚‘'
});
let mk = require('markdown-it-katex');

md.use(mk);

let app = new Vue({
  el: '#app',
  data: {
    input: exercise_text,
  },
  computed: {
    compiledMarkdown: function () {
      return md.render(this.input);
    }
  },
});
