import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.metrics import (accuracy_score,classification_report,confusion_matrix,roc_auc_score)
from src.classification.train_test import (train_arbre_aleatoire,train_GBM,train_HGBC)


def evaluer_modele(modele, nom_modele, x_train, y_train, x_test, y_test):
    """Évalue un modèle de classification et affiche l'importance des variables."""
    print(f"\n{'=' * 50}")
    print(f"ÉVALUATION : {nom_modele}")
    print(f"{'=' * 50}")

    # 1. Prédictions et probabilités
    y_pred_train = modele.predict(x_train)
    y_pred_test = modele.predict(x_test)
    y_proba_test = modele.predict_proba(x_test)[:, 1]

    # 2. Calcul des métriques
    acc_train = accuracy_score(y_train, y_pred_train) * 100
    acc_test = accuracy_score(y_test, y_pred_test) * 100
    auc_test = roc_auc_score(y_test, y_proba_test)

    print(f"Bien classés (Train) : {acc_train:.3f} %")
    print(f"Bien classés (Test)  : {acc_test:.3f} %")
    print(f"Score ROC-AUC (Test) : {auc_test:.3f}")

    # 3. Matrice de confusion et rapport détaillé
    print("\nMatrice de confusion :")
    print(confusion_matrix(y_test, y_pred_test))

    print("\nRapport de classification :")
    print(classification_report(y_test, y_pred_test))

    # 4. Importance des variables (compatible RF, GBM et HGBC)
    if hasattr(modele, "feature_importances_"):
        scores_imp = modele.feature_importances_
    else:
        perm = permutation_importance(
            modele, x_test, y_test, n_repeats=5, random_state=42, n_jobs=-1
        )
        scores_imp = perm.importances_mean

    importances = pd.DataFrame(
        scores_imp, index=x_train.columns, columns=["importance"]
    ).sort_values("importance", ascending=False)

    print("Top 10 des variables les plus importantes :")
    print(importances.head(10))

modele_rf =  train_arbre_aleatoire()
modele_gbm = train_GBM()    
modele_hgbc = train_HGBC()

evaluer_modele(modele_rf, "Random Forest", x_train, y_train, x_test, y_test)
evaluer_modele(modele_gbm, "Gradient Boosting", x_train, y_train, x_test, y_test)
evaluer_modele(modele_hgbc, "Hist Gradient Boosting", x_train, y_train, x_test, y_test)