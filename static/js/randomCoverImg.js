var totalCount = 4;

function randomCover() {
  var num = Math.ceil(Math.random()*totalCount);
  document.body.background = 'static/img/' + 'coverimg_' + num + '.jpg';
  document.body.background.style = 'background-image; background: none repeat scroll';
}
