# 3-Board Misere Tic-Tac-Toe
#
# Reference:
# Plambeck, Thane E., and Greg Whitehead.
# "The Secrets of Notakto: Winning at X-only Tic-Tac-Toe."
# arXiv preprint arXiv:1301.1672 (2013).

import random
import copy

# The dict storing the map from board state to element in commutative monoid
# This dict is pre-calculated offline
boardDict = {'#145678': [0, 0, 0, 0], '#01234678': [0, 0, 0, 0], '#0137': [1, 0, 0, 0], '#012345': [0, 0, 0, 0], '#0124678': [0, 0, 0, 0], '#04578': [0, 0, 0, 0], '#135678': [0, 0, 0, 0], '#03578': [0, 1, 0, 0], '#0238': [0, 1, 0, 0], '#012458': [0, 0, 0, 0], '#048': [0, 0, 0, 0], '#045': [1, 0, 0, 0], '#014678': [0, 0, 0, 0], '#047': [1, 0, 0, 0], '#012457': [0, 0, 0, 0], '#0235': [0, 1, 0, 0], '#23568': [0, 0, 0, 0], '#0234': [0, 1, 0, 0], '#23567': [0, 1, 0, 0], '#3456': [0, 0, 0, 0], '#3457': [0, 0, 0, 0], '#3458': [0, 0, 0, 0], '#012357': [0, 0, 0, 0], '#012356': [0, 0, 0, 0], '#04568': [0, 0, 0, 0], '#38': [0, 1, 0, 0], '#35': [1, 0, 0, 0], '#34': [0, 1, 0, 0], '#37': [1, 0, 0, 0], '#36': [1, 0, 0, 1], '#012358': [0, 0, 0, 0], '#123567': [0, 0, 0, 0], '#134': [1, 1, 0, 0], '#137': [0, 1, 0, 0], '#136': [0, 0, 0, 1], '#138': [0, 0, 0, 0], '#123568': [0, 0, 0, 0], '#123678': [0, 0, 0, 0], '#038': [0, 0, 0, 1], '#01348': [0, 0, 0, 0], '#13678': [0, 0, 0, 0], '#01346': [0, 0, 0, 0], '#036': [0, 0, 0, 0], '#037': [0, 0, 0, 1], '#145': [1, 1, 0, 0], '#0136': [0, 0, 0, 0], '#146': [1, 0, 0, 0], '#0134': [1, 0, 0, 0], '#0135': [1, 0, 0, 0], '#0138': [1, 0, 0, 0], '#01234': [0, 0, 0, 0], '#015678': [0, 0, 0, 0], '#2367': [1, 0, 0, 0], '#34567': [0, 0, 0, 0], '#34568': [0, 0, 0, 0], '#2368': [0, 1, 0, 0], '#258': [0, 0, 0, 0], '#024578': [0, 0, 0, 0], '#256': [0, 0, 0, 1], '#257': [0, 0, 0, 1], '#013457': [0, 0, 0, 0], '#013456': [0, 0, 0, 0], '#0347': [0, 1, 0, 0], '#0346': [0, 0, 0, 0], '#0348': [0, 0, 0, 0], '#013458': [0, 0, 0, 0], '#013678': [0, 0, 0, 0], '#0123678': [0, 0, 0, 0], '#013578': [0, 0, 0, 0], '#124567': [0, 0, 0, 0], '#124568': [0, 0, 0, 0], '#1268': [0, 1, 0, 0], '#1267': [1, 0, 0, 0], '#678': [0, 0, 0, 0], '#12678': [0, 0, 0, 0], '#4568': [0, 1, 0, 0], '#13458': [0, 0, 0, 0], '#12478': [0, 0, 0, 0], '#03478': [0, 0, 0, 0], '#0134578': [0, 0, 0, 0], '#13456': [0, 0, 0, 0], '#13457': [0, 0, 0, 0], '#78': [1, 0, 0, 1], '#15678': [0, 0, 0, 0], '#1235678': [0, 0, 0, 0], '#1367': [1, 0, 0, 0], '#1368': [0, 1, 0, 0], '#123467': [0, 0, 0, 0], '#1567': [1, 1, 0, 0], '#1568': [0, 1, 0, 0], '#02478': [0, 0, 0, 0], '#178': [0, 0, 0, 1], '#01234567': [0, 0, 0, 0], '#078': [0, 0, 0, 1], '#378': [0, 0, 0, 1], '#01234568': [0, 0, 0, 0], '#0123458': [0, 0, 0, 0], '#0467': [0, 1, 0, 0], '#12356': [0, 1, 0, 0], '#12357': [0, 1, 0, 0], '#12358': [0, 0, 0, 0], '#01347': [0, 0, 0, 0], '#0468': [0, 0, 0, 0], '#0123457': [0, 0, 0, 0], '#0234567': [0, 0, 0, 0], '#0123456': [0, 0, 0, 0], '#0234568': [0, 0, 0, 0], '#3468': [0, 1, 0, 0], '#2468': [0, 0, 0, 0], '#2467': [0, 0, 0, 0], '#3467': [1, 0, 0, 0], '#234568': [0, 0, 0, 0], '#02378': [1, 0, 0, 0], '#05678': [0, 0, 0, 0], '#01578': [0, 1, 0, 0], '#234567': [0, 0, 0, 0], '#1345678': [0, 0, 0, 0], '#456': [1, 0, 0, 0], '#012456': [0, 0, 0, 0], '#24568': [0, 0, 0, 0], '#01278': [0, 0, 0, 0], '#24567': [0, 0, 0, 0], '#458': [1, 1, 0, 0], '#046': [1, 0, 0, 0], '#01378': [0, 1, 0, 0], '#0267': [0, 1, 0, 0], '#025678': [0, 0, 0, 0], '#3567': [1, 0, 0, 0], '#3568': [0, 1, 0, 0], '#0268': [1, 0, 0, 0], '#0148': [0, 0, 0, 0], '#02578': [0, 0, 0, 0], '#02368': [0, 0, 0, 0], '#0147': [0, 0, 0, 0], '#0146': [0, 1, 0, 0], '#0145': [0, 1, 0, 0], '#1234568': [0, 0, 0, 0], '#35678': [0, 0, 0, 0], '#23678': [0, 0, 0, 0], '#023567': [0, 0, 0, 0], '#134568': [0, 0, 0, 0], '#134567': [0, 0, 0, 0], '#023568': [0, 0, 0, 0], '#23478': [1, 0, 0, 0], '#03678': [0, 0, 0, 0], '#01245': [0, 0, 0, 0], '#125678': [0, 0, 0, 0], '#01457': [0, 0, 0, 0], '#01456': [1, 0, 0, 0], '#12468': [0, 0, 0, 0], '#045678': [0, 0, 0, 0], '#1234678': [0, 0, 0, 0], '#01458': [0, 0, 0, 0], '#13568': [1, 0, 0, 0], '#01467': [0, 0, 0, 0], '#0145678': [0, 0, 0, 0], '#0134567': [0, 0, 0, 0], '#568': [1, 0, 0, 0], '#13567': [0, 1, 0, 0], '#23': [0, 1, 0, 0], '#26': [1, 0, 0, 0], '#27': [0, 1, 0, 0], '#24': [0, 1, 0, 0], '#25': [1, 0, 0, 1], '#0345678': [0, 0, 0, 0], '#28': [0, 1, 0, 0], '#123458': [0, 0, 0, 0], '#1456': [0, 1, 0, 0], '#1358': [1, 1, 0, 0], '#012346': [0, 0, 0, 0], '#012347': [0, 0, 0, 0], '#245': [1, 1, 0, 0], '#012348': [0, 0, 0, 0], '#1357': [1, 0, 0, 0], '#1356': [1, 1, 0, 0], '#34678': [0, 0, 0, 0], '#01237': [0, 0, 0, 0], '#01236': [0, 0, 0, 0], '#01235': [0, 0, 0, 0], '#147': [0, 0, 0, 0], '#148': [1, 0, 0, 0], '#01238': [0, 0, 0, 0], '#123578': [0, 0, 0, 0], '#0123568': [0, 0, 0, 0], '#028': [1, 1, 0, 0], '#027': [1, 0, 0, 0], '#026': [1, 1, 0, 0], '#025': [1, 0, 0, 0], '#024': [1, 0, 0, 0], '#023': [1, 0, 0, 0], '#0123567': [0, 0, 0, 0], '#04567': [1, 0, 0, 0], '#0458': [0, 0, 0, 0], '#0124578': [0, 0, 0, 0], '#0457': [0, 1, 0, 0], '#0456': [0, 1, 0, 0], '#012467': [0, 0, 0, 0], '#012468': [0, 0, 0, 0], '#457': [1, 1, 0, 0], '#135': [0, 1, 0, 0], '#12345678': [0, 0, 0, 0], '#02346': [0, 0, 0, 0], '#02347': [1, 0, 0, 0], '#02345': [0, 0, 0, 0], '#02348': [0, 0, 0, 0], '#2378': [0, 1, 0, 0], '#01246': [0, 0, 0, 0], '#01247': [0, 0, 0, 0], '#248': [1, 0, 0, 0], '#567': [0, 0, 0, 1], '#1678': [0, 0, 0, 0], '#247': [1, 0, 0, 0], '#246': [0, 0, 0, 0], '#01248': [0, 0, 0, 0], '#124678': [0, 0, 0, 0], '#0356': [0, 0, 0, 0], '#0357': [1, 1, 0, 0], '#0358': [1, 0, 0, 0], '#2678': [0, 0, 0, 0], '#01345678': [0, 0, 0, 0], '#034578': [0, 0, 0, 0], '#034678': [0, 0, 0, 0], '#1457': [0, 0, 0, 0], '#245678': [0, 0, 0, 0], '#023456': [0, 0, 0, 0], '#023457': [0, 0, 0, 0], '#1278': [0, 1, 0, 0], '#023458': [0, 0, 0, 0], '#0678': [0, 0, 0, 0], '#4678': [0, 0, 0, 0], '#4578': [1, 0, 0, 0], '#034': [1, 1, 0, 0], '#03567': [0, 0, 0, 0], '#035': [0, 0, 0, 1], '#234678': [0, 0, 0, 0], '#03568': [0, 0, 0, 0], '#68': [0, 1, 0, 0], '#67': [1, 0, 0, 1], '#45678': [0, 0, 0, 0], '#0235678': [0, 0, 0, 0], '#235678': [0, 0, 0, 0], '#067': [1, 0, 0, 0], '#068': [1, 1, 0, 0], '#01234578': [0, 0, 0, 0], '#348': [1, 0, 0, 0], '#01468': [0, 0, 0, 0], '#12348': [1, 0, 0, 0], '#12347': [0, 0, 0, 0], '#12346': [0, 0, 0, 0], '#12345': [0, 0, 0, 0], '#346': [1, 1, 0, 0], '#347': [1, 1, 0, 0], '#345': [0, 0, 0, 0], '#3678': [0, 0, 0, 0], '#2345678': [0, 0, 0, 0], '#2458': [0, 0, 0, 0], '#3478': [0, 1, 0, 0], '#13': [1, 0, 0, 0], '#12': [1, 0, 0, 1], '#17': [1, 0, 0, 0], '#16': [0, 1, 0, 0], '#15': [1, 0, 0, 0], '#14': [0, 1, 0, 0], '#01567': [1, 0, 0, 0], '#24678': [0, 0, 0, 0], '#01568': [1, 0, 0, 0], '#01367': [0, 0, 0, 0], '#01678': [0, 0, 0, 0], '#24578': [0, 0, 0, 0], '#01368': [0, 0, 0, 0], '#0156': [0, 1, 0, 0], '#0157': [1, 1, 0, 0], '#0135678': [0, 0, 0, 0], '#0258': [0, 0, 0, 0], '#0257': [0, 1, 0, 0], '#0256': [0, 1, 0, 0], '#0158': [1, 1, 0, 0], '#02467': [0, 0, 0, 0], '#02468': [0, 0, 0, 0], '#123468': [0, 0, 0, 0], '#0478': [0, 0, 0, 0], '#236': [0, 0, 0, 1], '#237': [0, 0, 0, 0], '#234': [1, 0, 0, 0], '#235': [0, 0, 0, 1], '#1234567': [0, 0, 0, 0], '#238': [1, 0, 0, 0], '#1236': [1, 1, 0, 0], '#1237': [1, 1, 0, 0], '#1234': [0, 1, 0, 0], '#1235': [1, 0, 0, 0], '#1238': [0, 1, 0, 0], '#134678': [0, 0, 0, 0], '#01345': [0, 0, 0, 0], '#134578': [0, 0, 0, 0], '#0234578': [0, 0, 0, 0], '#8': [0, 0, 0, 0], '#3': [0, 0, 0, 0], '#2': [0, 0, 0, 0], '#1': [0, 0, 0, 0], '#0': [0, 0, 0, 0], '#7': [0, 0, 0, 0], '#6': [0, 0, 0, 0], '#5': [0, 0, 0, 0], '#4': [0, 0, 2, 0], '#': [0, 0, 1, 0], '#014578': [0, 0, 0, 0], '#012578': [0, 0, 0, 0], '#012678': [0, 0, 0, 0], '#13578': [0, 1, 0, 0], '#03457': [0, 0, 0, 0], '#03456': [0, 0, 0, 0], '#13478': [0, 0, 0, 0], '#03458': [0, 0, 0, 0], '#1458': [0, 1, 0, 0], '#57': [1, 0, 0, 0], '#56': [0, 1, 0, 0], '#58': [1, 0, 0, 1], '#1348': [0, 1, 0, 0], '#1467': [0, 0, 0, 0], '#012378': [0, 0, 0, 0], '#1468': [0, 1, 0, 0], '#1346': [0, 1, 0, 0], '#1347': [0, 0, 0, 0], '#1345': [0, 0, 0, 0], '#157': [0, 1, 0, 0], '#156': [0, 0, 0, 0], '#02458': [0, 0, 0, 0], '#02456': [0, 0, 0, 0], '#02457': [1, 0, 0, 0], '#158': [0, 0, 0, 1], '#12578': [0, 0, 0, 0], '#018': [0, 0, 0, 1], '#0123578': [0, 0, 0, 0], '#0567': [0, 1, 0, 0], '#012': [0, 0, 0, 0], '#013': [0, 1, 0, 0], '#016': [1, 0, 0, 0], '#017': [0, 0, 0, 1], '#12378': [1, 0, 0, 0], '#015': [0, 0, 0, 1], '#14578': [0, 0, 0, 0], '#0124567': [0, 0, 0, 0], '#0245678': [0, 0, 0, 0], '#0124568': [0, 0, 0, 0], '#0123478': [0, 0, 0, 0], '#14678': [0, 0, 0, 0], '#2568': [0, 0, 0, 0], '#012478': [0, 0, 0, 0], '#2567': [1, 1, 0, 0], '#2357': [1, 1, 0, 0], '#2347': [0, 1, 0, 0], '#2346': [0, 0, 0, 0], '#02357': [1, 0, 0, 0], '#02356': [0, 0, 0, 0], '#02358': [0, 0, 0, 0], '#2348': [0, 1, 0, 0], '#278': [1, 0, 0, 0], '#01257': [0, 0, 0, 0], '#01256': [0, 0, 0, 0], '#578': [0, 1, 0, 0], '#0345': [0, 0, 0, 0], '#478': [1, 1, 0, 0], '#01258': [0, 0, 0, 0], '#013478': [0, 0, 0, 0], '#0368': [0, 0, 0, 0], '#0367': [0, 0, 0, 0], '#0168': [0, 1, 0, 0], '#0167': [0, 1, 0, 0], '#034568': [0, 0, 0, 0], '#034567': [0, 0, 0, 0], '#02678': [0, 0, 0, 0], '#1248': [0, 1, 0, 0], '#023467': [0, 0, 0, 0], '#023468': [0, 0, 0, 0], '#1247': [0, 0, 0, 0], '#1246': [0, 0, 0, 0], '#1245': [1, 0, 0, 0], '#12457': [0, 0, 0, 0], '#12456': [0, 0, 0, 0], '#12458': [0, 0, 0, 0], '#01245678': [0, 0, 0, 0], '#357': [0, 1, 0, 0], '#356': [0, 0, 0, 1], '#058': [0, 0, 0, 1], '#056': [1, 0, 0, 0], '#057': [0, 0, 0, 0], '#358': [0, 0, 0, 1], '#23578': [0, 0, 0, 0], '#01478': [0, 0, 0, 0], '#024678': [0, 0, 0, 0], '#08': [1, 0, 0, 0], '#01': [1, 0, 0, 1], '#02': [0, 1, 0, 0], '#03': [1, 0, 0, 1], '#04': [0, 1, 0, 0], '#05': [0, 1, 0, 0], '#06': [0, 1, 0, 0], '#07': [0, 1, 0, 0], '#128': [1, 0, 0, 0], '#01356': [0, 0, 0, 0], '#01357': [0, 1, 0, 0], '#01358': [0, 1, 0, 0], '#123': [0, 0, 0, 1], '#126': [0, 0, 0, 1], '#127': [0, 0, 0, 1], '#124': [1, 1, 0, 0], '#125': [0, 1, 0, 0], '#0248': [0, 0, 0, 0], '#0123': [0, 0, 0, 0], '#0125': [0, 0, 0, 0], '#0124': [0, 0, 0, 0], '#0127': [0, 0, 0, 0], '#0126': [0, 0, 0, 0], '#0128': [0, 0, 0, 0], '#0245': [0, 1, 0, 0], '#0246': [0, 0, 0, 0], '#0247': [0, 1, 0, 0], '#04678': [0, 0, 0, 0], '#34578': [0, 0, 0, 0], '#0134678': [0, 0, 0, 0], '#024568': [0, 0, 0, 0], '#0568': [0, 1, 0, 0], '#1234578': [0, 0, 0, 0], '#024567': [0, 0, 0, 0], '#014': [1, 1, 0, 0], '#23458': [0, 0, 0, 0], '#23457': [0, 0, 0, 0], '#23456': [0, 0, 0, 0], '#0237': [0, 1, 0, 0], '#0236': [0, 0, 0, 0], '#013567': [0, 0, 0, 0], '#02345678': [0, 0, 0, 0], '#013568': [0, 0, 0, 0], '#124578': [0, 0, 0, 0], '#345678': [0, 0, 0, 0], '#012568': [0, 0, 0, 0], '#012567': [0, 0, 0, 0], '#023678': [0, 0, 0, 0], '#13468': [1, 0, 0, 0], '#0134568': [0, 0, 0, 0], '#03467': [0, 0, 0, 0], '#03468': [0, 0, 0, 0], '#12467': [0, 0, 0, 0], '#13467': [0, 0, 0, 0], '#45': [0, 1, 0, 0], '#46': [0, 1, 0, 0], '#47': [0, 1, 0, 0], '#123478': [0, 0, 0, 0], '#0125678': [0, 0, 0, 0], '#48': [0, 1, 0, 0], '#1378': [1, 1, 0, 0], '#1478': [0, 0, 0, 0], '#012368': [0, 0, 0, 0], '#012367': [0, 0, 0, 0], '#1578': [1, 0, 0, 0], '#12567': [0, 1, 0, 0], '#168': [1, 0, 0, 0], '#167': [0, 0, 0, 1], '#12568': [0, 0, 0, 0], '#5678': [0, 0, 0, 0], '#12367': [0, 1, 0, 0], '#368': [1, 0, 0, 0], '#0578': [1, 0, 0, 0], '#367': [0, 1, 0, 0], '#12368': [1, 0, 0, 0], '#0123467': [0, 0, 0, 0], '#14568': [1, 0, 0, 0], '#0234678': [0, 0, 0, 0], '#014567': [0, 0, 0, 0], '#014568': [0, 0, 0, 0], '#2578': [0, 0, 0, 0], '#14567': [0, 0, 0, 0], '#0123468': [0, 0, 0, 0], '#2478': [0, 1, 0, 0], '#035678': [0, 0, 0, 0], '#2358': [0, 0, 0, 0], '#234578': [0, 0, 0, 0], '#267': [0, 0, 0, 1], '#268': [1, 1, 0, 0], '#2356': [1, 0, 0, 0], '#02367': [0, 0, 0, 0], '#4567': [0, 1, 0, 0], '#01235678': [0, 0, 0, 0], '#467': [1, 1, 0, 0], '#01267': [0, 0, 0, 0], '#01268': [0, 0, 0, 0], '#468': [1, 0, 0, 0], '#0378': [1, 1, 0, 0], '#013468': [0, 0, 0, 0], '#2345': [0, 0, 0, 0], '#0278': [0, 1, 0, 0], '#013467': [0, 0, 0, 0], '#3578': [1, 0, 0, 0], '#18': [0, 1, 0, 0], '#02567': [1, 0, 0, 0], '#0178': [1, 0, 0, 0], '#02568': [0, 0, 0, 0], '#25678': [0, 0, 0, 0], '#1245678': [0, 0, 0, 0], '#123457': [0, 0, 0, 0], '#123456': [0, 0, 0, 0], '#1256': [1, 0, 0, 0], '#1257': [1, 0, 0, 0], '#2457': [0, 1, 0, 0], '#1258': [0, 0, 0, 0], '#2456': [0, 0, 0, 0], '#23467': [0, 0, 0, 0], '#012345678': [0, 0, 0, 0], '#023478': [0, 0, 0, 0], '#23468': [0, 0, 0, 0], '#023578': [0, 0, 0, 0]}
# The tuple storing the p position. each player don't want to face the p position in his turn
# And p position implies second play probably win the game
pPositionTuple = ([1, 0, 0, 0], [0, 2, 0, 0], [0, 1, 1, 0], [0, 0, 2, 0])
# The name of each board
boardName = ["A", "B", "C"]
# The number list converted into string
stringNumList = [str(i) for i in range(9)]
# The max search depth
searchDepth = 2


class gameState: # gameState class
    def __init__(self): # constructor
        self.deadBoard = [False for i in range(3)] # list to record the dead board
        self.boardState = [[False for j in range(9)] for i in range(3)] # 2-d list to record board states
        self.lastBoard = -1 # index of last alive board, default value is -1

    def setBoardState(self, action): # set board state
        self.boardState[action[0]][action[1]] = True

    def getBoardState(self): # get board state
        return self.boardState

    def setDeadBoard(self, boardIndex): # set dead board
        self.deadBoard[boardIndex] = True

    def getDeadBoard(self): # get dead board
        return self.deadBoard

    def countDeadBoard(self): # count the number of deadboard
        counter = 0
        for i in range(3):
            if self.deadBoard[i]:
                counter += 1
        return counter

    def getLastBoard(self): # get last board
        return self.lastBoard

    def getLegalAction(self): # get all legal actions
        actionList = []
        for i in range(3):
            if not self.deadBoard[i]:
                for j in range(9):
                    if not self.boardState[i][j]:
                        actionList.append((i, j))
        return actionList

    def isLegalAction(self, action): # check whether the action is legal
        if (not self.deadBoard[action[0]]) and (not self.boardState[action[0]][action[1]]):
            return True
        else:
            return False

    def getSuccessorGameState(self, action):
        successorGameState = copy.deepcopy(self)
        successorGameState.setBoardState(action)
        deadBoard = successorGameState.getDeadBoard()
        for i in range(3):
            if not deadBoard[i]:
                if successorGameState.isBoardDead(i):
                    successorGameState.setDeadBoard(i)

        if (successorGameState.countDeadBoard() == 2) and (successorGameState.lastBoard == -1):
            for i in range(3):
                if not deadBoard[i]:
                    successorGameState.lastBoard = i
        return successorGameState

    def evaluation(self, playerIndex): # evaluate the board states. Index 0 is AI, 1 is player
        if self.isGameEnd():
            if playerIndex == 0: # after player moves, the game ends
                return 2
            else: # after AI moves, the game ends
                return -2

        # if the game not ends, only AI will call this part
        stateList = deduce(boardState2DictKey(self))
        if stateList in pPositionTuple:
            return -1
        else:
            return 1

    def isBoardDead(self, boardIndex): # check whether a board is dead
        board = self.boardState[boardIndex]
        for i in range(3):
            if board[i * 3] and board[i * 3 + 1] and board[i * 3 + 2]: # 3 cells in a row are occupied
                return True

        for j in range(3):
            if board[j] and board[j + 3] and board[j + 6]: # 3 cells in a column are occupied
                return True

        if board[0] and board[4] and board[8]: # 3 cells on left diagonal are occupied
            return True

        if board[2] and board[4] and board[6]: # 3 cells on right diagonal are occupied
            return True

        return False

    def isGameEnd(self): # check whether the game ends
        deadBoard = self.getDeadBoard()
        if deadBoard[0] and deadBoard[1] and deadBoard[2]:
            return True
        else:
            return False


def list2String(cellList): # convert the list to string for dict query
    string = "#"
    for i in range(9):
        if cellList[i]:
            string += str(i)
    return string


# def string2List(string): # convert the string to list
#     cellList = [False for i in range(9)]
#     for i in range(1, len(string)):
#         cellList[int(string[i])] = True
#     return cellList


def boardState2DictKey(gameState): # query the dictionary based on gameState
    resultList = [0 for i in range(4)]
    boardState = gameState.getBoardState()
    for board in boardState:
        string = list2String(board)
        cellList = boardDict[string]
        for powIndex in range(4):
          resultList[powIndex] += cellList[powIndex]
    return resultList


def deduce(stateList): # deduce the stateList and return the simplified result. (eg. stateList: [a, b, c, d])
    while True:
        isChanged = False

        # to deduce as fast as possible, single if is used to replace elif
        if stateList[0] >= 2:
            stateList[0] -= 2
            isChanged = True

        if stateList[1] >= 3:
            stateList[1] -= 2
            isChanged = True

        if (stateList[1] >= 2) and (stateList[2] >= 1):
            stateList[1] -= 2
            isChanged = True

        if stateList[2] >= 3:
            stateList[0] += 1
            stateList[2] -= 1
            isChanged = True

        if (stateList[1] >= 2) and (stateList[3] >= 1):
            stateList[1] -= 2
            isChanged = True

        if (stateList[2] >= 1) and (stateList[3] >= 1):
            stateList[0] += 1
            stateList[2] -= 1
            isChanged = True

        if stateList[3] >= 2:
            stateList[2] += 2
            stateList[3] -= 2
            isChanged = True

        if not isChanged:
            break

    return stateList


def getAction(gameState): # get best action based on gameState
    actionList = gameState.getLegalAction()
    valList = []
    indexList = []
    for action in actionList: # execute miniMax
        valList.append(minValue(gameState.getSuccessorGameState(action), 1, searchDepth))
    maxVal = max(valList)

    for i in range(len(valList)):
        if valList[i] == maxVal:
            indexList.append(i)

    return actionList[indexList[random.randint(0, len(indexList) - 1)]]


def maxValue(gameState, depth, maxDepth): # max funtion in miniMax, only AI will call this
    if gameState.isGameEnd() or depth == maxDepth:
        return gameState.evaluation(0)

    value = -float("inf")
    for action in gameState.getLegalAction():
        value = max(value, minValue(gameState.getSuccessorGameState(action), depth, maxDepth))
    return value


def minValue(gameState, depth, maxDepth): # min function in miniMax, only player will call this
    if gameState.isGameEnd():
        return gameState.evaluation(1)

    value = float("inf")
    for action in gameState.getLegalAction():
        value = min(value, maxValue(gameState.getSuccessorGameState(action), depth + 1, maxDepth))
    return value


def printState(gameState): # print the board states
    deadBoard = gameState.getDeadBoard()
    boardState = gameState.getBoardState()
    aliveBoard = []
    for i in range(3):
        if not deadBoard[i]:
            aliveBoard.append(i)

    if (gameState.getLastBoard() != -1) and (len(aliveBoard) == 0):
        aliveBoard.append(gameState.getLastBoard())

    for boardIndex in aliveBoard: # 1st line, name of each board
        print boardName[boardIndex] + ":   \t",
    print

    for boardIndex in aliveBoard: # 2nd line, 1st row of each board
        print printCell(boardState[boardIndex], 0), printCell(boardState[boardIndex], 1), printCell(boardState[boardIndex], 2), "\t",
    print

    for boardIndex in aliveBoard: # 3rd line, 2nd row of each board
        print printCell(boardState[boardIndex], 3), printCell(boardState[boardIndex], 4), printCell(boardState[boardIndex], 5), "\t",
    print

    for boardIndex in aliveBoard: # 4th line, 3rd row of each board
        print printCell(boardState[boardIndex], 6), printCell(boardState[boardIndex], 7), printCell(boardState[boardIndex], 8), "\t",
    print


def printCell(board, cellIndex): # auxiliary function to convert each cell (bool) into number / cross
    if board[cellIndex]:
        return "X"
    else:
        return cellIndex


def printAction(action): # return AI's action
    return boardName[action[0]] + str(action[1])


# main part of this game
game = gameState()
while True:
    try:
        # AI
        action = getAction(game)
        print "AI: " + printAction(action) # AI's action
        game = game.getSuccessorGameState(action) # AI moves
        printState(game) # print present state
        if game.isGameEnd(): # check game ends or not
            print "Game Over. You win the game."
            break

        # player
        while True: # get input from player
            playersMove = raw_input("Your move: ") # player's action
            if len(playersMove) != 2: # validate the length of input
                print "Wrong input, please enter your move again."
                continue

            if (playersMove[0] not in boardName) or (playersMove[1] not in stringNumList):
                print "Wrong input, please enter your move again."
                continue

            playersAction = (boardName.index(playersMove[0]), int(playersMove[1]))
            if game.isLegalAction(playersAction):
                game = game.getSuccessorGameState(playersAction)  # player moves
                break
            else:
                print "Illegal move, please enter your move again."
                continue

        printState(game) # print new state
        if game.isGameEnd(): # check game ends or not
            print "Game Over. You lose the game."
            break

    except KeyboardInterrupt or IOError or EOFError: # deal with exception
        break