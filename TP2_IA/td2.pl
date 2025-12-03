%% Introduction à l'IA - TD 2
%% Un système expert médical en Prolog
%%
%% Etape 1: Charger ce fichier dans SWI-Prolog
%% 
%% Guide d utilisation des commandes SWI à utiliser dans votre terminal : https://www.swi-prolog.org/pldoc/man?section=cmdline
%% \!\: vous devez produire un exécutable de ce fichier pour pouvoir l utiliser
%%
%% Etape 2 : Exécuter le fichier en effectuant la requête
%% ?- consultation.
%% (répondre avec ";" à un diagnostic pour avoir le suivant.)
%% ?- effacer.
%% pour effectuer une autre consultation si on n'a pas vu tous les diagnostics.

:- dynamic positif/1.
:- dynamic negatif/1.

consultation :- writeln('Bienvenue au service de consultation automatique.'), 
	writeln('Votre nom :'),
	%% Ici, votre nom est sauvegardé dans la variable "Name" qui va etre réutilisé à la fin de la consultation
	readln([Name | _]),
	%% TODO: Le système a besoin des connaissances pour pouvoir fonctionner, à vous de jouer !
	diagnostic(Dis),
	% !, % "ceci si on ne veut qu'un seul diagnostic et ensuite il faut effacer." 
	%% Dans ce scénario, le systeme est capable de déterminer la cause
	write(Name), write(', votre diagnostic est : '), writeln(Dis).

%% Dans ce scénario, le systeme n est pas capable de déterminer la cause
consultation :- writeln('Desole, je n\'arrive pas a faire de diagnostic.'),
	effacer.

%% Le prédicat "symptome" prend en argument "X", nous allons donc appeler ce prédicat en donnant une valeur à X qui sera interpreté
symptome(X) :-
	%% On pose une question à l utilisateur en utilisant "X"
	atomic_list_concat(['Avez-vous', X, '? (oui/non)'], ' ', Q),
	%% La variable Q correspond à la réponse que l'on donne à cette question
	sym_positif(Q, X).

sym_positif(_, X) :- positif(X), !.
sym_positif(Q, X) :- not(negatif(X)),
	interroger(Q, X, R), R = [oui].

interroger(Q, X, R) :- writeln(Q), readln(R), enregistrer(X, R).

enregistrer(X, [oui]) :- asserta(positif(X)).
enregistrer(X, [non]) :- asserta(negatif(X)).

% On fait le ménage:
% la commande "retractall" permet d'effacer tous les renseignements (liste de "oui" et/ou de "non") que nous avons donné au système
effacer :-
	retractall(positif(_)),
	retractall(negatif(_)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% écrire ici la connaissance "experte" permettant de faire des diagnostics
%% sous forme de règles comme celle de cet exemple:


%% Rhume
diagnostic(rhume) :-
    symptome('le nez qui coule'),
    symptome('mal a la gorge'),
    symptome('de la conjonctivite').

diagnostic(rhume) :-  % alternative
    symptome('le nez qui coule'),
    symptome('des eternuements frequents').

%% Grippe
diagnostic(grippe) :-
    symptome('une fievre'),
    symptome('de la fatigue'),
    symptome('la toux seche').

diagnostic(grippe) :-  % alternative
    symptome('des maux de tete'),
    symptome('des frissons'),
    symptome('des courbatures').

%% Allergie
diagnostic(allergie) :-
    symptome('des eternuements frequents'),
    symptome('le nez qui coule'),
    symptome('les yeux rouges et larmoyants').

diagnostic(allergie) :-  % alternative
    symptome('des demangeaisons'),
    symptome('les yeux rouges et larmoyants').

%% Angine
diagnostic(angine) :-
    symptome('mal a la gorge'),
    symptome('une difficulte a avaler'),
    symptome('une fievre legere').

diagnostic(angine) :-  % alternative
    symptome('mal a la gorge'),
    symptome('les ganglions enfles').

%% Gastro-enterite
diagnostic(gastro) :-
    symptome('nausee'),
    symptome('vomissements'),
    symptome('la diarrhee'),
    symptome('des crampes abdominales').

diagnostic(gastro) :-  % alternative
    symptome('la diarrhee'),
    symptome('des douleurs abdominales').

%% Infection urinaire
diagnostic(infection_urinaire) :-
    symptome('des brulures en urinant'),
    symptome('une envie frequente d\'uriner'),
    symptome('des urines troubles ou malodorantes').

diagnostic(infection_urinaire) :-  % alternative
    symptome('une envie frequente d\'uriner'),
    symptome('de la douleur au bas-ventre').

%% Varicelle
diagnostic(varicelle) :-
    symptome('une eruption cutanee rouge'),
    symptome('des demangeaisons'),
    symptome('une fievre legere').

diagnostic(varicelle) :-  % alternative
    symptome('des boutons rouges'),
    symptome('des demangeaisons').

%% COVID-19
diagnostic(covid19) :-
    symptome('de la fievre'),
    symptome('la toux seche'),
    symptome('de la fatigue'),
    symptome('une perte du gout ou de l\'odorat').

diagnostic(covid19) :-  % alternative
    symptome('des maux de tete'),
    symptome('des douleurs musculaires'),
    symptome('la toux'),
    symptome('la fievre legere').

diagnostic(covid19) :-  % alternative pour symptomes plus legers
    symptome('de la fatigue'),
    symptome('un mal de gorge'),
    symptome('un nez qui coule').



