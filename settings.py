#  A: NIPS,ICML,ACL,AAAI,IJCAI, ICLR, SIGIR, SIGKDD,WWW,ICDE
#  B: EMNLP,COLING,UAI,KR,COLT

resources=[]

###############  2020 ######################





################## 2019 ########################

# onedict={
#     'publication': 'NIPS 2019',
#     'urllist': ['https://dblp.org/db/conf/nips/nips2019'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)
onedict={
    'publication': 'NIPS 2019',
    'urllist': ['https://nips.cc/Conferences/2019/AcceptedPapersInitial'],
    'titlepatten': '<p><b>(.*?)</b><br><i>'
}
resources.append(onedict)


# onedict={
#     'publication': 'EMNLP 2019',
#     'urllist': ['https://dblp.org/db/conf/emnlp/emnlp2019'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)

onedict={
    'publication': 'EMNLP 2019',
    'urllist': ['https://www.emnlp-ijcnlp2019.org/program/accepted/'],
    'titlepatten': '<li><span style="color:cornflowerblue">(.*?)</span>',
}
resources.append(onedict)


onedict={
    'publication': 'ICML 2019',
    'urllist': ['https://dblp.org/db/conf/icml/icml2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> '
}
resources.append(onedict)

onedict={
    'publication': 'ACL 2019',
    'urllist': ['https://dblp.org/db/conf/acl/acl2019-1', 'https://dblp.org/db/conf/acl/acl2019-2'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'AAAI 2019',
    'urllist': ['https://dblp.org/db/conf/aaai/aaai2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICLR 2019',
    'urllist': ['https://dblp.org/db/conf/iclr/iclr2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'IJCAI 2019',
    'urllist': ['https://dblp.org/db/conf/ijcai/ijcai2019.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGIR 2019',
    'urllist': ['https://dblp.org/db/conf/sigir/sigir2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGKDD 2019',
    'urllist': ['https://dblp.org/db/conf/kdd/kdd2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'WWW 2019',
    'urllist': ['https://dblp.org/db/conf/www/www2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICDE 2019',
    'urllist': ['https://dblp.org/db/conf/icde/icde2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)



onedict={
    'publication': 'UAI 2019',
    'urllist': ['https://dblp.org/db/conf/uai/uai2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict = {
    'publication': 'CLOT 2019',
    'urllist': ['https://dblp.org/db/conf/colt/colt2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

# onedict={
#     'publication': 'COLING 2019',
#     'urllist': ['https://dblp.org/db/conf/coling/coling2019.html'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)

# onedict={
#     'publication': 'KR 2019',
#     'urllist': ['https://dblp.org/db/conf/kr/kr2019'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)











################## 2018 ########################
onedict={
    'publication': 'ICML 2018',
    'urllist': ['https://dblp.org/db/conf/icml/icml2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> '
 }
resources.append(onedict)

onedict={
    'publication': 'NIPS 2018',
    'urllist': ['https://dblp.org/db/conf/nips/nips2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ACL 2018',
    'urllist': ['https://dblp.org/db/conf/acl/acl2018-1', 'https://dblp.org/db/conf/acl/acl2018-2'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'AAAI 2018',
    'urllist': ['https://dblp.org/db/conf/aaai/aaai2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICLR 2018',
    'urllist': ['https://dblp.org/db/conf/iclr/iclr2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'IJCAI 2018',
    'urllist': ['https://dblp.org/db/conf/ijcai/ijcai2018.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGIR 2018',
    'urllist': ['https://dblp.org/db/conf/sigir/sigir2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGKDD 2018',
    'urllist': ['https://dblp.org/db/conf/kdd/kdd2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'WWW 2018',
    'urllist': ['https://dblp.org/db/conf/www/www2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICDE 2018',
    'urllist': ['https://dblp.org/db/conf/icde/icde2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'EMNLP 2018',
    'urllist': ['https://dblp.org/db/conf/emnlp/emnlp2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'COLING 2018',
    'urllist': ['https://dblp.org/db/conf/coling/coling2018.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'UAI 2018',
    'urllist': ['https://dblp.org/db/conf/uai/uai2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'KR 2018',
    'urllist': ['https://dblp.org/db/conf/kr/kr2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'CLOT 2018',
    'urllist': ['https://dblp.org/db/conf/colt/colt2018'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


################## 2017 ########################
onedict={
    'publication': 'ICML 2017',
    'urllist': ['https://dblp.org/db/conf/icml/icml2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'NIPS 2017',
    'urllist': ['https://dblp.org/db/conf/nips/nips2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ACL 2017',
    'urllist': ['https://dblp.org/db/conf/acl/acl2017-1', 'https://dblp.org/db/conf/acl/acl2017-2'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'AAAI 2017',
    'urllist': ['https://dblp.org/db/conf/aaai/aaai2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICLR 2017',
    'urllist': ['https://dblp.org/db/conf/iclr/iclr2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'IJCAI 2017',
    'urllist': ['https://dblp.org/db/conf/ijcai/ijcai2017.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGIR 2017',
    'urllist': ['https://dblp.org/db/conf/sigir/sigir2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGKDD 2017',
    'urllist': ['https://dblp.org/db/conf/kdd/kdd2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'WWW 2017',
    'urllist': ['https://dblp.org/db/conf/www/www2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICDE 2017',
    'urllist': ['https://dblp.org/db/conf/icde/icde2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'EMNLP 2017',
    'urllist': ['https://dblp.org/db/conf/emnlp/emnlp2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

# onedict={
#     'publication': 'COLING 2017',
#     'urllist': ['https://dblp.org/db/conf/coling/coling2017.html'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)

onedict={
    'publication': 'UAI 2017',
    'urllist': ['https://dblp.org/db/conf/uai/uai2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

# onedict={
#     'publication': 'KR 2017',
#     'urllist': ['https://dblp.org/db/conf/kr/kr2017'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)

onedict={
    'publication': 'CLOT 2017',
    'urllist': ['https://dblp.org/db/conf/colt/colt2017'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)



################## 2016 ########################
onedict={
    'publication': 'ICML 2016',
    'urllist': ['https://dblp.org/db/conf/icml/icml2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'NIPS 2016',
    'urllist': ['https://dblp.org/db/conf/nips/nips2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ACL 2016',
    'urllist': ['https://dblp.org/db/conf/acl/acl2016-1', 'https://dblp.org/db/conf/acl/acl2016-2'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'AAAI 2016',
    'urllist': ['https://dblp.org/db/conf/aaai/aaai2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICLR 2016',
    'urllist': ['https://dblp.org/db/conf/iclr/iclr2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'IJCAI 2016',
    'urllist': ['https://dblp.org/db/conf/ijcai/ijcai2016.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGIR 2016',
    'urllist': ['https://dblp.org/db/conf/sigir/sigir2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGKDD 2016',
    'urllist': ['https://dblp.org/db/conf/kdd/kdd2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'WWW 2016',
    'urllist': ['https://dblp.org/db/conf/www/www2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICDE 2016',
    'urllist': ['https://dblp.org/db/conf/icde/icde2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'EMNLP 2016',
    'urllist': ['https://dblp.org/db/conf/emnlp/emnlp2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'COLING 2016',
    'urllist': ['https://dblp.org/db/conf/coling/coling2016.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'UAI 2016',
    'urllist': ['https://dblp.org/db/conf/uai/uai2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'KR 2016',
    'urllist': ['https://dblp.org/db/conf/kr/kr2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'CLOT 2016',
    'urllist': ['https://dblp.org/db/conf/colt/colt2016'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

#
################## 2015 ########################
onedict={
    'publication': 'ICML 2015',
    'urllist': ['https://dblp.org/db/conf/icml/icml2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> '
}
resources.append(onedict)

onedict={
    'publication': 'NIPS 2015',
    'urllist': ['https://dblp.org/db/conf/nips/nips2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ACL 2015',
    'urllist': ['https://dblp.org/db/conf/acl/acl2015-1', 'https://dblp.org/db/conf/acl/acl2015-2'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'AAAI 2015',
    'urllist': ['https://dblp.org/db/conf/aaai/aaai2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICLR 2015',
    'urllist': ['https://dblp.org/db/conf/iclr/iclr2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'IJCAI 2015',
    'urllist': ['https://dblp.org/db/conf/ijcai/ijcai2015.html'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGIR 2015',
    'urllist': ['https://dblp.org/db/conf/sigir/sigir2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'SIGKDD 2015',
    'urllist': ['https://dblp.org/db/conf/kdd/kdd2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'WWW 2015',
    'urllist': ['https://dblp.org/db/conf/www/www2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

onedict={
    'publication': 'ICDE 2015',
    'urllist': ['https://dblp.org/db/conf/icde/icde2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)


onedict={
    'publication': 'EMNLP 2015',
    'urllist': ['https://dblp.org/db/conf/emnlp/emnlp2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

# onedict={
#     'publication': 'COLING 2015',
#     'urllist': ['https://dblp.org/db/conf/coling/coling2015.html'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)

onedict={
    'publication': 'UAI 2015',
    'urllist': ['https://dblp.org/db/conf/uai/uai2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)

# onedict={
#     'publication': 'KR 2015',
#     'urllist': ['https://dblp.org/db/conf/kr/kr2015'],
#     'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
# }
# resources.append(onedict)

onedict = {
    'publication': 'CLOT 2015',
    'urllist': ['https://dblp.org/db/conf/colt/colt2015'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
}
resources.append(onedict)