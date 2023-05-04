$(document).ready(() => {
  $(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
      const langCode = $('INPUT#language_code').val();
      $.getJSON(
        `https://fourtonfish.com/hellosalut/hello/?lang=${langCode}`,
        function (data) {
          $('#hello').text(data.hello);
        }
      );
    });
  });
});
