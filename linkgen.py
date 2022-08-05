def link(inp):
    last="&op=translate"
    ini="https://translate.google.co.in/?sl=en&tl=sa&text="
    l=inp
    final=ini
    for i in l.split():
        kk=i+"%20"
        final+=kk
    final+=last
    return final
# dharmasya%20glanir%20bhavati%20Bharata
