1. 그룹화

GROUP BY 명령어를 통해 특정 컬럼을 기준으로 그룹화 할 수 있습니다.

그룹화를 하면 조회된 데이터의 통계를 내기 위한 집계함수(count, avg, sum, max, min)를 사용하기에 용이해집니다.

![image](https://github.com/jyzayu/TIL/assets/55649979/bddd54d4-ad7d-4f8b-bdc3-56ba645656aa)

위와 같은 테이블이 있을 때,아래는 name 컬럼을 기준으로 그룹화해 집계함수(COUNT(Name), SUM(Quantity) )를 하는 예제를 보여줍니다.

SELECT name, COUNT(name), SUM(quantity) FROM table1 GROUP BY name;

결과는 다음과 같이 name으로 그룹화 한 후, 집계를 실행합니다.



![image](https://github.com/jyzayu/TIL/assets/55649979/2f6c54d6-36a1-4c63-84d9-befd406d59cf)

GROUP BY로 그룹화 하지 않은 컬럼은 SELECT 해도 정확한 데이터가 나오지 않습니다.

즉, 그룹화 하지 않은 컬럼은 집계함수를 통해서만 조회하도록 해야 합니다.

아래는 그룹화 컬럼이 아닌 quantity 컬럼도 조회하는 경우의 예제입니다.

SELECT name, quantity, COUNT(name), SUM(quantity) FROM table1 GROUP BY name;

![image](https://github.com/jyzayu/TIL/assets/55649979/a82d3eb8-d7af-4c9f-a6dc-a30a00e1f8d5)


![image](https://github.com/jyzayu/TIL/assets/55649979/c532b7b8-fee7-4fb4-9fbe-16e6d5004a4c)

위 예에서 name 컬럼 값이 item1인 데이터가 2개가 있지만, GROUP BY 명령어 실행 후 1개밖에 보이지 않습니다.

GROUP BY는 DISTINCT와 같이 중복 데이터를 제거하는 것을 알 수 있습니다. 

이로써, 집계함수를 사용하여 특정 GROUP으로 분류하고 정렬이 필요하다면 GROP BY절을, 

특정 GROUP 구분없이 단순히 중복 제거가 필요할 경우 DISTINCT를 사용하는 것이 좋습니다. 

(속도면에서 이득) 다음은 GROUP BY 절과 정렬( ORDER BY )를 함께 실행한 예시입니다.


SELECT name, COUNT(name), SUM(quantity) FROM table1 GROUP BY name ORDER BY SUM(quantity) DESC;
 
 SELECT 쿼리 조회 순서에 따르면, ORDER BY는 GROUP BY보다 나중에 실행됩니다. 

 수행 순서는 아래와 같습니다. 
   
   FROM 
   
   WHERE 
   
   GROUP BY 
   
   HAVING 
   
   SELECT 
   
   ORDER BY 
   
   LIMIT 
    

2. HAVING

GROUP BY 절에서 조건을 주려면 WHERE이 아닌, HAVING 절을 사용해야 합니다.

위의 SELECT 실행 순서를 보면 WHERE 절이 GROUP BY 보다 먼저 실행되기 때문에,

GROUP BY에 대응되는 HAVING절이 있습니다. HAVING 은 GROUP BY 뒤에 작성하며, 

WHERE와 동일한 형식으로 조건을 작성할 수 있습니다.


아래는 name 컬럼을 기준으로 그룹화 하는데, 그룹화한 항목의 개수가 1인 데이터들만 조회하는 예제입니다.
![image](https://github.com/jyzayu/TIL/assets/55649979/30b25550-0dde-4b28-9c72-8559e671bb45)

출처: https://dev-coco.tistory.com/58 [슬기로운 개발생활:티스토리]
