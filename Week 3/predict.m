function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

x = [ones(m, 1) X];
a1 = [ones(m,1) sigmoid(x*Theta1')];
a2 = sigmoid(a1*Theta2');
 
[throwaway,p] = max(a2,[],2);


end
