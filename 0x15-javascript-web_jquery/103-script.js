const $ = window.$;
$(document).ready(() => {
  const fetchData = () => {
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
  };
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.keyCode === 13) {
      fetchData();
    }
  });
  $('INPUT#btn_translate').on('click', () => {
    fetchData();
  });
});
