const $ = window.$;
const ul = $('UL#list_movies');

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: (data) => {
    data.results.forEach((el) => {
      const li = $('<li>').text(el.title);
      ul.append(li);
    });
  },
  error: (xhr, status, error) => {
    console.error(error);
  }
});
