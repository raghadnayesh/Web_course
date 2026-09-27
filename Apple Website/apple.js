const allMenus = document.querySelectorAll('[class$="-menu"]');
const allContainers = document.querySelectorAll('nav > div');

let timer;

function hideAllMenus() {
  clearTimeout(timer);
  allMenus.forEach(menu => {
    menu.style.display = 'none';
  });
}

allContainers.forEach(container => {
  const menu = container.querySelector('[class$="-menu"]');
  if (!menu) return;

  container.addEventListener('mouseenter', () => {
    hideAllMenus();
    menu.style.display = 'flex';
  });

  container.addEventListener('mouseleave', () => {
    timer = setTimeout(() => {
      menu.style.display = 'none';
    }, 150);
  });
});

const shopIphone = document.querySelector('#btn-shop-iphone');
if (shopIphone) {
  shopIphone.addEventListener('mouseenter', () => {
    shopIphone.style.backgroundColor = 'rgb(37, 84, 241)';
    shopIphone.style.color = 'white';
  });
  shopIphone.addEventListener('mouseleave', () => {
    shopIphone.style.backgroundColor = 'white';
    shopIphone.style.color = 'rgb(37, 84, 241)';
  });
}

const addToCalender = document.querySelector('.add-to-calender-btn')
addToCalender.addEventListener('mouseenter', () => {
  addToCalender.style.backgroundColor = 'rgb(37, 84, 241)';
  addToCalender.style.color = 'white';
});
addToCalender.addEventListener('mouseleave', () => {
  addToCalender.style.backgroundColor = 'white';
  addToCalender.style.color = 'rgb(37, 84, 241)';
})