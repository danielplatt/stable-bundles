
alpha_beta_gamma_number_options = 0
for k in [0,1,2]:
    for l in range(k+1):
        for m in range (l+1):
            if k+l+m <= 3 and k+l+m > 0:
                alpha_beta_gamma_number_options += 1
                print(k,l,m)

tau_number_options = 0
for k in [0,1,2,3,4,5,6,7]:
    for l in range(k+1):
        for m in range (l+1):
            if k+l+m <= 7 and k+l+m > 2 and k != 0 and l != 0:
                tau_number_options += 1
                print(k,l,m)

print(f'alpha_beta_gamma_number_options={alpha_beta_gamma_number_options}')
print(f'tau_number_options={tau_number_options}')
print(f'product={alpha_beta_gamma_number_options*tau_number_options}')