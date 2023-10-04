const $ = window.$;
$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const val = $('INPUT#language_code').val();
    const urlV = `https://hellosalut.stefanbohacek.dev/?lang=${val}`;
    $.ajax({
      url: urlV,
      type: 'GET',
      dataType: 'json',
      success: (data) => {
        $('DIV#hello').text(data.hello);
      },
      error: (xhr, status, error) => {
        console.error(error);
      }
    });
  });
});
