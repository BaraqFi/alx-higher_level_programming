$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, textstatus) => {
    $('DIV#character').text(data.name);
});
