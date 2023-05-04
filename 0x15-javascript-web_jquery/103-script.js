$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const langCode = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/', { lang: langCode }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keypress((event) => {
    if (event.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
