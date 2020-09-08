function p = predictOneVsAll(all_theta, X)

m = size(X, 1);
num_labels = size(all_theta, 1);
% Add ones to the X data matrix
X = [ones(m, 1) X];
predictions = X*all_theta';
[throwaway,p] = max(predictions,[],2);

end
