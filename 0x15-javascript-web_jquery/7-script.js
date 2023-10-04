const $ = window.$;
const div = $('#character');

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: (data) => {
    div.text(data.name);
  },
  error: (xhr, status, error) => {
    console.error(error);
  }
});
