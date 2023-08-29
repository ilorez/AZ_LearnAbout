'use client';
import Image from 'next/image'
import styles from './page.module.css'
import { useEffect, useRef, useState } from 'react';
// type btnProp={
//   value : string
// }
let isOTurn = false;
let isLastTurnWasO = false; 
let isOver = false;
function GameSection(){
  // const selfRef = useRef<Array<HTMLButtonElement | null>>([])
  const [btnsValue,setBtnsValue] = useState<Array<Array<string|number>>>([["","",""],["","",""],["","",""]]);
  
  
  const clickedOn = (index:Array<number>) =>{

    if (btnsValue[index[0]][index[1]] != "" || isOver) return 
    let btnsCopy = [...btnsValue]
    isOTurn ? btnsCopy[index[0]][index[1]]="O":btnsCopy[index[0]][index[1]]="X"
    setBtnsValue(btnsCopy)
    isOTurn = !isOTurn
    console.log(isOTurn)
  }
    const possibleWins = [
      [[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,2],[1,1],[2,0]],[[0,0],[1,1],[2,2]]
    ]
    const possibleWinsIds = [
      [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]

    ]
  const checkWin = () =>{
    console.log('checking win...')
    possibleWins.forEach((win,index)=>{
      if(btnsValue[win[0][0]][win[0][1]] && btnsValue[win[0][0]][win[0][1]]===btnsValue[win[1][0]][win[1][1]] && btnsValue[win[1][0]][win[1][1]]===btnsValue[win[2][0]][win[2][1]]){
        console.log(`${btnsValue[win[1][0]][win[1][1]]} wins`);
        isOver = true;
        possibleWinsIds[index].forEach(id=>{
          let btn = document.querySelector(`#btn${id}`);
          if (btn){
            btn.classList.add(styles.bgGreen)
          }
          
        })
        
        
        
      }
      
    });
  }
  const checkDraw = () =>{
    console.log('checking draw')
    return btnsValue.every(row=> row.includes("") ? false:true);
    
    
  }


  useEffect(()=>{
    console.log('handlePlay')
    checkWin();
    if(!isOver){
      if(checkDraw()){
        isOver = true
        console.log('draw')
        const allBtns = document.querySelectorAll("[id^='btn']");
        allBtns.forEach(btn=>{
      btn.classList.add(styles.bgYellow)
    })
      }
    }
  },[btnsValue])

  const restartGame = () =>{
    setBtnsValue([["","",""],["","",""],["","",""]])
    isOver = false;
    isOTurn  = !isLastTurnWasO
    isLastTurnWasO = !isLastTurnWasO
    const btnsGreen = document.querySelectorAll(`.${styles.bgGreen},.${styles.bgYellow}`);
    btnsGreen.forEach(btn=>{
      btn.classList.remove(styles.bgGreen,styles.bgYellow)
    })
    
  }

  return (
    <section>
      <div></div>
      <div className={styles.btnsSection}>
        {btnsValue.map((row, rowIndex) => (
          <div >
            {row.map((col, colIndex) => (
              <button
                
                id={`btn${rowIndex * 3 + colIndex + 1}`}
                onClick={() => clickedOn([rowIndex, colIndex])}
              >
                {col}
              </button>
            ))}
          </div>
        ))}
      </div>
      <div>
        <button onClick={restartGame}>Restart</button>
      </div>
    </section>
  );
  
  
}

export default function Home() {
  
  return (
    <>  
      <GameSection />  
    </>
  )
  }
