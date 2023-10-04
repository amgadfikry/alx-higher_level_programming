const $ = window.$;
const ul = $('UL.my_list');
const div = $('#add_item');

div.on('click', () => {
  ul.append('<li>Item</li>');
});
