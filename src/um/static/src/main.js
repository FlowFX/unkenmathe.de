// initialize markdown-it and katex
let md = require('markdown-it')('commonmark');
let mk = require('markdown-it-katex');

md.use(mk);

let app = new Vue({
  el: '#app',
  delimiters: ['[', ']'],
  data: {
    input: exercise_text,
  },
  computed: {
    compiledMarkdown: function () {
      return md.render(this.input);
    }
  },
});
