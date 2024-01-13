function solution(arr)
{
    let stack = [];
    arr.forEach((e) => {
        if (stack[stack.length - 1] !== e) {stack.push(e)}
        
    })

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log(stack)
    
    return stack;
}