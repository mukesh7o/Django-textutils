analyzed = ""
for char in A:
    if char != "/n":
        analyzed += char
params = {'purpose': "Removed New line", "Analyzed_text": analyzed}
return render(request, "rpunc.html", params)
