% DrawSpline.m文件
function DrawSpline(n, k, P, NodeVector)
% B样条的绘图函数
% 已知n+1个控制顶点P(i), k次B样条，P是2*(n+1)矩阵存控制顶点坐标, 节点向量NodeVector
plot(P(1, 1:n+1), P(2, 1:n+1),...
                    'o','LineWidth',1,...
                    'MarkerEdgeColor','k',...
                    'MarkerFaceColor','g',...
                    'MarkerSize',6);
line(P(1, 1:n+1), P(2, 1:n+1));
Nik = zeros(n+1, 1);
arr = zeros(2,200);
for u = 0 : 0.005 : 1-0.005
    for i = 0 : 1 : n
        Nik(i+1, 1) = BaseFunction(i, k , u, NodeVector);
    end
    p_u = P * Nik;
    t = floor(u/0.005 + 1);
    if u == 0
        tempx = p_u(1,1);
        tempy = p_u(2,1);
        disp(t)
        disp(tempx)
        disp(tempy)
        arr(1,t) = tempx;
        arr(2,t) = tempy;
        line([tempx p_u(1,1)], [tempy p_u(2,1)],...
            'Marker','.','LineStyle','-', 'Color',[.3 .6 .9], 'LineWidth',3);
    else
        line([tempx p_u(1,1)], [tempy p_u(2,1)],...
            'Marker','.','LineStyle','-', 'Color',[.3 .6 .9], 'LineWidth',3);
        tempx = p_u(1,1);
        tempy = p_u(2,1);
        disp(t)
        disp(tempx)
        disp(tempy)
        arr(1,t) = tempx;
        arr(2,t) = tempy;
    end
end
save save arr;
end