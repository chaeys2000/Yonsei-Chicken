document.addEventListener('DOMContentLoaded', function() {
    // 변수 초기화
    var imageCount = 0;
    var maxClicks = 9;
    var furImage = document.getElementById('fur-image');
    var progressBar = document.getElementById('progress-bar');
    
    // 이미지 클릭 이벤트 처리
    furImage.addEventListener('click', clickHandler);
    
    function clickHandler() {
      imageCount++;
      
      if (imageCount % 3 === 0 && imageCount <= maxClicks) {
        if (imageCount === maxClicks) {
          furImage.removeEventListener('click', clickHandler);
          furImage.src = '/static/no_fur_image.jpg';
          createArrowButton();
        }
        else {
            furImage.src = `/static/${imageCount / 3}_3_fur_image.jpg`;
            updateProgressBar();
        }
        
      }
    }
    
    // 게이지 업데이트 함수
    function updateProgressBar() {
      var progressWidth = (imageCount / maxClicks) * 100;
      progressBar.style.width = progressWidth + '%';
    }
    
    // 화살표 버튼 생성 함수
    function createArrowButton() {
        const buttonTest = document.querySelector('.test');
      var arrowButton = document.createElement('button');
      arrowButton.innerHTML = '&#8594;'; // 오른쪽 화살표 아이콘
      arrowButton.addEventListener('click', function() {
        window.location.href = "{% url 'mix' %}";
      });
      buttonTest.appendChild(arrowButton);
    }
  });
  
  