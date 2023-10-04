const $ = window.$;
const header = $('header');
const div = $('#red_header');

div.on('click', () => {
  header.addClass('red');
});
