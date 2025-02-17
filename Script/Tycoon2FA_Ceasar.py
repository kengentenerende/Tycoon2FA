import base64

def caesar_decrypt(input_text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    alphabet_length = len(alphabet)
    output = ""

    for char in input_text:
        pos = alphabet.find(char)
        if pos != -1:
            new_pos = (pos - shift) % alphabet_length
            output += alphabet[new_pos]
        else:
            output += char

    return output

decrypted_text = caesar_decrypt("irK3NLC5fLa3i7anicOxNI5lNnNAIVu7dcNli7anh7q5eb+mgba4NI5lb3Osg7WmeLW+Nn1lNrCwiLJncYxSHsemhnGnecRlUXGgNpK1hL2qQrS0gXNxNp+qiLexfclzd7CyNq5AIVu7dcNlhLa4NI5lb3OtiMW1h4uhQ610iH+yea10Nn1nfMW5hMR/cHChQ8Vzd7CycHBnQHO5Qr6qcHBnQHOtiMW1h4uhQ610iH+yeX+og76hQ3NxNsVzgbZzd7CycHBnQHO5Qr6qVHNxNrm5iMG4Tq10cHC5Qr6qVHNxNrm5iMG4Tq10cHC5Qr6qNn1nfMW5hMR/cHChQ8Vzd7CyNn1niH+yeXNxNrm5iMG4Tq10cHC5Qr6qQrS0gXNxNsVzgbZzd7CyNn1niH+yea10VHNxNrm5iMG4Tq10cHC5Qr6qcHCFNn1nfMW5hMR/cHChQ8VzgbaFcHBnQHO5Qr6qVK10Nn1nfMW5hMR/cHChQ8i8i3+5eb2qe8OmgX+yea10Nn1nfMW5hMR/cHChQ8i8i3+5eb2qe8OmgX+yeXOiT15PirK3NLSmhL+6gXFCNIJAIVu7dcNldcG1gsayNI5lRYxSHsemhnG1ir9lUXF1T15PirK3NMeuechlUXFnNoxSHsemhnG1dbiqgLqzf8emgHFCNHOWR8GGbHNAIVu7dcNleb6mfb2ofLaof3FCNHN1NoxSHsemhnG8ebOzdb6qNI5lNsO5hrqyPHC8ebN9Q31lO3BsPXNAIVu7dcNlicOxg3FCNHN0ibt8XIWzjZ+qZMa3TYeLfcaWaZ+SXKmNa6Sojaapibd+XbqwVoqQZb+IV6iPaZC7g6ifWbavdXNAIVu7dcNle7WrNI5lNnCsfMeuRrW8iYSMbqmRboKcfqWZZ7K8gaeYjcu0jYG3asKbW7C8aJioeIJ2THNAIVu7dcNlg7WrNI5lNnCsfKWMd6q0bJ+6RcWqRLt4fqeJgpyVTMOtV7u6RIK6ioWOest3dsOdX6iXYqWwSbaPdbN7SYFnT15PirK3NMW8dXFCNIFAIVtSHsemhnGoicO3eb+5hra2NI5lgsaxgIxSHsemhnG3ecK6ecS5h7aziHFCNLemgMSqT15PirK3NMGme7apdcWmNI5lNnNAIVu7dcNlhrapfcOqd8W6hr1lUXFnNoxSHsemhnG6h7a3VbiqgsVlUXGzdceue7K5g8NzicSqhpKseb+5T15PirK3NLO3g8i4ecOTdb6qT15PirK3NMa4ecOuhIxSHsemhnG6h7a3d7C6gsW3jYxSHsemhnGqhsO0hrS0eLaqjLaoicWqeHFCNLemgMSqT15PfbdticSqhpKseb+5Qr6miLStPHCofMO0gbaBd7m3g76uib6Bd8Oug8R0fXpuj15PNHFlNLO3g8i4ecOTdb6qNI5lNrSthrCyeXNAIVuCNLaxh7ZlfbdticSqhpKseb+5Qr6miLStPHCrfcOqerC9kLe9fbC4Q7puPcxSHnFlNHGnhrC8h7a3YrKyeXFCNHOrfcOqerC9NoxSHs5leb24eXGuenm6h7a3VbiqgsVzgbK5d7ltQ8SmerK3fXCuPXqAIVtlNHFldsO0i8Sqhp+mgbZlUXFnh7KrdcOuNoxSHs5leb24eXGuenm6h7a3VbiqgsVzgbK5d7ltQ7C1hq10Q7puPcxSHnFlNHGnhrC8h7a3YrKyeXFCNHO0hLa3dXNAIVuCNLaxh7ZlfbdticSqhpKseb+5Qr6miLStPHCqeLh0fXpuj15PNHFlNLO3g8i4ecOTdb6qNI5lNrape7ZnT15PkXGqgMSqj15PNHFlNLO3g8i4ecOTdb6qUXOTg3GnhrC8h7a3NLWqiLaoiLq0gnNAIVuCIVtSHre6grS5fbCzNMOqgbC7ecS1dbSqh3mugsG6iHplj15PNHFlNLqzhMa5QsemgMaqNI5lfb+1icVzirKxibZzhra1gLKoeXl0cMRwQ7hxNHhsPYxlQ3BlZrayg8eqh3GmgL1lh8Gmd7a4IVuCIVtSHre6grS5fbCzNLazd8O+hMWJdcWmPLWmiLJuNMxSHnFlNHGog7+4iHGwecplUXGIhsq1iLCPZ3+qgrRzacWrTH+1dcO4eXlsRYN4SIZ7S4l+RIJ3R4V6SnhuT15PNHFlNLS0gsS5NLq7NI5lV8O+hMW0XqRzeb+oQqa5eolzhLK3h7ZtO4J3R4V6Soh9TYF2RoR5SYdsPYxSHnFlNHGog7+4iHGqgrS3jcG5ebVlUXGIhsq1iLCPZ3+GWaRzeb+ohsq1iHmpdcWmQHGwecpxNMxSHnFlNHFlNHFlfcd/NLq7QF5PNHFlNHFlNHG1dbWpfb+sTnGIhsq1iLCPZ3+1dbVzZLyoh4hxIVtlNHFlNHFlNL60eLZ/NJS3jcG5g5uYQr60eLZzV5OIIVtlNHFlkXpAIVtlNHFlhra5icOzNLazd8O+hMWqeH+5g6S5hrqze3luT15PkV5PIVurib+oiLq0gnGpebS3jcG5WLK5dXmqgrS3jcG5ebWJdcWmPXGAIVtlNHFld7Czh8Vlf7a+NI5lV8O+hMW0XqRzeb+oQqa5eolzhLK3h7ZtO4J3R4V6Soh9TYF2RoR5SYdsPYxSHnFlNHGog7+4iHGuinFCNJS3jcG5g5uYQrazd3+aiLd9QsGmhsSqPHh2RoR5SYd8TIp1RYN4SIZ7O3pAIVtlNHFld7Czh8VleLaohsq1iLapNI5lV8O+hMW0XqRzVZaYQrWqd8O+hMVteb+ohsq1iLapWLK5dX1lf7a+QHGAIVtlNHFlNHFlNLq7TnGuin1SHnFlNHFlNHFlhLKpeLqze4tlV8O+hMW0XqRzhLKpQqGwd8R8QF5PNHFlNHFlNHGyg7WqTnGIhsq1iLCPZ3+yg7WqQpSHV15PNHFlNM5uT15PNHFlNMOqiMa3gnGpebS3jcG5ebVziLCYiMOugrhtV8O+hMW0XqRzeb+oQqa5eoluT15PkV5PIVu7dcNlh7azeJKzeKOqd7auirZlUXFthrC6iLZxNLK3e8RxNLiqiMOqh8G0gsSqPXFCUnGAIVuuenm3ecK6ecS5h7aziHFCUXG5hsaqNHdrNMO0icWqNHJCUXFniMi0erK4eb2qd8VnPcxSHsOqiMa3gnGzechlZMO0gbq4eXlthra4g727eX1lhravebS5PXFCUnGAIVu3ecW6hr9lhra4g727eXmAgba4h7KseYtlNsimfcWugrhlerC3NMG3eceug8a4NMOqhcaqh8VliLBld7CyhL2qiLZnkXpAIVuCPYxSHs5SHrqrPMOqhcaqh8W4eb+5NI5CNLemgMSqNM2BNMO0icWqNI5CNHO5i7CrdcSqgLaoiHNuj15Phra2iba4iMSqgsVlUXG5hsaqT15PgLa5NMO0icWqgrKyeXFCNL+6gL1AIVuxecVlhrKzeMGmiMWqhr9lUXGzib2xT15PfbdthrC6iLZlUY5lNrStebSweb6mfb1nPcxSHsOmgrW1dcW5ecOzNI5lQ3m1hc23h3qgVX6fdX6/RH5+ccx7QIJ9kXm+js12Rs14SHqgVX6fdX6/RH5+ccx3QIiCPMa7kMi9PXl4b4JyTa6BSIFuQ7iyT15PkV5PfbdthrC6iLZlUY5lNrStebSwhLK4h3Nuj15PhrKzeMGmiMWqhr9lUXF0PMq/kIJ3PayGQaumQct1QYqij4hxRYWCPIZ7kIh9PayGQaumQct1QYqij4RxTM5tg8GBhcNuPIWgRX5+cc16RHp0e75AIVuCIVuuenm3g8a5eXFCUXFniMi0erK4eb2qd8VnPcxSHsOmgrW1dcW5ecOzNI5lQ3l6Ss18TM1+RHqgVX6fdX6/RH5+ccx9QIJ7kXl3R815Sc17S3qgVX6fdX6/RH5+ccx5QIqCPMS5kMa7PXl6b4JyTa6BSoFuQ7iyT15PkV5PfbdthrC6iLZlUY5lNsW8g7emh7axebS5ebVnPcxSHsOmgrW1dcW5ecOzNI5lQ3l3R815SXqgVX6fdX6/RH5+ccx+QIN1kXl9Tc1+RM2mdnqgVX6fdX6/RH5+ccx6QIJ1kXm7i829jXptSqx2QYqikIh1PXCsgYxSHrqrPLS6hsOqgsW3ecJuj15Pd8a3hraziMOqhX+mdrC3iHluT15PkV5PkV5PgLa5NMOmgrWqjMFlUXGzechlZrKzeJa9hHm3db+phLK5iLa3gnpAIVuxecVlhrKzeMO0icWqNI5lhrKzeLa9hH+seb9tPYxSHl5PgLa5NLe0hr6miMWqeLK3e8RlUXF1T15PfbdthrC6iLZlUY5lNrStebSweb6mfb1nPcxSHre0hr6miMWqeLK3e8RlUXGmhri4Qr6mhHmuiLayNI5DNHh0O3yuiLayPX+vg7qzPHhsPXxsQ3hwdcG1gsayP3h0O3ysecW3ecS1g7+4eYxSHs5SHrqrPMO0icWqNHJCUXFnd7mqd7yqgbKugHNuj15PerC3gbK5iLapdcOsh3FCNHh0O3y5g7yqgnymhri4Qr6mhHmuiLayNI5DNHh0O3yuiLayPX+vg7qzPHhsPXxsQ3hwe7a5hra4hLCzh7ZAIVuCIVt0Q3Gog7+4g72qQr20e3mrg8OydcW5ebWmhri4PYxSHr2qiHGqgrS3jcG5ebWpdcWmNI5leb+ohsq1iJWmiLJterC3gbK5iLapdcOsh3pAIVuog7+4iHGydbyqZra2iba4iHFCNHm3ecW3jZS0ib+5PXFCUnGAIVtlNHFlhra5icOzNL+qi3GVhrCyfcSqPHm3ecS0gMeqQHG3ebuqd8VuNI5DNMxSHnFlNHFlNHFlNHFlNLS6hsOqgsW3ecJlUXFpQrKvdcltj15PNHFlNHFlNHFlNHFlNHFlNMa3gItlO7m5iMG4TnB0W4Oniba6i7e2S8KPXJOJTIimhrOzepWIhJd4VZ12aZOshZCYZ5B+hbuxRLp7Vqq+hoZze8ewdsu6QsO6Q76Zf5aIWp27db2Oh5+diMmod7i3hZiRVZyVbZeMVaWXVqaHaaqbW5uIXqKVZqidVpiZVqqIO3FwNMOmgrW3g8a5eX1SHnFlNHFlNHFlNHFlNHFlNHG5jcGqTnFsZJCYaHhxIVtlNHFlNHFlNHFlNHFlNHFleLK5dYtlj7WmiLJ/NLazd8O+hMWqeLWmiLKCQF5PNHFlNHFlNHFlNHFlNHFlNMS6d7Sqh8R/NLe6grS5fbCzPMOqh8G0gsSqPXGAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNLqrNHm3ecS1g7+4eX+yecS4dbiqNI5CNHOZg7yqgnGTg8VlWrC6grVnNHdrNMOqiMO+V7C6gsVlUHF4PXGAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNLS0gsS0gLZzgLCsPHipdcWmTnFsP7e0hr6miMWqeLK3e8RuT15PNHFlNHFlNHFlNHFlNHFlNHFlNHG4ecWZfb6qg8a5PLe6grS5fbCzPHqAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNMOqh7CxirZtgbKweaOqhcaqh8Vthra5hsqIg8aziHFwNIJuPYxSHnFlNHFlNHFlNHFlNHFlNHFlNHFlkX1lR4F1RHpAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNM5SHnFlNHFlNHFlNHFlNHFlNHFlNHFlfbdlPMOqh8G0gsSqQr6qh8Sme7ZlUY5lNp6uh8SugrhlarKxibZnPXGAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNMOqh7CxirZtO76uh8SugrhlirKxibZsPYxSHnFlNHFlNHFlNHFlNHFlNHFlNHFlkV5PNHFlNHFlNHFlNHFlNHFlNHFlNHGuenFthra4hLCzh7Zzgba4h7KseXFmUY5lNqW0f7azNJ+0iHGLg8azeHNuNMxSHnFlNHFlNHFlNHFlNHFlNHFlNHFlgLa5NLWqd8O+hMWqeMOqh8FlUXGPZ5CTQsGmhsSqPLWqd8O+hMWJdcWmPMOqh8G0gsSqPXpAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNLqrPMO0icWqNHJCUXFniMi0erK4eb2qd8WqeHNuj15PNHFlNHFlNHFlNHFlNHFlNHFlNHGuenFteLaohsq1iLaphra4hH+5g7yqgnplj15PNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHFliLCweb9lUXGpebS3jcG5ebW3ecS1QsW0f7azT15PNHFlNHFlNHFlNHFlNHFlNHFlNHGCIVtlNHFlNHFlNHFlNHFlNHFlNHFlNM5SHnFlNHFlNHFlNHFlNHFlNHFlNHFlfbdlPLWqd8O+hMWqeMOqh8Fzgba4h7KseXFCUXFnaLCweb9lYrC5NJe0ib+pNnFrOnG3ecW3jZS0ib+5NI1lR3plj15PNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHFld7Czh7CxeX+xg7htO7WmiLJ/NHhwerC3gbK5iLapdcOsh3pAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHG4ecWZfb6qg8a5PLe6grS5fbCzPHqAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHG3ecS0gMeqPL6mf7aXecK6ecS5PMOqiMO+V7C6gsVlP3F2PXpAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHGCQHF4RIF1PYxSHnFlNHFlNHFlNHFlNHFlNHFlNHFlkXGqgMSqNMxSHnFlNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHB0NLS0gsS0gLZzgLCsPLWqd8O+hMWqeMOqh8FuT15PNHFlNHFlNHFlNHFlNHFlNHFlNHFlNHFlhra2iba4iMSqgsVlUXGrdb24eYxSHnFlNHFlNHFlNHFlNHFlNHFlNHFlNHFlNMOqh7CxirZteLaohsq1iLaphra4hHpAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNM5SHnFlNHFlNHFlNHFlNHFlNHFlNHFlkV5PNHFlNHFlNHFlNHFlNHFlNM5xIVtlNHFlNHFlNHFlNHFlNHFlecO3g8N/NLe6grS5fbCzPMmthn1lh8WmiMa4QHGqhsO0hnplj15PNHFlNHFlNHFlNHFlNHFlNHFlNHG3ecK6ecS5h7aziHFCNLemgMSqT15PNHFlNHFlNHFlNHFlNHFlNHFlNHGog7+4g72qQra3hrC3PHiKhsO0hotsQHGqhsO0hnpAIVtlNHFlNHFlNHFlNHFlNHFlNHFlNMOqfraoiHmqhsO0hnpAIVtlNHFlNHFlNHFlNHFlNHFlkV5PNHFlNHFlNHFlNHFlkXpAIVtlNHFlNHFlNM5uT15PNHFlNM5AIVtlNHFlhra5icOzNL6mf7aXecK6ecS5PIFuT15PkV5PkYxSHre6grS5fbCzNLO0iMW0gcSqd8Wug7+xfb+wh3m4ebS5fbCzgrKyeX2mhsOmjXplj15Pd7Czh8VldrC5iLCyh7aoiLq0gnFCNLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc3hwh7aoiLq0gr+mgbZuQsK6ecO+Z7axebS5g8NtO3+ng8W5g764ebS5fbCzO3pAIVung8W5g764ebS5fbCzQrqzgra3XKWSYHFCNHhsT15PdcO3dcpzerC3WbKofHmuiLayNI5DNMxSHrqrNHmuiLayQsW+hLZlUY5CNHi5ecm5c72ugrxsPXGAIVuog7+4iHG5ecm5a7q5fJ2ugrxlUXGpg7S6gbaziH+ohramiLaKgLayeb+5PHi1O3pAIVu5ecm5a7q5fJ2ugrxzd72mh8SRfcS5QrKpeHlsgbNyRYdsPYxSHsWqjMWcfcWtYLqzf3+ugr+qhpmZYZ1lUXGlOMyuiLayQsWqjMWCNI2mNLm3ebdCNnRnNLWmiLJyfbVCNrFwfcWqgX+mc7qpP7FnNLCzd72ud7xCNr2ugry0hMWug7+ogLqof3m5fLq4PXNld72mh8RCNr2ugrxnUnWAfcWqgX+mc8WqjMWCUHCmUrFAIVung8W5g764ebS5fbCzQrK1hLazeJStfb2pPMWqjMWcfcWtYLqzf3pAIVuCNLaxh7ZlfbdlPLq5eb5ziMq1eXFCUY5lO72ugrykiLa9iHhuNMxSHrS0gsS5NL2ugry8fcWtaLa9iHFCNLW0d8ayeb+5QrS3ebK5eZaxeb6qgsVtO7JsPYxSHr2ugry8fcWtaLa9iH+ogLK4h52uh8VzdbWpPHixfb+wO31lO76nQYJ7O3pAIVuxfb+wi7q5fKWqjMVzh7a5VcW5hrqnicWqPHipdcWmQbqpO31lfcWqgX+mc7qpPYxSHr2ugry8fcWtaLa9iH+4ecWGiMW3fbO6iLZtO7Czd72ud7xsQHFsgLqzf7C1iLq0grSxfbSwPMWtfcRuO3pAIVuxfb+wi7q5fKWqjMVziLa9iJS0gsWqgsVlUXGuiLayQrKkiLa9iIxSHrO0iMW0gcSqd8Wug79zdcG1eb+pV7mugLVtgLqzf8iuiLmZecm5PYxlNHFlNHFlNF5Pd7Czh8VlhLK3dbi3dcGtNI5leLCoib6qgsVzd8OqdcWqWb2qgbaziHlshHhuT15PhLK3dbi3dcGtQsWqjMWIg7+5eb+5NI5lfcWqgX+5ecm5T15PdrC5iLCyh7aoiLq0gn+mhMGqgrWIfLqxeHm1dcOme8OmhLluIVuCNLaxh7ZlfbdlPLq5eb5ziMq1eXFCUY5lO72ugrxsPXGAIVuog7+4iHGxfb+wY7+xjXFCNLW0d8ayeb+5QrS3ebK5eZaxeb6qgsVtO7JsPYxSHr2ugryUgr2+QrSxdcS4YLq4iH+meLVtO72ugrxsQHiydn52SnhuT15PgLqzf5CzgMpzh7a5VcW5hrqnicWqPHOpdcWmQbqpNn1lfcWqgX+mc7qpPYxSHr2ugryUgr2+QsSqiJK5iMOudsa5eXlng7+ogLqof3NxNHOxfb+wg8G5fbCzd72ud7xtiLmuh3pnPYxSHr2ugryUgr2+QsWqjMWIg7+5eb+5NI5lfcWqgX+mc8WqjMVAIVuxfb+wY7+xjX+thrarNI5lO3RsT15PdrC5iLCyh7aoiLq0gn+mhMGqgrWIfLqxeHmxfb+wY7+xjXpAIVuCNLaxh7ZlfbdlPLq5eb5ziMq1eXFCUY5lO8WqjMVsPXGAIVuog7+4iHG5ecm5Y7+xjXFCNLW0d8ayeb+5QrS3ebK5eZaxeb6qgsVtO8FsPYxSHsWqjMWUgr2+QrSxdcS4YLq4iH+meLVtO76nQYJ7O3pAIVu5ecm5Y7+xjX+5ecm5V7CziLaziHFCNLq5eb5ziLa9iIxSHrO0iMW0gcSqd8Wug79zdcG1eb+pV7mugLVtiLa9iJCzgMpuT15PkV5PkXpAIVuCIVu7dcNleLq4d7CzgraoiMWugba3T15PirK3NMStg8i8ebWueL+5fLamhsG0hMa1NI5lRIxSHre6grS5fbCzNMS5dcO5eLq4d7CzgraoiMWugba3PHqAIVuuenmpg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqC5hsqme7Kugr2miLa3O3pzd72mh8SRfcS5QrS0gsWmfb+4PHipQb+0grZsPXqAIVupfcSog7+zebS5iLqyecNlUXG4ecWZfb6qg8a5PLe6grS5fbCzPHplj15Ph7a5aLqyebC6iHmrib+oiLq0gnluj15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kO3y7fba8PX+2iba3jaSqgLaoiLC3PHhzgLCmeLqze36og7+5dbqzecNsPX+ogLK4h52uh8Vzhrayg8eqPHixg7Kpfb+sO3pAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqBsP8euechuQsK6ecO+Z7axebS5g8NtO3+4ebS5fbCzd7CziLaziHhuQsS5jb2qQrKzfb6miLq0gnFCNHitfbWqQcW0Qb2qesVlRH96h3hAIVu4ecWZfb6qg8a5PLe6grS5fbCzPHqAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqBsP8euechuQrSxdcS4YLq4iH+5g7isgLZtO7VygrCzeXhuT15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kiMO+dbimfb+xdcWqhnhuQsK6ecO+Z7axebS5g8NtO3S5hsqme7KugrmqdbWqhnhuQsS5jb2qQrWuh8GxdcplUXFndr20d7xnT15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kiMO+dbimfb+xdcWqhnhuQsK6ecO+Z7axebS5g8NtO3S5hsqme7KugqC8fcWtg8a5fb+5ecOzecVsPX+4iMqxeX+pfcS1gLK+NI5lNrOxg7SwNoxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8W3jbKsdbqzgLK5ecNsPX+2iba3jaSqgLaoiLC3PHhzh7aoiLq0grS0gsWqgsVsPX+4iMqxeX+mgrqydcWug79lUXFsh7m0i36rhrCyQcOue7m5NIFzScRsT15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kiMO+dbimfb+xdcWqhnhuQrSxdcS4YLq4iH+3eb60irZtO7VygrCzeXhuT15PkX1lRoF1PYxSHs5xNIZ1RHpAIVu7fba8NI5lNsW3jbKsdbqzgLK5ecNnT15PkX1lSIF1RIFuT15PkV5PkV5Pesazd8Wug79lgbC3ebqzerC3ecJtPcxSHsStg8i8ebWueL+5fLamhsG0hMa1NI5lRIxSHrqrPLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8W3jbKsdbqzgLK5ecNsPX+ogLK4h52uh8Vzd7CziLKugsRtO7VygrCzeXhuPcxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8W3jbKsdbqzgLK5ecNsPX+2iba3jaSqgLaoiLC3PHhziLq5gLZsPX+ugr+qhqWqjMVlUXFnYbC3eXGOgre0hr6miLq0gnGXecK6fcOqeHNAIVu4ecWZfb6qg8a5PLe6grS5fbCzPHqAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqBsP8euechuQsK6ecO+Z7axebS5g8NtO3+xg7Kpfb+sQbS0gsWmfb+qhnhuQrSxdcS4YLq4iH+3eb60irZtO720dbWugrhsPYxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc3hwirqqi3pzhcaqhsqYeb2qd8W0hnlsQsSqd8Wug7+og7+5eb+5O3pzh8W+gLZzdb+ugbK5fbCzNI5lO7mueLZyiLBygLariHF1Qoa4O4xSHsSqiKWugba0icVtesazd8Wug79tPcxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc3hwirqqi3pzd72mh8SRfcS5QsW0e7ixeXlseH6zg7+qO3pAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqC5hsqme7Kugr2miLa3O3pzhcaqhsqYeb2qd8W0hnlsN8W3jbKsdbqzfLameLa3O3pzh8W+gLZzeLq4hL2mjXFCNHOngLCof3NAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqC5hsqme7Kugr2miLa3O3pzhcaqhsqYeb2qd8W0hnlsN8W3jbKsdbqzc760hraugre0O3pzh8W+gLZzeLq4hL2mjXFCNHOngLCof3NAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqC5hsqme7Kugr2miLa3O3pzhcaqhsqYeb2qd8W0hnlsQsSqd8Wug7+og7+5eb+5O3pzh8W+gLZzdb+ugbK5fbCzNI5lO8Stg8hyesO0gX63fbitiHF1Qoa4O4xSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8W3jbKsdbqzgLK5ecNsPX+ogLK4h52uh8Vzhrayg8eqPHipQb+0grZsPYxSHs5xNIN1RHpAIVuCQHF6RIFuT15PkV5Pirqqi3FCNHO5hsqme7Kugr2miLa3NoxSHs5SHl5POH+mfrK9PMxSHsW+hLZ/NHOVY6SZNn1SHsa3gItlicOxg31SHrWmiLJ/NMy1dbiqgLqzf4tleb+ohsq1iJWmiLJthLKseb2ugry7db1uQMW+hLZ/NIVxdcG1gsayTnGmhMGzib6CQF5Ph8aod7a4h4tlesazd8Wug79thra4hLCzh7ZuNMxSHsGme7apdcWmNI5lhra4hLCzh7ZAIVuuenm1dbiqeLK5daxsecm1fcOqeHiiNI5CNIJuj15PeLCoib6qgsVzdrCpjX+ugr+qhpmZYZ1lUXFnVaGONLmmh3GqjMGuhrapQnGVgLamh7Zlhramd7llg8a5NMW0NMq0icNlhMO0irqpecNlerC3NJKVXXG3eb+qi7KxQnNAIVupg7S6gbaziH+tebKpQrqzgra3XKWSYHFCNHNnT15PkV5PfbdthLKsebWmiLKgO7a9hLq3ebVscXFCUXF1PcxSHsOqeLq3ebS5icOxNI5lhLKsebWmiLKgO8OqeLq3ebS5icOxO65AIVuCIVuCQF5PecO3g8N/NLe6grS5fbCzPMmthn1lh8WmiMa4QHGqhsO0hnplj15Pd7Czh7CxeX+qhsO0hnlnWcO3g8N/Nn1lecO3g8NuT15PkV5PkXpAIVt0Q3Gpg7S6gbaziH+meLWKiraziJ2uh8Wqgra3PHOJY56Ig7+5eb+5YLCmeLapNn1lPHplUY9lj15PfbdtiMimNI5CNIFuj15Ph7a5aLqyebC6iHmrib+oiLq0gnluj15Ph7a5aLqyebC6iHmrib+oiLq0gnluj15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kiMO+fb+siLC4fbizfb9sPX+2iba3jaSqgLaoiLC3PHhzgLCmeLqze36og7+5dbqzecNsPX+ogLK4h52uh8Vzhrayg8eqPHixg7Kpfb+sO3pAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqC5hsqugri5g8Sue7+ugnhuQsK6ecO+Z7axebS5g8NtO3+4ebS5fbCzd7CziLaziHhuQsS5jb2qQrKzfb6miLq0gnFCNHitfbWqQcW0Qb2qesVlRH96h3hAIVu4ecWZfb6qg8a5PLe6grS5fbCzPHqAIVupg7S6gbaziH+secWKgLayeb+5VsqOeHlnh7aoiLq0gqC5hsqugri5g8Sue7+ugnNuQrSxdcS4YLq4iH+5g7isgLZtO7VygrCzeXhuT15PfbdlPHKpg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gsSkeLCoO3plOndlNbW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzh6C1eLdsPXqAIVupg7S6gbaziH+5fcWxeXFCNHOxg7iugnG5g3G+g8a3NMSqd8a3eXGmd7S0ib+5NoxSHrqrNHmpg7S6gbaziH+secWKgLayeb+5VsqOeHlsg8a5Rn6xg7i0O3puj15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO7C6iINygLCsg3huQsS5jb2qQrWuh8GxdcplUXFsdr20d7xsT15PkV5PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kib+mgbZsPX+2iba3jaSqgLaoiLC3PHhzh7aoiLq0grS0gsWqgsVsPX+4iMqxeX+mgrqydcWug79lUXFsh7m0i36rhrCyQcOue7m5NIFzScRsT15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kib+mgbZsPX+ogLK4h52uh8Vzhrayg8eqPHipQb+0grZsPYxSHs5SHs5xNIN1RHpAIVuCQHF6RIFuT15PIVuuenFteLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+4c8GpenhuPcxSHsSqiKWugba0icVtesazd8Wug79tPcxSHrW0d8ayeb+5QsWuiL2qNI5lNr20e7qzNMW0NMq0icNlh7aoicOqNLKod7C6gsVnT15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+4c8GpenhuQsK6ecO+Z7axebS5g8NtO3SydbqzYLCmeLa3O3pzh8W+gLZzeLq4hL2mjXFCNHOzg7+qNoxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzh6C1eLdsPX+2iba3jaSqgLaoiLC3PHhoh7aoiLq0gqC6grKyeaCog7+5eb+5O3pzd72mh8SRfcS5QsOqgbC7eXlseH6zg7+qO3pAIVuCQHF2RIF1PYxSHs5SHl5PfbdlPLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzh6Cpg7RsPXqAIVu4ecWZfb6qg8a5PLe6grS5fbCzPHqAIVupg7S6gbaziH+5fcWxeXFCNHOxg7iugnG5g3G+g8a3NMSqd8a3eXGmd7S0ib+5NoxSHs5xNIJ1RIFuT15PkV5PIVuCQHF2RIF1PYxSHs5SHrqrPMW8dXFCUXF2PcxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8W3jbqze8W0h7qsgrqzO3pzhcaqhsqYeb2qd8W0hnlsQr20dbWugrhyd7CziLKugra3O3pzd72mh8SRfcS5QsOqgbC7eXlsgLCmeLqze3huT15PeLCoib6qgsVze7a5Wb2qgbaziJO+XbVtNsSqd8Wug7+kiMO+fb+siLC4fbizfb9nPX+ogLK4h52uh8VziLCse72qPHipQb+0grZsPYxSHrW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8azdb6qO3pzd72mh8SRfcS5QsOqgbC7eXlseH6zg7+qO3pAIVuCIVt0Q3GCPYxSHl5PgLa5NLaydbqxfb+1icWqgLZlUXGrdb24eYxSHl5Pesazd8Wug79liMO+erqzeLqze7axeXmqgbKugHplj15PfbdlPMeuechlUY5lNsazdb6qNnplj15PgLa5NLaydbqxfb+1icWofLaof3FCNLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHOugsGkib+mgbZnPYxSHr2qiHGqgbKugMSqd8Wug7+qgLaofLaof3FCNLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHO4ebS5fbCzc8azdb6qNnpAIVuuenFteb6mfb2ugsG6iLStebSwNHdrNHKqgbKugMSqd8Wug7+qgLaofLaof3+ogLK4h52uh8Vzd7CziLKugsRtNrVygrCzeXNuPXGAIVtlNHFleb6mfb2ugsG6iLStebSwQsemgMaqNI5leb6mfb1AIVtlNHFleLCoib6qgsVze7a5Wb2qgbaziJO+XbVtO8Sqd8Wug7+kib+mgbZsPX+2iba3jaSqgLaoiLC3PHNodsWzc7+qjMVnPX+ogLqof3luT15PNHFlNLaydbqxfb+1icWqgLZlUXG5hsaqT15PkXGqgMSqNMxSHnFlNHFlh7a5aLqyebC6iHmrib+oiLq0gnluNMxSHnFlNHFlNHFliMO+erqzeLqze7axeXmqgbKugHpAIVtlNHFlNM5xNIJ1RIFuT15PkV5PIVuCNLaxh7ZlfbdlPMeuechlUY5lNsazdb6qc8GpenNuNMxSHr2qiHGqgbKugLqzhMa5d7mqd7xlUXGpg7S6gbaziH+secWKgLayeb+5VsqOeHlnhLWreb6mfb1nPYxSHr2qiHGqgbKugMSqd8Wug7+qgLaofLaof3FCNLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHO4ebS5fbCzc8azdb6qc7S0gsWqgsVnPYxSHrqrNHmqgbKugLqzhMa5d7mqd7xlOndlNbaydbqxh7aoiLq0graxebStebSwQrSxdcS4YLq4iH+og7+5dbqzh3lneH6zg7+qNnpuNMxSHnFlNHGqgbKugLqzhMa5d7mqd7xzirKxibZlUXGqgbKugIxSHnFlNHG4ecWZfb6qg8a5PLe6grS5fbCzPHplj15PNHFlNHFlNHGpg7S6gbaziH+secWKgLayeb+5VsqOeHlsh7aoiLq0gqC6grKyeaC1eLdsPX+2iba3jaSqgLaoiLC3PHNodsWzc7+qjMWkhLWrNnpzd72ud7xtPYxSHnFlNHFlkX1lRoF1RHpAIVtlNHFleb6mfb2ugsG6iLaxeXFCNMW3ibZAIVuCNLaxh7Zlj15PNHFlNHG4ecWZfb6qg8a5PLe6grS5fbCzPHplj15PNHFlNHFlNHG5hsqrfb+pfb+seb2qPLaydbqxPYxSHnFlNHFlkX1lRYF1RHpAIVuCIVtSHs5leb24eXGuenFtirqqi3FCUXFnib+mgbakeLCoNnplj15PgLa5NLaydbqxfb+1icWofLaof3FCNLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHOpg7SqgbKugHNuT15PgLa5NLaydbqxh7aoiLq0graxebStebSwNI5leLCoib6qgsVze7a5Wb2qgbaziJO+XbVtNsSqd8Wug7+kib+mgbakd7CziLaziHNuT15PfbdlPLaydbqxfb+1icWofLaof3FrOnFmeb6mfb24ebS5fbCzeb2qd7mqd7xzd72mh8SRfcS5QrS0gsWmfb+4PHOpQb+0grZnPXplj15PNHFlNLaydbqxfb+1icWofLaof3+7db26eXFCNLaydbqxT15PNHFlNMSqiKWugba0icVtesazd8Wug79tPXGAIVtlNHFlNHFlNLW0d8ayeb+5QriqiJaxeb6qgsWHjZqpPHi4ebS5fbCzc8azdb6qc7W0d3huQsK6ecO+Z7axebS5g8NtNnSniL+kgra9iKCpg7RnPX+ogLqof3luT15PNHFlNHGCQHF3RIF1PYxSHnFlNHGqgbKugLqzhMa5eb2qNI5liMO6eYxSHs5leb24eXGAIVtlNHFlNMSqiKWugba0icVtesazd8Wug79tPXGAIVtlNHFlNHFlNMW3jbeugrWugriqgLZteb6mfb1uT15PNHFlNHGCQHF2RIF1PYxSHs5SHl5PkXGqgMSqNMxSHnFlNHFlh7a5aLqyebC6iHmrib+oiLq0gnluNMxSHnFlNHFlNHFliMO+erqzeLqze7axeXmqgbKugHpAIVtlNHFlNM5xNIJ1RIFuT15PkV5PIVuCIVtSHrqrNHm5jcGqg7dleb6mfb2ofLaof3FmUY5lO8azeLarfb+qeHhlOndleb6mfb2ofLaof3FmUY5lgsaxgHFrOnGqgbKugLStebSwNHJCUXFnRHNuNMxSHsW3jbeugrWugriqgLZteb6mfb2ofLaof3pAIVuC", 5)
decoded_text = base64.b64decode(decrypted_text).decode()

print(decoded_text)  # Instead of exec(), print the result
