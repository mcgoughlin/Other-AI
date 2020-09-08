function [J, grad] = costFunction(theta, X, y)
% Initialize some useful values
m = length(y); % number of training examples
n = length(theta); % number of input variables + 1
grad = zeros(size(theta)); % gradient adjustments to theta

z = sigmoid(X*theta); %guesses made my logistical regression

Js = y.*(-log(z)) - (1-y).* log(1-z);
J = (1/m)*sum(Js);

errors = z-y; % sum the differences between regressed answers and labels

grad(1) = sum(errors);
for j = 2:n
    grad(j) = sum(errors.*X(:,j));
end

grad = grad./m;

end
