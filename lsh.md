# Introduction to Locality Sensitive Hashing: Random Projection Method
## Idea behind this method

Consider a image dataset matrix `D` with `n` vectors of size `d`. This database `D` can be projected onto a lower dimensional space with `n` vectors of size `k` using a random projection matrix.

## Algorithm

We construct a table of all possible bins where each bin is made up of similar items. Each bin can be represented by a bitwise hash value so that two images with same bitwise hash values are more likely to be similar than those with different hashes.

Steps to generate a bitwise hash table (this is our `hash_table.py`):

1. Create `k` random vectors of length `d` each, where `k` is the size of bitwise hash value and `d` is the dimension of the feature vector (in our case, this is the dimension of the image).
2. For each random vector, compute the dot product of the random vector and the image. If the result of the dot product is positive, assign the bit value as 1, else 0.
3. Concatenate all the bit values computed for `k` dot products.
4. Repeat the above two steps for all images to compute hash values for all images.
5. Group images with same hash values together to create a LSH table.


In addition, because of the randomness, it is not likely that all similar items are grouped correctly. To overcome this limitation, a common practice is to create multiple hash tables and consider an image `a` to be similar to image `b`, if they are in same bin in at least one of the tables. It is also worth noting that multiple tables generalize the high dimensional space better and amortize the contribution of bad random vectors.

In practice, the number of hash tables and size of the hash value `k` are tuned to adjust the trade-off between recall and precision.

`lsh.py` contains construction of multiple hash tables.
