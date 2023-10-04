const $ = window.$;
$(document).ready(() => {
  const ul = $('UL.my_list');
  const add = $('DIV#add_item');
  const remove = $('DIV#remove_item');
  const clear = $('DIV#clear_list');
  const li = '<li>Item</li>';

  add.on('click', () => {
    ul.append(li);
  });
  remove.on('click', () => {
    $('ul li').last().remove();
  });
  clear.on('click', () => {
    ul.empty();
  });
});
