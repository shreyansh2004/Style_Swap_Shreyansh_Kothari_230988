# GANs task (finally)

### Objective
In this task you'll use GANs to generate 'photorealistic' images on the dataset of collection of pokemon sprites obtained from [pokemondb](https://pokemondb.net/sprites). Borrow the convolutional architecture from the deep convolutional GANs (DCGAN) introduced in this [paper](https://arxiv.org/pdf/1511.06434).

For downloading the dataset use the following link:
~http://d2l-data.s3-accelerate.amazonaws.com/pokemon.zip~
https://drive.google.com/file/d/1LvXH0NLp-jwI2FVkl9HgH6urv64xA0Jq/view?usp=sharing
For your ease it is recommended to write a download and extract function in the code itself which will use this link to download the data.
### Rules
- The code should be in pytorch.
- Do not use libraries like labml, d2l, mxnet.
- Deadline 5th June EOD.

### Deliverables
- Notebook with all the code ofc.
- A writeup in markdown/latex:
	- With explanation of major points of the GANs & DCGANs.
	- The technicalities of your task like explaining the images, resizing, dimension changes in generator/discriminator networks etc.
	- Results of different experimentations you did.

### Additional
- The task is not that computationally expensive, can be done using the free tier T4 GPU of google colab.
- Following are the results from the code we wrote and trained on 20 epochs:
- EPOCH 1:
<p align="center">
  <img src="https://github.com/qu-bit1/style-swap/blob/master/week3/e1.png" />
</p>
- EPOCH 7:
<p align="center">
  <img src="https://github.com/qu-bit1/style-swap/blob/master/week3/e7.png" />
</p>
- EPOCH 20:
<p align="center">
  <img src="https://github.com/qu-bit1/style-swap/blob/master/week3/e20.png" />
</p>
- So don't worry if your code doesn't produce exactly 'photorealistic images', the only requirement of this task is that you should be able to show that your model is learning, that's enough (or maybe run your code for more epochs or do whatever and show us some new pokemons lol).