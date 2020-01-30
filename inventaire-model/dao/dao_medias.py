

import logging.config
import sqlite3
from  settings import  settings
from models.medias import Media



logging.config.fileConfig(settings.LOGGING_CONF_FILE)
logger = logging.getLogger("logger1")

class MediaDao:

    def __init__(self, file):
        self.__file = "{}/{}".format(settings.BASE_DIR, file)

    def initialiser_base(self):
        try:
            logger.info("initialiser la base de donnees {0}".format(self.__file))
            logger.debug("creer une connexion")
            conn = sqlite3.connect(self.__file)
            logger.debug("creer la tables des medias")
            cursor = conn.cursor()
            requete = "create table medias( id integer, name text)"
            cursor.execute(requete)
            logger.debug("valider la creation")
            conn.commit()
        except Exception as e:
            logger.error(e)
        finally:
            logger.debug("liberer la connexion")
            if cursor is not None :
                cursor.close()
            if conn is not None:
                conn.close()
    def ajouter(self, media):
        try:
            logger.info("ajouter un {0}".format(media))
            logger.debug("creer une connexion")
            conn = sqlite3.connect(self.__file)
            logger.debug("creer la tables des medias")
            cursor = conn.cursor()
            requete = "insert into medias( id, name) values({0},'{1}')".format(
                                                                    media.ident,
                                                                    media.libelle )
            cursor.execute(requete)
            logger.debug("valider la creation")
            conn.commit()
        except Exception as e:
            logger.error(e)
        finally:
            logger.debug("liberer la connexion")
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    def listerMedias(self):
        """"""
        medias = None
        try:
            logger.info("lister les medias")
            logger.debug("creer une connexion")
            conn = sqlite3.connect(self.__file)
            cursor = conn.cursor()
            requete = "select id, name from  medias"
            cursor.execute(requete)
            rows = cursor.fetchall()
            medias = []
            for row in rows :
                media = Media(row[0],row[1])
                medias.append(media)
            logger.debug("valider la creation")
            conn.commit()
        except Exception as e:
            logger.error(e)
        finally:
            logger.debug("liberer la connexion")
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
        return medias
    def listerParId(self, id):
        pass

    def supprimer(self, media_id):
        try:
            logger.info("supprimer un {0}".format(media_id))
            logger.debug("creer une connexion")
            conn = sqlite3.connect(self.__file)
            cursor = conn.cursor()
            requete = "delete from medias where id='{}'".format(media_id)
            cursor.execute(requete)
            logger.debug("valider la suppression")
            conn.commit()
        except Exception as e:
            logger.error(e)
        finally:
            logger.debug("liberer la connexion")
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

