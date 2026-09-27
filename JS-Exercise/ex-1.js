const loginBtn = document.querySelector('.login-btn');
function changeLoginBtn(){
    if (loginBtn.innerHTML.trim() === 'Login' ){
        loginBtn.innerHTML = 'Logout';
    }
    else{
        loginBtn.innerHTML = 'Login';
    }
}

const like13btn = document.querySelector('.likes-13-btn');
function cliked13Btn(){
    like13btn.style.padding = '20px';
    alert('You cliked on 13 likes button');

}

const like37btn = document.querySelector('.likes-37-btn');
function cliked37Btn(){
    like37btn.style.border = '5px solid pink';
    alert('You cliked on 37 likes button');
}

const addDifinitionBtn = document.querySelector('.add-definition-btn');
function removeBtn(){
    addDifinitionBtn.remove();
}

const numOfLikes = document.querySelector('.num-of-likes');
const like = document.querySelector('.like-btn');
function addLike(){
    let currentNum = parseInt(numOfLikes.innerHTML);
    currentNum = currentNum + 1;
    numOfLikes.innerHTML = currentNum;
    like.style.color = "red";
    like.style.backgroundColor = "blue";
}
