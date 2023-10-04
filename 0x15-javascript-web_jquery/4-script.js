const $ = window.$;
const header = $('header');
const div = $('#toggle_header');

div.on('click', () => {
  header.toggleClass('green red');
});
