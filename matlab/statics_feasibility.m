function statics_feasibility(output_dir, mu_s)
% Original AI instructional reference; NOT executed in MATLAB in this session.
% Calculated force/friction model, not measured data. Base MATLAB only.
% Attempt the model yourself first. Then independently modify a parameter.
% Example: statics_feasibility('chosen-output-folder', 0.4)
% p = P/(M*g), n = N/(M*g), f = signed friction/(M*g).
if nargin ~= 2
    error('Supply an explicit output directory and mu_s.');
end
validateattributes(mu_s, {'numeric'}, {'real','scalar','finite','nonnegative'});
if ~exist(output_dir, 'dir')
    mkdir(output_dir);
end
theta_deg = linspace(0, 89.5, 400);
p = linspace(0, 2, 401);
[theta, push] = meshgrid(theta_deg*pi/180, p);
n = cos(theta) + push.*sin(theta);
f = sin(theta) - push.*cos(theta);
admissible = (n >= 0) & (abs(f) <= mu_s*n);
fig = figure('Color','w');
imagesc(theta_deg, p, double(admissible));
set(gca,'YDir','normal');
colormap([0.97 0.94 0.92; 0.64 0.81 0.78]);
caxis([0 1]);
hold on;
plot(theta_deg, tan(theta_deg*pi/180), '--', 'Color',[0.32 0.27 0.49], 'LineWidth',1.5);
xlim([0 89]); ylim([0 2]);
xlabel('Inclination theta (degrees)');
ylabel('Horizontal push P/(M g)');
title(sprintf('Calculated force/friction feasibility, mu_s = %.3g',mu_s));
% Green satisfies force/friction inequalities. Finite-body tipping is omitted.
% The dashed curve is f = 0; above/below it friction has opposite signs.
print(fig, fullfile(output_dir,'statics_feasibility.png'), '-dpng', '-r150');
end
