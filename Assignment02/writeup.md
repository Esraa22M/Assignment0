# Programming-Assignment genfei challenge [Assignment2](https://github.com/Esraa22M/Assignment0/tree/master/Assignment02)
## [genfei challenge](https://cybertalents.com/challenges/cryptography/genfei)
### how to solve it 
 given [encrypt.py](https://github.com/Esraa22M/Assignment0/blob/master/Assignment02/encrypt.py) which contains
 ## encrypt function
   encrypt in two steps 
   
      first step

 
                 		a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337

          

      second step 
    
          		a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
     repeat the above steps 30 times
 ## decryption is the reverse of the encryption process
 * first step  decrypting the second step in encrypt
```python

    tempa = a
        d = d ^ 1337
        a = c ^ (F(d | F(d) ^ d))
        b = b ^ (F(d ^ F(a) ^ (d | a)))
        c = tempa ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
  ```      
  * second step decrypting the frist step in encrypt
  ```python

     tempa = a
        a = d ^ 31337
        d = c ^ (F(a | F(a) ^ a))
        c = b ^ (F(a ^ F(d) ^ (a | d)))
        b = tempa ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))
    ```

  * repeat the above steps 30 times 
  *  return plaintext and remove  "'"  
  *  read flag.enc  then decrypt it and then display the result after drop [#] sumbols
  * submit the code 
  
