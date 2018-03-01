## Anthony Dike 
## Decision Tree Model

from sklearn import tree

#THIS IS THE DATA SET

#[ht, wt, shoe size]
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37],
	 [166,65,40], [190,90,47], [175,64,39], [177,70,40], 
	 [159,55,37], [171,75,42], [181,85,43] ]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 
	 'male', 'female', 'male', 'fe male', 'male', ]

#classifier
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

#displays a prediction to what the algorithm considers male or female
prediction =clf.predict([[190,70,43]])

print prediction