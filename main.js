/*=============== HOME SWIPER ===============*/
window.onload= () =>{
  let homeSwiper = new Swiper(".home-swiper", {
      spaceBetween: 30,
      loop: 'true',
      
      pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
  })
  const textarea = document.querySelector("textarea")
  const button = document.querySelector("button")
  button.addEventListener("click", (e) => {
      e.preventDefault()
      fetch("http://127.0.0.1:5000", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          mode: "no-cors",
          body: JSON.stringify({ data: textarea.value }),
      }).then((res) => {
          console.log(res)
      })
  })
  }
  
  