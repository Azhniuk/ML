function setMatrix() {
    document.querySelector("#heading").innerHTML = "Set matrix"
  }


document.querySelector("#heading").innerHTML = "Set dimension"


const changeSelected = (e) => {
    const $select = document.querySelector('#dimension');
    $select.value = '2'
  };


  
  
let setDetHTML = `<div class = "row">`;

{
    weekHTML = weekHTML + `
    <div class = "col-2">
      <div class = "week-date">
          ${formatDay(forecastDay.dt)}
      </div>
        
        <image 
                  src = "http://openweathermap.org/img/wn/${forecastDay.weather[0].icon}@2x.png"
                  id =""
                  alt = ""
                  
                  class = ""
                  width = "42"
                  />
        <div class = "week-temp">
          <span class = "week-temp-min">${Math.round(forecastDay.temp.min)}° </span>
          <span class = "week-temp-max">${Math.round(forecastDay.temp.max)}°</span>
        </div>
      </div>`
    }});


    weekHTML = weekHTML +`</div>`;
    weekElement.innerHTML = weekHTML;
  
