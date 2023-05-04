$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json'
}).done((data) => {
  const resp = data.results;
  let i;
  for (i = 0; i < resp.length; i++) {
    $('<li>').text(resp[i].title).appendTo('UL#list_movies');
  }
});
