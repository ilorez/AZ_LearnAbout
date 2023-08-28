// Select Elements
const player = document.querySelector('.player');
const video = player.querySelector('video');
const playerControls = player.querySelector('.player__controls');
const progress = playerControls.querySelector('.progress');
const progressFilled = playerControls.querySelector('.progress__filled');
const playBtn = playerControls.querySelector('.toggle');
const skipBtns = [...playerControls.querySelectorAll('[data-skip]')];
const volumeRange = playerControls.querySelector('[name="volume"]');
const speedRange = playerControls.querySelector('[name="playbackRate"]');

console.dir(video)
// console.dir(video.currentTime)
// console.dir(video.duration)
// console.dir(video.volume)

// functions


function editProgBar(){
    // if(video.paused) return;
    let currentTime = video.currentTime;
    let duration = video.duration;
    let proPerCent = (100*parseFloat(currentTime))/parseFloat(duration);
    progressFilled.style.flexBasis = `${proPerCent}%`;
}
function updateButton(){
    playBtn.textContent = this.paused ? '►': 'II';
}
function video_play(){

    video.paused ? video.play() : video.pause();
}
function skipTime(){
    skip = parseInt(this.getAttribute('data-skip'));
    video.currentTime += skip;
}
function volumeChange(){
    video.volume = parseFloat(volumeRange.value);
}
function speedChange(){
    video.playbackRate = parseFloat(speedRange.value);
}
function scrub(e){
    scrubTime = (e.offsetX / progress.offsetWidth) * video.duration;
    video.currentTime = scrubTime;
}
// Event
video.addEventListener('click',video_play)
video.addEventListener('timeupdate',editProgBar)
video.addEventListener('pause',updateButton)
video.addEventListener('play',updateButton)

playBtn.addEventListener('click',video_play)
skipBtns.forEach(btn => {
    btn.addEventListener('click',skipTime)
})
volumeRange.addEventListener('change',volumeChange)
speedRange.addEventListener('change',speedChange)

let mouseDown = false;
progress.addEventListener('click',scrub);
progress.addEventListener('mousemove',()=> mouseDown && scrub(e));
progress.addEventListener('mousedown',() => mouseDown = true);
progress.addEventListener('mouseup',() => mouseDown = false);


