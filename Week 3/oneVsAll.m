function [all_theta] = oneVsAll(X, y, num_labels, lambda)
% Some useful variables
m = size(X, 1);
n = size(X, 2);

% You need to return the following variables correctly 
all_theta = zeros(num_labels, n + 1);
X = [ones(m, 1) X];
options = optimset('GradObj', 'on', 'MaxIter', 50);

% for epoch = 1:5
    for i = 1:num_labels
       initial_theta = all_theta(i,:);
       cf = @(t)(lrCostFunction(t', X, (y == i), lambda));
       theta = fminunc(cf,initial_theta,options);
       all_theta(i, :) = theta;
    end
% end

end
