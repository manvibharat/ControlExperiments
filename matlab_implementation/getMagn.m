function [mag] = getMagn( t,input,output,f )


time = t;
voltage = input;
theta = output;
dt = time(2)-time(1);
[voltage_peaks, l_vp] = findpeaks(voltage);
freq=f;

if size(voltage_peaks,1)<2
    error('Data must contain atleast one complete peak-to-peak.')
end


[theta_peaks,l_tp] = findpeaks(theta);
[theta_troughs,l_tt] = findpeaks(-theta);
theta_troughs = -theta_troughs;
if size(theta_peaks,1)>size(theta_troughs,1)
    mag = mean(theta_peaks(1:size(theta_troughs,1))-theta_troughs)/2;
else
    mag = mean(theta_peaks-theta_troughs(1:size(theta_peaks,1)))/2;
end
mag = mag/voltage_peaks(1);

if size(theta_peaks,1)>size(voltage_peaks,1)
    phase = mean((l_vp-l_tp(1:size(voltage_peaks,1))).*dt)*freq*2*pi;
else
    phase = mean((l_vp(1:size(theta_peaks,1))-l_tp).*dt)*freq*2*pi;
end
phase = wrapToPi(phase);
phase = phase*180/pi;

end

