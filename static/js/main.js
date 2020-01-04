Array.from(document.querySelectorAll('.mail button'), function (e) {
  e.addEventListener('click', function () {
    const s = 'MBIS;eCMBCG;LOwAG;CFe=IG'
    var r = ''
    for (i = 0; i < s.length; i++) {
      r += String.fromCharCode((s.charCodeAt(i) + 5) % 93 + 33)
    }
    document.querySelector('.mail').innerHTML = r
  })
})

Array.from(document.querySelectorAll('#more'), function (e) {
  e.addEventListener('click', function () {
    Array.from(document.querySelectorAll('.invisible'), function (e) {
      e.classList.remove('invisible')
    })
    e.classList.add('invisible')
  })
})

const query = 'a[href^="http"]:not([href*="' + location.hostname + '"])'
Array.from(document.querySelectorAll(query), function(e) {
  e.setAttribute('target', '_blank')
})