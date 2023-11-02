/*fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays 
the value of hello from that fetch in the HTML tag DIV#hello8*/
window.onload = function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
};
