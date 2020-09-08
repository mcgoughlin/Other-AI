function plotData(X, y)
figure; hold on;

for i = 1:length(y)
    if y(i) == 1
        plot(X(i,1),X(i,2),'r+')
    else
        plot(X(i,1),X(i,2),'ko')
    end
end
hold off;

end
