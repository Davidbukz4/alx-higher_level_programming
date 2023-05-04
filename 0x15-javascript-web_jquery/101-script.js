$(document).ready(() => {
  // adds item
  $('DIV#add_item').on('click', () => {
    $('<li>').text('Item').appendTo('UL.my_list');
  });
  // removes item
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li:last-child').remove();
  });
  // clears list
  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
