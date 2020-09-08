function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
n = length(X(1,:));
J_history = zeros(num_iters, 1);
adjustments = zeros(n,1);
for iter = 1:num_iters
    J_history(iter) = computeCost(X,y,theta);
    error = X*theta-y;
    adj = X.*error;
    for i = 1:n
        adjustments(i) = sum(adj(:,i));
    end
    theta = theta-(alpha/m)*adjustments;
end

end
