"""
Solution 03 | Report 

To understand the effect of different values of n and sigma, I used the programs written in Sol_1 and Sol_2.

---------------------------------------------------------------------------------------

1. Effect of Dataset Size (n) : Using Sol_1 and Sol_2, I tested the model with different values of n while keeping sigma the same.

- n = 50:
  The model learned the beta values, but the results were
  not very accurate.

- n = 500:
  The model performed better and the beta values became
  more accurate.

- n = 5000:
  The learned beta values were very close to the original
  beta values.

Conclusion: Increasing the value of n helps the model learn better because it has more data to train on.

---------------------------------------------------------------------------------------

2. Effect of Noise (sigma): Using Sol_1 and Sol_2, I tested the model with different
values of sigma while keeping n the same.

- sigma = 0.1:
  The model learned the beta values very well.

- sigma = 1:
  The model still gave good results.

- sigma = 5:
  The error increased and the beta values became less accurate.

- sigma = 10:
  The model found it difficult to learn the correct beta values.

---------------------------------------------------------------------------------------

Final Conclusion: Based on the results from Sol_1 and Sol_2, I found that a larger value of n improves the learning of the model, while a larger value of sigma reduces its accuracy. The best results are obtained when the dataset size is large and the noise is small.

"""