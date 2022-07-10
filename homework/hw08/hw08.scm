(define (my-filter func lst)  
 (cond 
   ((null? lst) '())
   ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
   (else (my-filter func (cdr lst)))
 )
)

(define (interleave s1 s2) 
 (cond
   ((and (null? s1) (null? s2)) '())
   ((and (not (null? s1)) (null? s2)) s1)
   ((and (not (null? s2)) (null? s1)) s2)
   (else (cons (car s1) (cons (car s2) (interleave (cdr s1) (cdr s2)))))
 )
)

(define (accumulate merger start n term)
 (if (= n 1)
     (merger start (term n))
     (merger (term n) (accumulate merger start (- n 1) term)) 
 )
)

(define (no-repeats lst) 
 (cond
   ((null? lst) '())
   (else (cons (car lst) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst))))) 
 )
)


