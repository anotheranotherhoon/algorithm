function solution(left, right) {
    var count = 0;
    var answer = 0;
    for(var i=left; i<=right; i++){
        for(var j=1; j<=i; j++){
            if(i%j === 0 ){
                count += 1;
            }
        }
        if(count % 2 === 0){
            answer += i;
        }else{
            answer -= i;
        }
        count =0;
    }
    return answer;
}

function solution(left, right) {
    var answer = 0;
    for(let i=left; i<right+1; i++){
        var cnt = 0
        for(let j=1; j<i+1; j++){
            if(i%j==0){
                cnt+=1;
            }
        }
        if(cnt % 2 ==0){
            answer += i;
        }else{
            answer -= j;
        }
    }
    return answer;
}