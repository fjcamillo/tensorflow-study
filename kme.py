import tensorflow as tf
import numpy as np
from km import create_samples, plot_clusters
n_features = 2
n_clusters = 3
n_samples_per_clusters = 500
seed = 700
embiggen_factor = 70

np.random.seed(seed)
centroids, samples = create_samples(n_clusters, n_samples_per_clusters, n_features, embiggen_factor, seed)

model = tf.initialize_all_variables()
with tf.Session() as sess:
    samples_values = sess.run(samples)
    centroid_values = sess.run(centroids)
    plot_clusters(samples_values, centroid_values, n_samples_per_clusters)
