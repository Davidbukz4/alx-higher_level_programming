$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json'
}).done((data) => {
  $('DIV#character').text(data.name);
});
