import matplotlib.pyplot as plt

# Traffic Intensity (rho) values 
rho = [0.5, 0.7, 0.9]

# --- Data Extraction (Mean Queue Wait Time Wq in seconds) ---
# Power of Parallelization Data 
wq_mm1 = [1.000, 2.333, 9.000]
wq_mm2 = [0.333, 0.961, 4.263]
wq_mm3 = [0.158, 0.547, 2.724]

# Cost of Priority Data 
wq_class1_high = [0.556, 0.814, 1.098]
wq_class2_low = [1.111, 2.713, 10.976]

# --- Setup the Figure ---
# Create a 1x2 grid of subplots for presentation side-by-side format
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('OMNET++ Queueing Systems: Performance Trends', fontsize=16, fontweight='bold', y=1.05)

# --- Plot 1: Power of Parallelization ---
ax1.plot(rho, wq_mm1, marker='o', linewidth=2, markersize=8, label='M/M/1 (1 Server)', color='#d62728')
ax1.plot(rho, wq_mm2, marker='s', linewidth=2, markersize=8, label='M/M/2 (2 Servers)', color='#1f77b4')
ax1.plot(rho, wq_mm3, marker='^', linewidth=2, markersize=8, label='M/M/3 (3 Servers)', color='#2ca02c')

ax1.set_title('Power of Parallelization', fontsize=14, pad=10)
ax1.set_xlabel('Traffic Load (rho)', fontsize=12)
ax1.set_ylabel('Mean Queue Wait Time - Wq (seconds)', fontsize=12)
ax1.set_xticks(rho)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(fontsize=11, loc='upper left')

# --- Plot 2: Cost of Priority ---
ax2.plot(rho, wq_class2_low, marker='X', linewidth=2, markersize=8, label='Low Priority (Class 2)', color='#9467bd')
ax2.plot(rho, wq_mm1, marker='o', linewidth=2, markersize=8, linestyle='--', label='Baseline M/M/1 (No Priority)', color='#7f7f7f')
ax2.plot(rho, wq_class1_high, marker='D', linewidth=2, markersize=8, label='High Priority (Class 1)', color='#ff7f0e')

ax2.set_title('The Cost of Priority Scheduling', fontsize=14, pad=10)
ax2.set_xlabel('Traffic Load (rho)', fontsize=12)
ax2.set_ylabel('Mean Queue Wait Time - Wq (seconds)', fontsize=12)
ax2.set_xticks(rho)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(fontsize=11, loc='upper left')

# --- Formatting and Saving ---
plt.tight_layout()
plt.savefig('queueing_trends.png', dpi=300, bbox_inches='tight') # Saves a high-quality image for the slides
plt.show() # Displays the interactive plot window