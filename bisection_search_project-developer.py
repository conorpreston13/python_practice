from demos import bisection_iter, analyze_func, generate_emails

list_of_domains = ['example1.com', 'example2.com', 'example3.com']
emails = generate_emails(10, list_of_domains, 1000000)

email = 'conor@example.com'
emails.append(email)

sorted_emails = sorted(emails)

index, found = bisection_iter(email, sorted_emails)

print(found)

if index:
    print(f"element at index: {index} is {sorted_emails[index]}")

analyze_func(bisection_iter, email, sorted_emails)
analyze_func(generate_emails, 10, list_of_domains, 1000000)
