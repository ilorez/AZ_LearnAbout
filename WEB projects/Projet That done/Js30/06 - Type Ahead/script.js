const endpoint =
  "https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json";
let cities = new Array();
  const response = fetch(endpoint)
    .then((infos) => infos.json())
    .then(data => cities.push(...data))
;
// console.log(cities)
// find matches
function findMatches(targetWord,array){
    return array.filter(place =>{
        const regex = new RegExp(targetWord,'gi');
        return place.city.match(regex) || place.state.match(regex);
    });
}
// # format numbers
function numberWithCommas(x){
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g,',');
}

const search = document.querySelector(".search");
const ul = document.querySelector(".suggestions");

function displaySearch(){
    const matchCities = findMatches(this.value,cities)
    const html = matchCities.map(citie=>{
        const regex = new RegExp(this.value,"gi");
        const cetName = citie.city.replace(regex, `<span class="hl">${this.value}</span>`) 
        const stateName = citie.state.replace(regex, `<span class="hl">${this.value}</span>`) 
        const popul = numberWithCommas(citie.population);
        return `
        <li>
            <span class="name">${cetName}, ${stateName}</span> 
            <span class="population">${popul}</span>
        </li>
    `}).join("");
    ul.innerHTML = html
}

search.addEventListener("change",displaySearch);
search.addEventListener("keyup",displaySearch);
