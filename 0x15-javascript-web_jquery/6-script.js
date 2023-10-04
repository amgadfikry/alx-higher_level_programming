const $ = window.$;
const header = $('header');
const div = $('#update_header');

div.on('click', () => {
  header.text('New Header!!!');
});
