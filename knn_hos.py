#import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load iris dataset
iris = load_iris()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Experiment with different'n_neighbors' values
neighbor_values = [1, 3, 5, 7, 9]

for n_neighbor in neighbor_values:
    # Create a K-nearst neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=n_neighbor)

    # Train the classifier
    knn.fit(X_train, y_train)

    # Predict the class labels for the test set
    y_pred = knn.predict(X_test)

    # Calculate the accuracy of the classifier
    accuracy = accuracy_score(y_test, y_pred)

    # Print the predicted results
    print(f"n_neighbors = {n_neighbor}: Accuracy = {accuracy}")
    print(y_pred)
    print(y_test)
    print()
    