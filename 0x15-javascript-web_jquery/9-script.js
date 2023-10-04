const $ = window.$;
$(document).ready(() => {
  const div = $('DIV#hello');

  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: (data) => {
      div.text(data.hello);
    },
    error: (xhr, status, error) => {
      console.error(error);
    }
  });
});
