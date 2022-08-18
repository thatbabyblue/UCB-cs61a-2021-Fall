(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ordered? s) (if (null? (cdr s)) #t (if (<= (car s) (car (cdr s))) (ordered? (cdr s)) #f)))

(define (square x) (* x x))

(define (pow base exp) 
    (cond ((zero? exp) 1)
          ((odd? exp) (* base (pow base (- exp 1))))
          (else (square (pow base (quotient exp 2))))
    )
)


