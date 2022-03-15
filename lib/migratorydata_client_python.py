import abc
class PyJ(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GqZ(self, host):
        pass
    @abc.abstractmethod
    def Skw(self, jiT):
        pass
    @abc.abstractmethod
    def HLn(self, host, encrypted):
        pass
import threading
class Fwq:
    def __init__(self, value):
        self._lock = threading.Lock()
        self._value = value
    def URV(self, value):
        with self._lock:
            self._value = value
    def lBf(self):
        with self._lock:
            return self._value
    def __repr__(self) -> str:
        return str(self._value)
class mJo:
    def __init__(self, _start, _end):
        self._start = _start
        self._end = _end
    def pIu(self):
        return self._start
    def ufj(self):
        return self._end
import abc
class MigratoryDataListener(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def on_message(self, message):
        pass
    @abc.abstractmethod
    def on_status(self, status, info):
        pass
class MigratoryDataLogLevel:
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
import abc
class MigratoryDataLogListener(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def on_log(self, log, migratory_data_log_level):
        pass
class QoS:
    STANDARD = 0
    GUARANTEED = 1
class MessageType:
    SNAPSHOT = 0
    UPDATE = 1
    RECOVERED = 2
    HISTORICAL = 3
class MigratoryDataMessage:
    def __init__(self, _subject, _content, closure=None, qos=QoS.GUARANTEED, retained=True, reply_subject=None):
        self._subject = _subject
        self._content = _content
        self._closure = closure
        self._reply_to_subject = reply_subject
        self.VXt = qos
        self._retained = retained
        self._message_type = MessageType.UPDATE
        self._seq = None
        self._epoch = None
        self._compression = None
    def get_subject(self):
        return self._subject
    def get_content(self):
        return self._content
    def get_closure(self):
        return self._closure
    def get_reply_to_subject(self):
        return self._reply_to_subject
    def is_retained(self):
        return self._retained
    def get_seq(self):
        return self._seq
    def get_epoch(self):
        return self._epoch
    def get_qos(self):
        return self.VXt
    def get_message_type(self):
        return self._message_type
    def set_compressed(self, compression_bool):
        self._compression = compression_bool
    def is_compressed(self):
        return self._compression
    def __repr__(self) -> str:
        iFd = "["
        iFd += "Subj = " + str(self._subject) + ", "
        iFd += "Content =  " + str(self._content.decode("utf-8")) + ", "
        iFd += "Closure =  " + str(self._closure) + ", "
        iFd += "ReplyToSubject =  " + str(self._reply_to_subject) + ", "
        iFd += "Retained = " + str(self._retained) + ", "
        iFd += "QOS = " + self.vtq() + ", "
        iFd += "MessageType = " + self.mEJ() + ", "
        iFd += "Seq = " + str(self._seq) + ", "
        iFd += "Epoch = " + str(self._epoch) + " "
        iFd += "Compression = " + str(self._compression) + " "
        iFd += "]"
        return iFd
    def vtq(self):
        if self.VXt == QoS.STANDARD:
            return "STANDARD"
        return "GUARANTEED"
    def mEJ(self):
        if self._message_type == MessageType.SNAPSHOT:
            return "SNAPSHOT"
        if self._message_type == MessageType.UPDATE:
            return "UPDATE"
        if self._message_type == MessageType.RECOVERED:
            return "RECOVERED"
        return "HISTORICAL"
class obv:
    def __init__(self):
        self.YoI = bytearray()
        self.Kif = 0
        self.content_length_mark = -1
        self.payload_mark = -1
        self.body_start_mark = -1
        self.body_end_mark = -1
    def yTC(self, Kif):
        self.Kif = Kif
    def extend(self, glt):
        self.YoI.extend(glt)
    def append(self, glt):
        self.YoI.append(glt)
    def vVU(self):
        self.YoI = self.YoI[self.Kif:]
        self.Kif = 0
    def clear(self):
        self.YoI = bytearray()
        self.Kif = 0
    def jWm(self):
        if self.Kif == 0:
            return self.YoI
        else:
            return self.YoI[self.Kif:]
import threading
import socket
class KRy(threading.Thread):
    def __init__(self, _socket, connection, uuid):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._connection = connection
        self._buf = obv()
        self._uuid = uuid
        self._run = True
    def run(self):
        while self._run:
            try:
                TYl = self._socket.recv(32768)
                if len(TYl) == 0:
                    break
                self._buf.extend(TYl)
                self._connection.RyP(self._buf)
                if self._buf.Kif > 0 and self._buf.Kif < len(self._buf.YoI):
                    self._buf.vVU()
                elif self._buf.Kif >= len(self._buf.YoI):
                    self._buf.clear()
            except (OSError, socket.error) as fpI:
                pass
        self._connection.nCJ(self._uuid, XRm.zPk, "read_thread")
    def SUb(self):
        self._run = False
import queue
import threading
import socket
class qlT(threading.Thread):
    def __init__(self, _socket):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._message_queue = queue.Queue()
        self._run = True
        self._stop_event = None
    def run(self):
        while self._run:
            try:
                message = self._message_queue.get(True, 0.1)
                if message is not None:
                    self._socket.send(bytes(message))
            except (queue.Empty or socket.error) as fpI:
                pass
    def qbU(self, message):
        self._message_queue.put(message)
    def SUb(self):
        self._run = False
import logging
class Ufp(MigratoryDataLogListener):
    def __init__(self):
        self.log1 = logging.getLogger("CLIENT")
        self.log1.setLevel(logging.INFO)
        nOo = logging.StreamHandler()
        nOo.setLevel(logging.INFO)
        Uxy = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        nOo.setFormatter(Uxy)
        del self.log1.handlers[:]
        self.log1.addHandler(nOo)
    def on_log(self, log, migratory_data_log_level):
        if migratory_data_log_level == MigratoryDataLogLevel.TRACE:
            self.log1.debug(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.DEBUG:
            self.log1.debug(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.INFO:
            self.log1.info(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.WARN:
            self.log1.warning(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.ERROR:
            self.log1.error(log)
import abc
class NEq(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def trace(self, message):
        pass
    @abc.abstractmethod
    def debug(self, message):
        pass
    @abc.abstractmethod
    def info(self, message):
        pass
    @abc.abstractmethod
    def warn(self, message):
        pass
    @abc.abstractmethod
    def error(self, message):
        pass
import threading
class AcC(NEq):
    def __init__(self):
        self._lock = threading.Lock()
        self._log_listener = Ufp()
        self._log_level = MigratoryDataLogLevel.INFO
    def yFI(self, log_listener, log_level):
        with self._lock:
            self._log_listener = log_listener
            self._log_level = log_level
    def error(self, message):
        if self._log_level <= MigratoryDataLogLevel.ERROR:
            self._log_listener.on_log(message, MigratoryDataLogLevel.ERROR)
    def trace(self, message):
        if self._log_level <= MigratoryDataLogLevel.TRACE:
            self._log_listener.on_log(message, MigratoryDataLogLevel.TRACE)
    def debug(self, message):
        if self._log_level <= MigratoryDataLogLevel.DEBUG:
            self._log_listener.on_log(message, MigratoryDataLogLevel.DEBUG)
    def warn(self, message):
        if self._log_level <= MigratoryDataLogLevel.WARN:
            self._log_listener.on_log(message, MigratoryDataLogLevel.WARN)
    def info(self, message):
        if self._log_level <= MigratoryDataLogLevel.INFO:
            self._log_listener.on_log(message, MigratoryDataLogLevel.INFO)
class wPc:
    AvA = "[READ_EVENT]"
    zeZ = "[PING_EVENT]"
    hSv = "[CONNECT_EVENT]"
    QoC = "[DISCONNECT_EVENT]"
    sOi = "[READER_DISCONNECT_EVENT]"
    qlo = "[MESSAGE_RECEIVED_EVENT]"
    Uiv = "[WRITE_EVENT]"
    rla = "[CLIENT_PUBLISH_RESPONSE]"
    YlF = "[YlF]"
    Cqx = "[ENTITLEMENT_CHECK_RESPONSE]"
    GQQ = "[DISPOSE_EVENT]"
    TwE = "[PAUSE_EVENT]"
    LmE = "[RESUME_EVENT]"
    eSc = "[SUBSCRIBE_EVENT]"
    Mhi = "[UNSUBSCRIBE_EVENT]"
    oYn = "[PUBLISH_EVENT]"
    LiH = "[REPUBLISH_EVENT"
    XoV = "[PING_SERVER_EVENT]"
    lAM = "[CONNECT_SERVER_EVENT]"
    bdU = "[RECONNECT_EVENT]"
class bqk:
    AgB = 0
    njB = 1
    APR = 2
class Oqm:
    iTW = "cache_ok"
    vuS = 2
    def __init__(self, qxh, history):
        self._subject = qxh
        self._history = history
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = Oqm.iTW
        self._current_subscribe_type = bqk.AgB
    def get_seq(self):
        return self._seq
    def ZFD(self, CvH):
        self._seq = CvH
        self._messages_recieved_until_recovery += 1
    def uzS(self):
        return self._seq_id
    def bUC(self, wRp):
        self._seq_id = wRp
    def get_subject(self):
        return self._subject
    def XCr(self):
        return self._history
    def QfX(self):
        self._messages_recieved_until_recovery = 0
        if self.UCt():
            self._nr_of_consecutive_recoveries += 1
    def vjU(self):
        self._nr_of_consecutive_recoveries = 0
    def lEx(self):
        return self._messages_recieved_until_recovery
    def kzZ(self, status):
        self._cache_recovery_status = status
    def GUr(self):
        return self._cache_recovery_status
    def UCt(self):
        return self._seq_id != 70000
    def UMk(self):
        type = bqk.AgB
        if self.UCt():
            if self._nr_of_consecutive_recoveries >= Oqm.vuS:
                if self._history > 0:
                    type = bqk.njB
            else:
                type = bqk.APR
        else:
            if self._history > 0:
                type = bqk.njB
        if type == bqk.AgB or type == bqk.njB:
            self.kzZ(Oqm.iTW)
            self.vjU()
        self._current_subscribe_type = type
        return type
    def clF(self):
        return self._current_subscribe_type
    def OYJ(self):
        self._current_subscribe_type = bqk.AgB
    def max(self):
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = self.iTW
        self._current_subscribe_type = bqk.AgB
    def __repr__(self) -> str:
        iFd = "["
        iFd += "Subj = " + str(self._subject) + ", "
        iFd += "Seq = " + str(self._seq) + ", "
        iFd += "SeqId = " + str(self._seq_id) + ", "
        iFd += "NeedRecovery = " + str(self._need_recovery) + ", "
        iFd += "MessagesReceivedUntilRecovery = " + str(self._messages_recieved_until_recovery) + ", "
        iFd += "CacheRecoveryStatus = " + str(self._cache_recovery_status) + ", "
        iFd += "SubsType = " + str(self._current_subscribe_type) + ", "
        iFd += "NrOfConsecutiveRecovery = " + str(self._nr_of_consecutive_recoveries)
        iFd += "]"
        return iFd
class GAP:
    def __init__(self, operation, VFw):
        self.operation = operation
        self.VFw = VFw
    def __repr__(self) -> str:
        iFd = "OPERATION " + str(self.NwY(int(self.operation))) + " - "
        iFd += "Headers "
        for NQe in self.VFw:
            Emf = str(self.hVu(int(NQe)))
            value = None
            if Emf == "MESSAGE_TYPE" and isinstance(Emf, int):
                value = self.LNL(int(self.VFw.get(NQe)))
            else:
                value = str(self.VFw.get(NQe))
            iFd += Emf + ": " + value + " - "
        return iFd
    def NwY(self, number):
        if number == 0:
            return "SUBSCRIBE"
        elif number == 1:
            return "UNSUBSCRIBE"
        elif number == 2:
            return "PUBLISH"
        elif number == 3:
            return "PING"
        elif number == 4:
            return "IFRAME"
        elif number == 5:
            return "DISCONNECT"
        elif number == 6:
            return "AGENT_CONNECT"
        elif number == 7:
            return "RECOVERY_CACHE"
        elif number == 8:
            return "RECOVERY_IMAGE"
        elif number == 9:
            return "ENTITLEMENT_CHECK"
        elif number == 10:
            return "RESET_SUBJECT"
        elif number == 11:
            return "PROXY"
        elif number == 12:
            return "ACK"
        elif number == 13:
            return "STALE"
        elif number == 14:
            return "ADD_DATA_REF"
        elif number == 15:
            return "CLIENT_PUBLISH"
        elif number == 16:
            return "CLIENT_PUBLISH_RESPONSE"
        elif number == 17:
            return "SYNC_SUBSCRIPTION"
        elif number == 18:
            return "PUBLISH_ACK"
        elif number == 19:
            return "CONNECT"
    def hVu(self, number):
        if number == 0:
            return "SUBJECT"
        elif number == 1:
            return "DATA"
        elif number == 2:
            return "SEQ"
        elif number == 3:
            return "SEQ_ID"
        elif number == 4:
            return "ENCODING"
        elif number == 5:
            return "SESSION_ID"
        elif number == 6:
            return "DOMAIN"
        elif number == 7:
            return "CALLBACK"
        elif number == 8:
            return "IFRAME_FUNCTION"
        elif number == 9:
            return "ERROR"
        elif number == 10:
            return "PUBLISH_PASSWORD"
        elif number == 11:
            return "DOUBLE_PING"
        elif number == 12:
            return "SUBJECT_CACHE_END"
        elif number == 13:
            return "ENTITLEMENT_TOKEN"
        elif number == 14:
            return "ENTITLEMENT_STATUS"
        elif number == 15:
            return "WORKGROUP"
        elif number == 16:
            return "ACK_SUBSCRIBE"
        elif number == 17:
            return "PUBLICATION_RETAINED"
        elif number == 18:
            return "PUBLICATION_QOS"
        elif number == 19:
            return "AGENT_NAME"
        elif number == 20:
            return "PUSH_NOTIFICATION"
        elif number == 21:
            return "MESSAGE_TYPE"
        elif number == 22:
            return "USER_AGENT"
        elif number == 23:
            return "SESSION_TYPE"
        elif number == 24:
            return "SERVER_CLIENT_PING_TIME"
        elif number == 25:
            return "CLOSURE"
        elif number == 26:
            return "NODE_TYPE"
        elif number == 27:
            return "HISTORICAL_MESSAGES"
        elif number == 28:
            return "REPLY_SUBJECT"
        elif number == 29:
            return "VERSION"
        elif number == 30:
            return "PUBLISH_SAMPLE"
        elif number == 31:
            return "PUBLISH_SAMPLE_TIMESTAMP"
        elif number == 32:
            return "CLUSTER_TOKEN"
    def LNL(self, number):
        if number == 1:
            return "SNAPSHOT"
        elif number == 2:
            return "UPDATE"
        elif number == 3:
            return "RECOVERY"
class bqs:
    vct = 0
    tGP = 1
    uii = 2
import struct
class vxU:
    DTD = []
    KcZ = []
    PPf = []
    eeB = []
    Hnb = 0x19
    pHs = 0x7F
    fTy = 0x1E
    YiE = 0x1F
    FrW = []
    VFw = []
    rSa = []
    @staticmethod
    def PLD():
        for Pdu in range(0, 128):
            vxU.DTD.append(-1)
        vxU.DTD[oWA.zmZ] = 0x01
        vxU.DTD[oWA.fEB] = 0x02
        vxU.DTD[oWA.rUO] = 0x03
        vxU.DTD[oWA.HWc] = 0x04
        vxU.DTD[oWA.unY] = 0x05
        vxU.DTD[oWA.xHp] = 0x06
        vxU.DTD[oWA.dCD] = 0x08
        vxU.DTD[oWA.wiS] = 0x09
        vxU.DTD[oWA.Jue] = 0x0C
        vxU.DTD[oWA.Wqi] = 0x10
        vxU.DTD[oWA.CLIENT_PUBLISH_RESPONSE] = 0x13
        vxU.DTD[oWA.LOZ] = 0x1A
        for Pdu in range(0, 128):
            vxU.FrW.append(-1)
        for kEj in range(0, oWA.LOZ + 1):
            vxU.FrW[vxU.Weh(kEj)] = kEj
        for Pdu in range(0, 128):
            vxU.KcZ.append(-1)
        vxU.KcZ[PsT.SSa] = 0x01
        vxU.KcZ[PsT.dBF] = 0x02
        vxU.KcZ[PsT.qPC] = 0x03
        vxU.KcZ[PsT.HkI] = 0x04
        vxU.KcZ[PsT.MHX] = 0x05
        vxU.KcZ[PsT.bCA] = 0x06
        vxU.KcZ[PsT.DFN] = 0x07
        vxU.KcZ[PsT.MeO] = 0x08
        vxU.KcZ[PsT.Ruy] = 0x09
        vxU.KcZ[PsT.ERROR] = 0x0B
        vxU.KcZ[PsT.PKE] = 0x0C
        vxU.KcZ[PsT.jpR] = 0x0F
        vxU.KcZ[PsT.MDF] = 0x10
        vxU.KcZ[PsT.GVE] = 0x11
        vxU.KcZ[PsT.BBG] = 0x12
        vxU.KcZ[PsT.ebk] = 0x13
        vxU.KcZ[PsT.KAY] = 0x14
        vxU.KcZ[PsT.BMv] = 0x15
        vxU.KcZ[PsT.DKg] = 0x16
        vxU.KcZ[PsT.Mvk] = 0x17
        vxU.KcZ[PsT.Xxs] = 0x18
        vxU.KcZ[PsT.TMs] = 0x1A
        vxU.KcZ[PsT.gFz] = 0x20
        vxU.KcZ[PsT.uWt] = 0x27
        vxU.KcZ[PsT.yHj] = 0x28
        vxU.KcZ[PsT.gMY] = 0x23
        vxU.KcZ[PsT.MgJ] = 0x24
        vxU.KcZ[PsT.lEV] = 0x25
        vxU.KcZ[PsT.rDh] = 0x2C
        vxU.KcZ[PsT.bwH] = 0x2D
        vxU.KcZ[PsT.xsU] = 0x2E
        vxU.KcZ[PsT.cIA] = 0x2F
        vxU.KcZ[PsT.MWI] = 0x30
        vxU.KcZ[PsT.Wqe] = 0x1D
        vxU.KcZ[PsT.oxp] = 0x26
        for Pdu in range(0, 128):
            vxU.VFw.append(-1)
        for kEj in range(0, PsT.oxp + 1):
            vxU.VFw[vxU.Vxd(kEj)] = kEj
        for Pdu in range(0, 128):
            vxU.rSa.append(-1)
        vxU.mbs(PsT.SSa, JXC.XJM)
        vxU.mbs(PsT.dBF, JXC.EoU)
        vxU.mbs(PsT.qPC, JXC.yIr)
        vxU.mbs(PsT.HkI, JXC.yIr)
        vxU.mbs(PsT.MHX, JXC.yIr)
        vxU.mbs(PsT.bCA, JXC.yIr)
        vxU.mbs(PsT.DFN, JXC.EoU)
        vxU.mbs(PsT.MeO, JXC.EoU)
        vxU.mbs(PsT.Ruy, JXC.EoU)
        vxU.mbs(PsT.ERROR, JXC.yIr)
        vxU.mbs(PsT.PKE, JXC.EoU)
        vxU.mbs(PsT.jpR, JXC.yIr)
        vxU.mbs(PsT.BBG, JXC.XJM)
        vxU.mbs(PsT.ebk, JXC.XJM)
        vxU.mbs(PsT.KAY, JXC.XJM)
        vxU.mbs(PsT.BMv, JXC.yIr)
        vxU.mbs(PsT.DKg, JXC.yIr)
        vxU.mbs(PsT.Mvk, JXC.yIr)
        vxU.mbs(PsT.Xxs, JXC.yIr)
        vxU.mbs(PsT.TMs, JXC.XJM)
        vxU.mbs(PsT.gFz, JXC.XJM)
        vxU.mbs(PsT.uWt, JXC.XJM)
        vxU.mbs(PsT.gMY, JXC.XJM)
        vxU.mbs(PsT.MgJ, JXC.yIr)
        vxU.mbs(PsT.lEV, JXC.yIr)
        vxU.mbs(PsT.MDF, JXC.XJM)
        vxU.mbs(PsT.GVE, JXC.yIr)
        vxU.mbs(PsT.yHj, JXC.yIr)
        vxU.mbs(PsT.rDh, JXC.XJM)
        vxU.mbs(PsT.bwH, JXC.yIr)
        vxU.mbs(PsT.xsU, JXC.yIr)
        vxU.mbs(PsT.cIA, JXC.yIr)
        vxU.mbs(PsT.MWI, JXC.XJM)
        vxU.mbs(PsT.Wqe, JXC.yIr)
        vxU.mbs(PsT.oxp, JXC.yIr)
        for Pdu in range(0, 255):
            vxU.eeB.append(-1)
        vxU.eeB[vxU.pHs] = 0x01;
        vxU.eeB[vxU.fTy] = 0x02;
        vxU.eeB[vxU.YiE] = 0x03;
        vxU.eeB[wmQ.aOU] = 0x04;
        vxU.eeB[wmQ.KDl] = 0x05;
        vxU.eeB[wmQ.Ssa] = 0x06;
        vxU.eeB[wmQ.rEO] = 0x07;
        vxU.eeB[wmQ.Bdm] = 0x08;
        vxU.eeB[33] = 0x09;
        vxU.eeB[vxU.Hnb] = 0x0B;
        for Pdu in range(0, 255):
            vxU.PPf.append(-1)
        for kEj in range(0, 128):
            fpI = vxU.yjC(kEj)
            if fpI != -1:
                vxU.PPf[fpI] = kEj
    @staticmethod
    def mbs(hbS, hdr_type):
        vxU.rSa[vxU.Vxd(hbS)] = hdr_type
    @staticmethod
    def JpP(emi):
        Zfa = vxU.ULF(emi)
        hZw = 0
        for qZD in range(0, len(Zfa)):
            eeB = vxU.yjC(Zfa[qZD])
            if eeB != -1:
                hZw += 1
        if hZw == 0:
            YoI = bytearray()
            YoI.extend(Zfa)
            return YoI
        eTR = []
        for kEj in range(0, len(Zfa) + hZw):
            eTR.append(0)
        qZD = 0
        iAf = 0
        while qZD < len(Zfa):
            eeB = vxU.yjC(Zfa[qZD])
            if eeB != -1:
                eTR[iAf] = vxU.YiE
                eTR[iAf + 1] = eeB
                iAf += 1
            else:
                eTR[iAf] = Zfa[qZD]
            qZD += 1
            iAf += 1
        YoI = bytearray()
        YoI.extend(eTR)
        return YoI
    @staticmethod
    def AMG(Zfa):
        hZw = 0
        for qZD in range(0, len(Zfa)):
            eeB = vxU.yjC(Zfa[qZD])
            if eeB != -1:
                hZw += 1
        if hZw == 0:
            return Zfa
        eTR = []
        for kEj in range(0, len(Zfa) + hZw):
            eTR.append(0)
        qZD = 0
        iAf = 0
        while qZD < len(Zfa):
            eeB = vxU.yjC(Zfa[qZD])
            if eeB != -1:
                eTR[iAf] = vxU.YiE
                eTR[iAf + 1] = eeB
                iAf += 1
            else:
                eTR[iAf] = Zfa[qZD]
            qZD += 1
            iAf += 1
        YoI = bytearray()
        YoI.extend(eTR)
        return YoI
    @staticmethod
    def KAb(emi):
        Zfa = list(struct.unpack(len(emi) * 'B', emi))
        hZw = 0
        if len(Zfa) == 0:
            return emi
        for qZD in range(0, len(Zfa)):
            if Zfa[qZD] == vxU.YiE:
                hZw += 1
        eTR = []
        for kEj in range(0, len(Zfa) - hZw):
            eTR.append(0)
        qZD = 0
        iAf = 0
        while qZD < len(Zfa):
            qeI = Zfa[qZD]
            if qeI == vxU.YiE:
                if qZD + 1 < len(Zfa):
                    eTR[iAf] = vxU.rxr(Zfa[qZD + 1])
                    if eTR[iAf] == -1:
                        raise ValueError()
                    qZD += 1
                else:
                    raise ValueError()
            else:
                eTR[iAf] = qeI
            qZD += 1
            iAf += 1
        YoI = bytearray()
        YoI.extend(eTR)
        return YoI
    @staticmethod
    def dbG(emi, _headerId, _headerType):
        mFe = None
        Omr = emi.find(chr(vxU.Vxd(_headerId)))
        XdO = emi.find(chr(vxU.fTy), Omr)
        if Omr != -1 and XdO != -1:
            tRC = emi[Omr + 1:XdO]
            if _headerType == JXC.Kdr:
                mFe = tRC
            elif _headerType == JXC.EoU:
                mFe = tRC
            elif _headerType == JXC.XJM:
                mFe = tRC
            elif _headerType == JXC.yIr:
                mFe = vxU.CNe(tRC);
        return mFe
    @staticmethod
    def CNe(_dataString):
        emi = list(struct.unpack(len(_dataString) * 'B', _dataString))
        eTR = 0
        JrC = -1
        _val = 0
        oPO = len(emi)
        xgQ = 0
        if oPO == 1:
            return emi[0]
        elif oPO == 2 and emi[xgQ] == vxU.YiE:
            qeI = vxU.rxr(emi[xgQ + 1])
            if qeI != -1:
                return qeI
            else:
                raise ValueError()
        while oPO > 0:
            qeI = emi[xgQ]
            xgQ += 1
            if qeI == vxU.YiE:
                if oPO - 1 < 0:
                    raise ValueError()
                oPO -= 1
                qeI = emi[xgQ]
                xgQ += 1
                FlC = vxU.rxr(qeI)
                if FlC == -1:
                    raise ValueError()
            else:
                FlC = qeI
            if JrC > 0:
                _val |= FlC >> JrC
                eTR = eTR << 8 | (_val if _val >= 0   else _val + 256)
                _val = (FlC << (8 - JrC))
            else:
                _val = (FlC << - JrC)
            JrC = (JrC + 7) % 8;
            oPO -= 1
        return eTR
    @staticmethod
    def xQb(_val):
        if (int(_val) & 0xFFFFFF80) == 0:
            kEj = vxU.yjC(_val)
            if kEj == -1:
                return struct.pack('B', _val)
            else:
                return struct.pack('BB', vxU.YiE, kEj)
        nMX = 0
        if (int(_val) & 0xFF000000) != 0:
            nMX = 24
        elif (int(_val) & 0x00FF0000) != 0:
            nMX = 16
        else:
            nMX = 8
        eTR = []
        for kEj in range(0, 10):
            eTR.append(0)
        gVV = 0
        zvJ = 0
        while nMX >= 0:
            b = ((int(_val) >> nMX) & 0xFF)
            zvJ += 1
            eTR[gVV] |= ((b if b >= 0 else b + 256) >> zvJ)
            eeB = vxU.yjC(eTR[gVV])
            if eeB != -1:
                eTR[gVV] = vxU.YiE
                eTR[gVV + 1] = eeB
                gVV += 1
            gVV += 1
            eTR[gVV] |= (b << (7 - zvJ)) & 0x7F;
            nMX -= 8
        eeB = vxU.yjC(eTR[gVV])
        if eeB != -1:
            eTR[gVV] = vxU.YiE
            eTR[gVV + 1] = eeB
            gVV += 1
        gVV += 1
        if gVV < len(eTR):
            eTR = eTR[0:gVV]
        YoI = bytearray()
        YoI.extend(eTR)
        return YoI
    @staticmethod
    def rxr(b):
        if b >= 0:
            return vxU.PPf[int(b)]
        else:
            return -1
    @staticmethod
    def yjC(b):
        if b >= 0:
            return vxU.eeB[int(b)]
        else:
            return -1
    @staticmethod
    def Vxd(h):
        return vxU.KcZ[int(h)]
    @staticmethod
    def Weh(o):
        return vxU.DTD[int(o)]
    @staticmethod
    def pvf(hbS):
        HOM = vxU.Vxd(hbS)
        return vxU.rSa[HOM]
    @staticmethod
    def ULF(str_value):
        dtF = str_value.encode('utf-8')
        return list(struct.unpack(len(dtF) * 'B', dtF))
    @staticmethod
    def pkw(b):
        if b < 0:
            return None
        return vxU.VFw[b]
class oWA:
    zmZ = 0
    fEB = 1
    rUO = 2
    HWc = 3
    unY = 4
    xHp = 5
    dCD = 6
    wiS = 7
    Jue = 8
    Wqi = 9
    CLIENT_PUBLISH_RESPONSE = 10
    LOZ = 11
class PsT:
    SSa = 0
    dBF = 1
    qPC = 2
    HkI = 3
    MHX = 4
    bCA = 5
    DFN = 6
    MeO = 7
    Ruy = 8
    ERROR = 9
    PKE = 10
    jpR = 11
    BBG = 12
    ebk = 13
    KAY = 14
    BMv = 15
    DKg = 16
    Mvk = 17
    Xxs = 18
    TMs = 19
    gFz = 20
    uWt = 21
    gMY = 22
    MgJ = 23
    lEV = 24
    MDF = 25
    GVE = 26
    yHj = 27
    rDh = 28
    bwH = 29
    xsU = 30
    cIA = 31
    MWI = 32
    Wqe = 33
    oxp = 34
class JXC:
    Kdr = 0
    EoU = 1
    XJM = 2
    yIr = 3
class wmQ:
    aOU = 0x00
    rEO = 0x22
    KDl = 0x0A
    Ssa = 0x0D
    Bdm = 0x5C
class Bhs:
    CgC = 1
    USL = 2
    ucE = 3
    vao = 4
class CXT:
    svJ = 0
    WwQ = 1
    Edn = 2
    WHB = 3
    Gnq = 4
    zTW = 5
    oOt = 6
    XGh = 7
    LJK = 8
class oxm:
    SNAPSHOT = "1"
    UPDATE = "2"
    RECOVERED = "3"
    HISTORICAL = "4"
class Snd:
    eFU = "d"
    UZd = "a"
vxU.PLD()
class sUN(PyJ):
    Iww = "POST / HTTP/1.1\r\n"
    ZmT = "Host: "
    JgV = "Content-Length: "
    mDG = "000"
    bEb = "\r\n"
    def __init__(self):
        pass
    def GqZ(self, host):
        jiT = obv()
        jiT.extend(bytes(sUN.Iww, 'utf-8'))
        jiT.extend(bytes(sUN.ZmT, 'utf-8'))
        jiT.extend(bytes(host, 'utf-8'))
        jiT.extend(bytes(sUN.bEb, 'utf-8'))
        jiT.extend(bytes(sUN.JgV, 'utf-8'))
        jiT.content_length_mark = len(jiT.YoI)
        jiT.extend(bytes(sUN.mDG, 'utf-8'))
        jiT.extend(bytes(sUN.bEb, 'utf-8'))
        jiT.extend(bytes(sUN.bEb, 'utf-8'))
        jiT.payload_mark = len(jiT.YoI)
        return jiT
    def Skw(self, jiT):
        Kif = len(jiT.YoI)
        YDk = len(jiT.YoI) - jiT.payload_mark
        GqR = bytes(str(YDk), 'utf-8')
        if len(GqR) <= len(sUN.mDG):
            sZK = 0
            for kEj in range(len(sUN.mDG) - len(GqR),
                           len(sUN.mDG)):
                jiT.YoI[jiT.content_length_mark + kEj] = GqR[sZK]
                sZK = sZK + 1
        else:
            UPc = jiT.YoI[0:jiT.content_length_mark]
            UPc.extend(GqR)
            UPc.extend(jiT.YoI[(jiT.content_length_mark + len(sUN.mDG)):])
            jiT.YoI = UPc
    def HLn(self, host, encrypted):
        jiT = obv()
        return jiT
import random
class cAG(PyJ):
    kSB = "GET /WebSocketConnection HTTP/1.1\r\n"
    ruo = "GET /WebSocketConnection-Secure HTTP/1.1\r\n"
    sRQ = "Host: "
    Sen = "Origin: "
    nKZ = "Upgrade: websocket\r\n"
    aUc = "Sec-WebSocket-Key: 23eds34dfvce4\r\n"
    Kga = "Sec-WebSocket-Version: 13\r\n"
    cNI = "Sec-WebSocket-Protocol: pushv1\r\n"
    RhG = "Connection: Upgrade\r\n"
    bEb = "\r\n"
    Zxf = 2
    Zvm = 10
    xCR = 128
    NtQ = 128
    def GqZ(self, host):
        jiT = obv()
        Kif = cAG.Zvm
        for kEj in range(0, 10):
            jiT.extend(bytes([0]))
        for kEj in range(0, 4):
            Kif += 1
            rZr = random.randint(0, 255)
            jiT.extend([rZr])
        jiT.yTC(Kif)
        jiT.body_start_mark = Kif
        return jiT
    def Skw(self, jiT):
        Bpl = cAG.NtQ
        Bpl |= cAG.Zxf
        jiT.body_end_mark = len(jiT.YoI)
        eRJ = jiT.body_end_mark - jiT.body_start_mark
        wsg = self.ZlH(eRJ)
        rGs = self.YIO(eRJ, wsg)
        USB = 0
        jis = 0
        if wsg == 1:
            USB = 8
            jis = 8
            jiT.YoI[jis] = Bpl
            jiT.YoI[jis + 1] = rGs[0] | cAG.xCR
        elif wsg == 2:
            USB = 6
            jis = 6
            jiT.YoI[jis] = Bpl
            jiT.YoI[jis + 1] = 126 | cAG.xCR
            jis += 2
            for kEj in range(0, 2):
                jiT.YoI[jis + kEj] = rGs[kEj]
        else:
            jiT.YoI[jis] = Bpl
            jiT.YoI[jis + 1] = 127 | cAG.xCR
            jis += 2
            for kEj in range(0, 8):
                jiT.YoI[jis + kEj] = rGs[kEj]
        vyH = bytearray()
        vyH.extend([jiT.YoI[jiT.body_start_mark - 4]])
        vyH.extend([jiT.YoI[jiT.body_start_mark - 3]])
        vyH.extend([jiT.YoI[jiT.body_start_mark - 2]])
        vyH.extend([jiT.YoI[jiT.body_start_mark - 1]])
        yVF = 0
        for kEj in range(jiT.body_start_mark, jiT.body_end_mark):
            b = jiT.YoI[kEj] ^ vyH[yVF]
            jiT.YoI[kEj] = b
            if yVF == 3:
                yVF = 0
            else:
                yVF += 1
        jiT.yTC(USB)
    def HLn(self, host, encrypted):
        jiT = obv()
        if encrypted is False:
            jiT.extend(bytes(cAG.kSB, 'utf-8'))
        else:
            jiT.extend(bytes(cAG.ruo, 'utf-8'))
        jiT.extend(bytes(cAG.Sen, 'utf-8'))
        jiT.extend(bytes("http://" + str(host), 'utf-8'))
        jiT.extend(bytes(cAG.bEb, 'utf-8'))
        jiT.extend(bytes(cAG.sRQ, 'utf-8'))
        jiT.extend(bytes(str(host), 'utf-8'))
        jiT.extend(bytes(cAG.bEb, 'utf-8'))
        jiT.extend(bytes(cAG.nKZ, 'utf-8'))
        jiT.extend(bytes(cAG.RhG, 'utf-8'))
        jiT.extend(bytes(cAG.aUc, 'utf-8'))
        jiT.extend(bytes(cAG.Kga, 'utf-8'))
        jiT.extend(bytes(cAG.cNI, 'utf-8'))
        jiT.extend(bytes(cAG.bEb, 'utf-8'))
        return jiT
    def ZlH(self, size):
        if size <= 125:
            return 1
        elif size <= 65535:
            return 2
        return 8
    def YIO(self, value, wsg):
        myd = bytearray()
        ZSZ = 8 * wsg - 8
        for kEj in range(0, wsg):
            Ksy = self.ZzL(value, ZSZ - 8 * kEj)
            JBv = Ksy - (256 * int(Ksy / 256))
            myd.extend([JBv])
        return myd
    def ZzL(self, val, n):
        return (val % 0x100000000) >> n
import time
import zlib
import base64
class xuW:
    def __init__(self):
        self._encoding = CXT.LJK
    def Lhq(self):
        self._encoding = CXT.Gnq
    def XoE(self, YoI, entitlement_token, session_type, user_agent, version):
        YoI.extend(bytes(chr(vxU.Weh(oWA.LOZ)), 'utf-8'))
        if entitlement_token is not None:
            self.Vjn(YoI, vxU.Vxd(PsT.ebk),
                                   vxU.JpP(entitlement_token))
        if session_type is not None:
            self.Vjn(YoI, vxU.Vxd(PsT.MgJ),
                                   vxU.xQb(session_type))
        if user_agent is not None:
            self.Vjn(YoI, vxU.Vxd(PsT.gMY),
                                   vxU.JpP(user_agent))
        self.Vjn(YoI, vxU.Vxd(PsT.bwH),
                               vxU.xQb(version))
        self.Vjn(YoI, vxU.Vxd(PsT.MHX),
                               vxU.xQb(self._encoding))
        YoI.extend(bytes(chr(vxU.pHs), 'utf-8'))
    def XOx(self, YoI, qxh, session_id):
        YoI.extend(bytes(chr(vxU.Weh(oWA.zmZ)), 'utf-8'))
        self.Vjn(YoI, vxU.Vxd(PsT.SSa),
                               vxU.JpP(qxh.get_subject()))
        if session_id is not None and session_id >= 0:
            self.Vjn(YoI, vxU.Vxd(PsT.bCA),
                                   vxU.xQb(session_id))
        vSa = qxh.UMk()
        if vSa == bqk.njB:
            self.Vjn(YoI, vxU.Vxd(PsT.yHj),
                                   vxU.xQb(qxh.XCr()))
        elif vSa == bqk.APR:
            self.Vjn(YoI, vxU.Vxd(PsT.HkI),
                                   vxU.xQb(qxh.uzS()))
            self.Vjn(YoI, vxU.Vxd(PsT.qPC),
                                   vxU.xQb((qxh.get_seq() + 1)))
        self.Vjn(YoI, vxU.Vxd(PsT.MHX),
                               vxU.xQb(self._encoding))
        YoI.extend(bytes(chr(vxU.pHs), 'utf-8'))
    def fkD(self, YoI, session_id, qxh):
        YoI.extend(bytes(chr(vxU.Weh(oWA.fEB)), 'utf-8'))
        self.Vjn(YoI, vxU.Vxd(PsT.SSa),
                               vxU.JpP(qxh.get_subject()))
        if session_id >= 0:
            self.Vjn(YoI, vxU.Vxd(PsT.bCA),
                                   vxU.xQb(session_id))
        self.Vjn(YoI, vxU.Vxd(PsT.MHX),
                               vxU.xQb(self._encoding))
        YoI.extend(bytes(chr(vxU.pHs), 'utf-8'))
    def Eye(self, YoI, message, session_id):
        YoI.extend(bytes(chr(vxU.Weh(oWA.Wqi)), 'utf-8'))
        self.Vjn(YoI, vxU.Vxd(PsT.SSa),
                               vxU.JpP(message.get_subject()))
        if message.is_compressed():
            djx = self.mJH(message.get_content())
            if len(djx) < len(message.get_content()):
                self.Vjn(YoI, vxU.Vxd(PsT.dBF),
                                       vxU.AMG(djx))
            else:
                self.Vjn(YoI, vxU.Vxd(PsT.dBF),
                                       vxU.AMG(message.get_content()))
                message.set_compressed(False)
        else:
            self.Vjn(YoI, vxU.Vxd(PsT.dBF),
                                   vxU.AMG(message.get_content()))
        if message.get_reply_to_subject() is not None:
            self.Vjn(YoI, vxU.Vxd(PsT.rDh),
                                   vxU.JpP(message.get_reply_to_subject()))
        if message.get_closure() is not None and len(message.get_content()) > 0:
            self.Vjn(YoI, vxU.Vxd(PsT.MDF),
                                   vxU.JpP(message.get_closure()))
        if session_id >= 0:
            self.Vjn(YoI, vxU.Vxd(PsT.bCA),
                                   vxU.xQb(session_id))
        if message.is_retained() is True:
            self.Vjn(YoI, vxU.Vxd(PsT.Mvk),
                                   vxU.xQb(1))
        else:
            self.Vjn(YoI, vxU.Vxd(PsT.Mvk),
                                   vxU.xQb(0))
        nqb = message.get_qos()
        if nqb == QoS.GUARANTEED:
            self.Vjn(YoI, vxU.Vxd(PsT.Xxs),
                                   vxU.xQb(QoS.GUARANTEED))
        elif nqb == QoS.STANDARD:
            self.Vjn(YoI, vxU.Vxd(PsT.Xxs),
                                   vxU.xQb(QoS.STANDARD))
        if message.is_compressed():
            self.Vjn(YoI, vxU.Vxd(PsT.oxp),
                                   vxU.xQb(1))
        self.Vjn(YoI, vxU.Vxd(PsT.MHX),
                               vxU.xQb(self._encoding))
        YoI.extend(bytes(chr(vxU.pHs), 'utf-8'))
    def vAi(self, YoI, session_id):
        YoI.extend(bytes(chr(vxU.Weh(oWA.HWc)), 'utf-8'))
        if session_id >= 0:
            self.Vjn(YoI, vxU.Vxd(PsT.bCA),
                                   vxU.xQb(session_id))
        self.Vjn(YoI, vxU.Vxd(PsT.MHX),
                               vxU.xQb(self._encoding))
        YoI.extend(bytes(chr(vxU.pHs), 'utf-8'))
    def rMQ(self, YoI, qxh, CvH, epoch, session_id):
        YoI.extend(bytes(chr(vxU.Weh(oWA.PUBLISH_ACK)), 'utf-8'))
        self.Vjn(YoI, vxU.Vxd(PsT.SSa),
                               vxU.JpP(qxh))
        self.Vjn(YoI, vxU.Vxd(PsT.qPC),
                               vxU.xQb(CvH))
        self.Vjn(YoI, vxU.Vxd(PsT.HkI),
                               vxU.xQb(epoch))
        self.Vjn(YoI, vxU.Vxd(PsT.bCA),
                               vxU.xQb(session_id))
        self.Vjn(YoI, vxU.Vxd(PsT.MHX),
                               vxU.xQb(self._encoding))
        YoI.extend(bytes(chr(vxU.pHs), 'utf-8'))
    def Vjn(self, YoI, esp, glt):
        YoI.append(esp)
        YoI.extend(glt)
        YoI.append(vxU.fTy)
    def mJH(self, ejx):
        try:
            zEX = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
            wZA = zEX.compress(ejx)
            wZA += zEX.flush()
            EYC = base64.b64encode(wZA)
        except zlib.error as ex:
            return ejx
        return EYC
    def tKT(self, glt):
        try:
            LuN = base64.b64decode(glt)
            if not LuN:
                return glt
            zvY = zlib.decompress(LuN, -15)
        except base64.binascii.Error as ex:
            return glt
        except zlib.error as ex:
            return glt
        return zvY
import socket
import ssl
class wYp:
    @staticmethod
    def ARz(host, KHi, encryption, socket_timeout_seconds):
        kFD = None
        if encryption is False:
            kFD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            kFD.settimeout(socket_timeout_seconds)
            kFD.connect((host, KHi))
        else:
            IRK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            IRK.settimeout(socket_timeout_seconds)
            try:
                mgQ = ssl.create_default_context()
                kFD = mgQ.wrap_socket(IRK, server_hostname=host)
            except Exception as fpI: print(fpI)
            kFD.connect((host, KHi))
        return kFD
class jzR:
    Jxe = 80
    nfd = 443
    gEG = 100
    def __init__(self, address, encryption):
        self._weight = jzR.gEG
        self._unparsed_address = address
        FiE = address.find(' ')
        if FiE != -1:
            self._weight = int(address[0:FiE])
            if self._weight < 0 or self._weight > 100:
                raise ValueError(
                    "The Weight of a clust Member must be between 0 and 100, Weight: " + str(self._weight))
        kEj = address.find(']')
        yVF = address.rfind(":")
        bbu = None
        KHi = None
        if yVF != -1 and yVF + 1 < len(address) and yVF >= kEj:
            bbu = address[0:yVF]
            KHi = int(address[yVF + 1:])
        else:
            bbu = address
            if encryption:
                KHi = self.nfd
            else:
                KHi = self.Jxe
        if KHi < 0 or KHi > 65535:
            raise ValueError("Invalid Port number")
        if bbu == "":
            raise ValueError("Clust Member with null address")
        if bbu == "*":
            raise ValueError("Wildcard address (*) cannot be used to define a clust Member")
        self._address = bbu
        self._port = KHi
    def pkG(self):
        return self._weight
    def ijn(self):
        return self._port
    def Cdx(self):
        return self._address
    def Xuy(self, hvC):
        if (self._address == hvC._address):
            if self._port == hvC._port:
                return True
        return False
    def Inb(self):
        return self._unparsed_address
    def __repr__(self) -> str:
        iFd = "[Host="
        iFd += str(self.Cdx())
        iFd += ", Port="
        iFd += str(self.ijn())
        iFd += "]"
        return iFd
import random
class icR:
    def __init__(self, servers, encryption):
        self._members = []
        self._inactive_members = []
        self._current_member = None
        for kEj in range(0, len(servers)):
            self._members.append(jzR(servers[kEj], encryption))
    def Jsw(self):
        nZz = self.hWz()
        if len(nZz) == 0:
            self._inactive_members = []
            nZz = list(self._members)
        Rgs = self.RzT(nZz)
        self._current_member = nZz[Rgs]
        return self._current_member
    def hWz(self):
        nZz = list(self._members)
        for xBI in self._members:
            for IPW in self._inactive_members:
                if xBI.Xuy(IPW):
                    nZz.remove(xBI)
        return nZz
    def RzT(self, nZz):
        Rgs = -1
        SvO = 0
        for xBI in nZz:
            SvO = SvO + xBI.pkG()
        if SvO == 0:
            Rgs = int(len(nZz) * random.uniform(0, 1))
        else:
            MxX = int(SvO * random.uniform(0, 1))
            SvO = 0
            for kEj in range(0 < len(nZz)):
                SvO = SvO + nZz[kEj].pkG()
                if SvO > MxX:
                    Rgs = kEj
                    break
        return Rgs
    def XKi(self):
        return self._current_member
    def ULU(self, hvC):
        self._inactive_members.append(hvC)
import threading
class NYb:
    xHp = 0
    cDJ = 1
class iFm:
    def __init__(self):
        self._state = NYb.xHp
        self._lock = threading.Lock()
    def ZQg(self, state):
        with self._lock:
            self._state = state
    def hid(self):
        with self._lock:
            return self._state
class Nnr:
    @staticmethod
    def search(glt, dataLength, pattern, patternLength):
        RHM = [0] * patternLength
        yVF = 0
        len = 0
        kEj = 1
        while kEj < patternLength:
            if pattern[kEj] == pattern[len]:
                len += 1
                RHM[kEj] = len
                kEj += 1
            else:
                if len != 0:
                    len = RHM[len - 1]
                else:
                    RHM[kEj] = 0
                    kEj += 1
        kEj = 0
        while kEj < dataLength:
            if pattern[yVF] == glt[kEj]:
                kEj += 1
                yVF += 1
            if yVF == patternLength:
                return kEj - yVF
            elif kEj < dataLength and pattern[yVF] != glt[kEj]:
                if yVF != 0:
                    yVF = RHM[yVF - 1]
                else:
                    kEj += 1
        return -1
import abc
class sBj(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def LSS(self, NFc):
        pass
import abc
class YnO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def LKe(self, NFc):
        pass
    @abc.abstractmethod
    def fqB(self):
        pass
import abc
class avr(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def oYE(self, status, info):
        pass
    @abc.abstractmethod
    def neo(self, message):
        pass
import abc
class tNh(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def BVr(self, sWa, connection, keep_alive):
        pass
    @abc.abstractmethod
    def nCJ(self, sWa, connection, disconnect_info):
        pass
    @abc.abstractmethod
    def MRX(self, connection):
        pass
    @abc.abstractmethod
    def cancel(self):
        pass
    @abc.abstractmethod
    def uFI(self, value):
        pass
class asV(MigratoryDataMessage):
    def __init__(self, _subject, _content, closure, retained, _message_type, qos_, _reply_subject, _compression):
        super().__init__(_subject, _content, closure)
        self._retained = retained
        self._message_type = _message_type
        self.VXt = qos_
        self._reply_to_subject = _reply_subject
        self._compression = _compression
    def ZFD(self, CvH):
        self._seq = CvH
    def nnO(self, epoch):
        self._epoch = epoch
class DVj:
    def __init__(self, RIo, status, info, migratory_data_message):
        self.RIo = RIo
        self.status = status
        self.info = info
        self.migratory_data_message = migratory_data_message
class Dle:
    qlT = 0
    MjH = 1
class nnZ:
    LOZ = 1,
    OSM = 2,
    juR = 3,
    nCc = 4,
    zmZ = 5,
    fEB = 6,
    xHp = 7,
    ZBr = 8,
    afK = 9,
    CYA = 10,
    rUO = 11,
    iDL = 12
class QPy:
    def __init__(self, operation):
        self.operation = operation
        self.connection_uuid = None
        self.disconnect_reason = None
        self.EMh = None
        self.history = None
        self.md_message = None
        self.message = None
        self.info = None
    @staticmethod
    def chE():
        return QPy(nnZ.LOZ)
    @staticmethod
    def dDL(EMh, history):
        NFc = QPy(nnZ.zmZ)
        NFc.EMh = EMh
        NFc.history = history
        return NFc
    @staticmethod
    def VYS(EMh):
        NFc = QPy(nnZ.fEB)
        NFc.EMh = EMh
        return NFc
    @staticmethod
    def tEa(message):
        NFc = QPy(nnZ.rUO)
        NFc.md_message = message
        return NFc
    @staticmethod
    def wCN(message):
        NFc = QPy(nnZ.CYA)
        NFc.message = message
        return NFc
    @staticmethod
    def UTJ(uuid, disconnect_reason):
        NFc = QPy(nnZ.xHp)
        NFc.connection_uuid = uuid
        NFc.disconnect_reason = disconnect_reason
        return NFc
    @staticmethod
    def lFD(disconnect_info):
        NFc = QPy(nnZ.afK)
        NFc.info = disconnect_info
        return NFc
    @staticmethod
    def Wdz():
        NFc = QPy(nnZ.ZBr)
        return NFc
    @staticmethod
    def DPM():
        NFc = QPy(nnZ.OSM)
        return NFc
    @staticmethod
    def Qkq():
        NFc = QPy(nnZ.nCc)
        return NFc
    @staticmethod
    def bUY():
        NFc = QPy(nnZ.juR)
        return NFc
    @staticmethod
    def wsp():
        NFc = QPy(nnZ.iDL)
        return NFc
import re
class QZW:
    EtN = 0
    xIj = 1
    KVJ = 2
class XRm:
    saS = "OK"
    lFF = "DENY"
    acu = "connection_active_close_keep_alive"
    bhx = "connection_active_close_seq_higher"
    zPk = "connection_passive_close"
    BWx = "connection_error"
    iTW = "cache_ok"
    tZk = "cache_ok_no_new_message"
    HOr = "cache_ok_new_epoch"
    UDL = "end"
    FAp = "^\/([^\/]+\/)*([^\/]+|\*)$"
    @staticmethod
    def VUV(tRC):
        if not isinstance(tRC, str):
            return False
        QIq = re.compile(XRm.FAp)
        if QIq.search(tRC) is not None:
            return True
        return False
    @staticmethod
    def Xft(EMh):
        OoM = []
        for qxh in EMh:
            if qxh is not None and XRm.VUV(qxh):
                OoM.append(qxh)
        return OoM
    @staticmethod
    def Xda(sCn, recv_seq, recv_seq_id, listener_notifier, logger):
        if sCn.uzS() != recv_seq_id:
            sCn.ZFD(recv_seq)
            sCn.bUC(recv_seq_id)
            return QZW.EtN
        if recv_seq <= sCn.get_seq():
            return QZW.xIj
        if recv_seq == sCn.get_seq() + 1:
            if sCn.clF() == bqk.APR:
                sCn.OYJ()
                listener_notifier.oYE(MigratoryDataClient.NOTIFY_DATA_SYNC, sCn.get_subject())
                logger.debug(str(wPc.qlo) + str(
                    MigratoryDataClient.NOTIFY_DATA_SYNC) + str(sCn))
            sCn.ZFD(sCn.get_seq() + 1)
            return QZW.EtN
        if sCn.lEx() > 0:
            logger.info("Missing Messages: expected message with sequence number: " + str(
                sCn.get_seq() + 1) + ", received instead message with sequence number:  " + str(recv_seq) + " !")
            return QZW.KVJ
        logger.info("Reset sequence: '" + str(sCn.get_seq() + 1) + "'. The new sequence is: '" + str(recv_seq) + "' !")
        sCn.ZFD(recv_seq)
        listener_notifier.oYE(MigratoryDataClient.NOTIFY_DATA_RESYNC, sCn.get_subject())
        logger.debug(
            wPc.qlo + MigratoryDataClient.NOTIFY_DATA_RESYNC + str(sCn))
        return QZW.EtN
    @staticmethod
    def aji(sCn, recv_seq, recv_seq_id, listener_notifier, logger):
        if sCn.uzS() != recv_seq_id:
            sCn.ZFD(recv_seq)
            sCn.bUC(recv_seq_id)
            return QZW.EtN
        if recv_seq <= sCn.get_seq():
            return QZW.xIj
        if sCn.clF() == bqk.APR:
            sCn.OYJ()
        sCn.ZFD(recv_seq)
        return QZW.EtN
import threading
class Lea:
    def __init__(self):
        self._subject_table = {}
        self._empty_subject = Oqm("", 0)
        self._lock = threading.Lock()
    def IWC(self, EMh, history):
        with self._lock:
            for qxh in EMh:
                erT = self._subject_table.get(qxh)
                if erT is None:
                    self._subject_table[qxh] = Oqm(qxh, history)
    def dHb(self, EMh):
        with self._lock:
            FZV = []
            for qxh in EMh:
                erT = self._subject_table.get(qxh)
                if erT is not None:
                    try:
                        del self._subject_table[qxh]
                        FZV.append(erT)
                    except KeyError:
                        pass
            return FZV
    def Vsf(self):
        with self._lock:
            return self._subject_table.keys()
    def get_subject(self, qxh):
        with self._lock:
            return self._subject_table.get(qxh)
    def JsP(self, qxh):
        with self._lock:
            Gwc = self._subject_table.get(qxh)
            if Gwc is None:
                return False
            else:
                return True
    def QLN(self):
        with self._lock:
            return self._empty_subject
    def qmK(self):
        with self._lock:
            for NQe in self._subject_table:
                self._subject_table[NQe].max()
import threading
import queue
import time
class Pkk(YnO, threading.Thread):
    def __init__(self, mcD, logger):
        threading.Thread.__init__(self)
        self._logger = logger
        self._event_handler = mcD
        self._control_queue = queue.Queue()
        self._running = Fwq(True)
    def run(self):
        while self._running.lBf():
            self.sIx()
        self._event_handler.LSS(QPy.DPM())
        self._logger.debug("Exit single_thread_event_loop thread")
    def LKe(self, NFc):
        if self._running.lBf():
            self._control_queue.put(NFc)
    def sIx(self):
        try:
            NtS = self._control_queue.get(True, 0.1)
            if NtS is not None:
                self._event_handler.LSS(NtS)
        except queue.Empty:
            pass
    def fqB(self):
        self._running.URV(False)
class DeA:
    @staticmethod
    def han(jiT, yTC):
        IPA = mJo(-1, -1)
        if yTC == len(jiT.YoI):
            return IPA
        Kif = yTC
        NEC = 2
        noy = 0
        MgP = 0
        HMe = len(jiT.YoI) - Kif
        if HMe < NEC:
            return IPA
        b = jiT.YoI[Kif]
        Bpl = (b >> 7) & 0x01
        OVS = b & 0x40
        FCj = b & 0x20
        xcU = b & 0x10
        if Bpl != 1 or OVS != 0 or FCj != 0 or xcU != 0:
            return IPA
        Kif += 1
        b = jiT.YoI[Kif]
        RqL = b & 0x7F
        if RqL < 126:
            MgP = 0
            noy = RqL
        elif RqL == 126:
            MgP = 2
            if HMe < NEC + MgP:
                return IPA
            CVz = bytearray()
            for kEj in range(Kif + 1, Kif + 1 + MgP):
                CVz.extend([jiT.YoI[kEj]])
            noy = DeA.ysW(CVz)
            Kif += MgP
        elif RqL == 127:
            MgP = 8
            if HMe < NEC + MgP:
                return IPA
            CVz = bytearray()
            for kEj in range(Kif + 1, Kif + 1 + MgP):
                CVz.extend([jiT.YoI[kEj]])
            noy = DeA.ysW(CVz)
            Kif += MgP
        if HMe < (NEC + MgP + noy):
            return IPA
        Kif += 1
        return mJo(Kif, Kif + noy)
    @staticmethod
    def ysW(glt):
        if len(glt) == 2:
            return ((glt[0] & 0xFF) << 8) | (glt[1] & 0xFF)
        else:
            return ((glt[4] & 0x7F) << 24) | ((glt[5] & 0xFF) << 16) | ((glt[6] & 0xFF) << 8) | (glt[7] & 0xFF)
import re
class kWi:
    @staticmethod
    def Cvx(jiT, logger):
        KTf = jiT.Kif
        if jiT.YoI[KTf] == 72:
            KTf = kWi.fmr(jiT)
        if KTf == -1:
            return []
        jiT.yTC(KTf)
        EaA = []
        while True:
            if KTf >= len(jiT.YoI):
                return EaA
            if jiT.YoI[KTf] == vxU.Hnb:
                KTf += 1
            else:
                try:
                    KAP = DeA.han(jiT, KTf)
                except IndexError:
                    KAP = mJo(-1, -1)
                Gwn = KAP.pIu()
                kzi = KAP.ufj()
                if Gwn == -1:
                    return EaA
                while True:
                    kEj = kWi.BFc(jiT, Gwn, kzi, vxU.pHs)
                    if kEj == -1:
                        break
                    VFw = kWi.xZS(jiT, Gwn + 1, kEj, logger)
                    if VFw is not None:
                        message = GAP(vxU.FrW[jiT.YoI[Gwn]], VFw)
                        EaA.append(message)
                    Gwn = kEj + 1
                    jiT.yTC(Gwn)
                KTf = jiT.Kif
    @staticmethod
    def RuE(jiT, logger):
        Kif = kWi.CSa(jiT)
        if Kif == -1:
            return []
        jiT.yTC(Kif)
        EaA = []
        while True:
            kEj = kWi.BFc(jiT, Kif, len(jiT.YoI), vxU.pHs)
            if kEj == -1:
                break
            if jiT.YoI[Kif] == 72:
                EaA.extend(kWi.RuE(jiT, logger))
                break
            VFw = kWi.xZS(jiT, Kif + 1, kEj, logger)
            if VFw is not None:
                message = GAP(vxU.FrW[jiT.YoI[Kif]], VFw)
                EaA.append(message)
            Kif = kEj + 1
            jiT.yTC(Kif)
        return EaA
    @staticmethod
    def CSa(jiT):
        Kif = jiT.Kif
        if jiT.YoI[Kif] == 72:
            GHF = "\r\n\r\n".encode("utf-8")
            FHC = Nnr.search(jiT.YoI[Kif:], len(jiT.YoI), GHF,
                                                   len(GHF))
            if FHC != -1:
                Kif += FHC + len(GHF)
                jiT.yTC(Kif)
            else:
                return -1
        return Kif
    @staticmethod
    def fmr(jiT):
        GHF = "\r\n\r\n".encode("utf-8")
        Kif = jiT.Kif
        kEj = Nnr.search(jiT.YoI[Kif:], len(jiT.YoI), GHF,
                             len(GHF))
        if kEj == -1:
            return -1
        Kif = kEj + len(GHF)
        return Kif
    @staticmethod
    def BFc(jiT, start, end, value):
        for kEj in range(start, end):
            if jiT.YoI[kEj] == value:
                return kEj
        return -1
    @staticmethod
    def xZS(jiT, start, end, logger):
        VFw = None
        while True:
            if start >= end:
                break
            hbS = jiT.YoI[start]
            zRS = kWi.BFc(jiT, start + 1, end, vxU.fTy)
            if zRS == -1:
                logger.trace(
                    "Received an invalid msg: Hdr end missing - msg ignored, Hdr Position: " + str(
                        start) + ", " + str(jiT.YoI[start:end]))
                return None
            esp = vxU.pkw(hbS)
            if esp is None:
                logger.trace("Received an unknown Hdr - Hdr ignored, Hdr Position: " + str(jiT.YoI))
                start = zRS + 1
            start = start + 1
            if VFw is None:
                VFw = {}
            value = None
            scH = vxU.pvf(esp)
            FKQ = jiT.YoI[start:zRS]
            if scH == JXC.yIr:
                value = vxU.CNe(FKQ)
            elif scH == JXC.XJM:
                dtF = vxU.KAb(FKQ)
                value = dtF.decode('utf-8')
            elif scH == JXC.EoU:
                value = vxU.KAb(FKQ)
            elif scH == JXC.Kdr:
                value = FKQ
            rpz = VFw.get(esp)
            if rpz is None:
                VFw[esp] = value
            else:
                values = [rpz, value]
                VFw[esp] = values
            start = zRS + 1
        return VFw
import threading
import queue
class YfI(avr, threading.Thread):
    def __init__(self, listener):
        super().__init__()
        self._queue = queue.Queue()
        self._run = True
        self._migratory_data_listener = listener
    def oYE(self, status, info):
        self._queue.put(DVj(Dle.qlT, status, info, None))
    def neo(self, message):
        self._queue.put(DVj(Dle.MjH, None, None, message))
    def run(self):
        while self._run:
            try:
                vYd = self._queue.get(True, 0.1)
                if self._migratory_data_listener is not None:
                    if vYd.RIo == Dle.qlT:
                        self._migratory_data_listener.on_status(vYd.status, vYd.info)
                    elif vYd.RIo == Dle.MjH:
                        self._migratory_data_listener.on_message(vYd.migratory_data_message)
            except queue.Empty:
                pass
    def SUb(self):
        self._run = False
import socket
import uuid
import threading
class Xkt:
    LOZ = 0
    zrx = 1
class zHn:
    Jqp = 0
    nCc = 1
    vsv = 2
class Ard:
    ikq = 0
    OkM = 1
    HKO = 2
class Connection:
    def __init__(self, configuration, listener_notifier, FfZ, AEu, client_state, logger):
        self._lock = threading.Lock()
        self._reconnect_retries = 0
        self._session = -1
        self._socket = None
        self._reader = None
        self._writer = None
        self._reconnected = False
        self._session_received = False
        self._loop = None
        self._listener_notifier = None
        self._servers_down_count = 0
        self._is_server_down = False
        self._max_message_size = None
        self._publish_closures = []
        self._current_connection_id = None
        self._app_state = zHn.vsv
        self._node_type = Ard.ikq
        self._subject_manager = Lea()
        self._logger = logger
        self._configuration = configuration
        self._listener_notifier = listener_notifier
        self._cluster = FfZ
        self._scheduler = AEu
        self._client_state = client_state
        self._push_encoder = xuW()
        self._transport_type = self._configuration.trans_type
        if self._transport_type == hsd.HTTP:
            self._transport_encoder = sUN()
            self._push_encoder.Lhq()
        else:
            self._transport_encoder = cAG()
        self._message_listener = XcA()
        self._message_listener.JoW(self)
        self._cluster_token = None
    def YbJ(self):
        return self._message_listener
    def RyP(self, jiT):
        EaA = None
        if self._transport_type == hsd.IWR:
            EaA = kWi.Cvx(jiT, self._logger)
        else:
            EaA = kWi.RuE(jiT, self._logger)
        if len(EaA) > 0:
            self.YMg(EaA)
        else:
            self._loop.LKe(QPy.wsp())
            self._logger.debug(str(wPc.zeZ))
    def YMg(self, EaA):
        for kEj in range(0, len(EaA)):
            message = EaA[kEj]
            if message.operation == oWA.CLIENT_PUBLISH_RESPONSE or message.operation == oWA.rUO or message.operation == oWA.wiS or message.operation == oWA.dCD \
                    or message.operation == oWA.zmZ or message.operation == oWA.fEB or message.operation == oWA.LOZ:
                self._loop.LKe(QPy.wCN(message))
                self._logger.debug(wPc.AvA + str(message))
            elif message.operation == oWA.HWc:
                self._loop.LKe(QPy.wsp())
                self._logger.debug(str(wPc.zeZ))
            elif message.operation == oWA.Wqi:
                break
            else:
                self._logger.warn("No existing operation for msg: " + str(message))
    def connect(self):
        sWa = uuid.uuid4()
        self.pIY(sWa)
        if self._socket is not None:
            self.disconnect()
        try:
            hvC = self._cluster.Jsw()
            self._logger.info("Connecting to the clust Member: " + str(self._cluster.XKi()))
            self._socket = wYp.ARz(hvC.Cdx(), hvC.ijn(),
                                                    self._configuration.encryption,
                                                    self._configuration.socket_timeout_seconds)
            self._writer = qlT(self._socket)
            self._writer.start()
            self._reader = KRy(self._socket, self, sWa)
            self._reader.start()
            jiT = self._transport_encoder.HLn(self._cluster.XKi().Cdx(),
                                                                  self._configuration.encryption)
            if len(jiT.YoI) > 0:
                self._writer.qbU(jiT.YoI)
        except:
            self._logger.info("Failed to Connect: " + str(self._cluster.XKi()))
            self._scheduler.nCJ(sWa, self, XRm.BWx)
            return
        self._scheduler.BVr(sWa, self, Xkt.LOZ)
        self._scheduler.MRX(self)
        self.LXl()
    def LXl(self):
        jiT = self._transport_encoder.GqZ(self._cluster.XKi().Cdx())
        sZK = self._configuration
        self._push_encoder.XoE(jiT.YoI, sZK.entitlement_token, sZK.session_type, sZK.user_agent, sZK.bwH)
        self._transport_encoder.Skw(jiT)
        self._write(jiT.jWm())
    def zkL(self):
        self.disconnect()
        if self._app_state == zHn.Jqp:
            return
        self._cluster.ULU(self._cluster.XKi())
        self._reconnected = True
        self.connect()
    def disconnect(self):
        if self._socket is not None:
            self._socket.close()
        if self._writer is not None:
            self._writer.SUb()
        if self._reader is not None:
            self._reader.SUb()
        self._socket = None
        self._writer = None
        self._reader = None
        self._scheduler.cancel()
        self.isf()
    def SFQ(self):
        self._app_state = zHn.Jqp
        self.disconnect()
    def isf(self):
        self._client_state.ZQg(NYb.xHp)
        self._session = -1
        self._session_received = False
    def MpD(self):
        if self._app_state != zHn.vsv:
            return
        self._logger.info("Call pause")
        self._app_state = zHn.nCc
        self.disconnect()
    def resume(self):
        if self._app_state != zHn.nCc:
            return
        self._logger.info("Call resume")
        self._app_state = zHn.vsv
        self.cLP()
        self.zkL()
    def subscribe(self, EMh, history):
        if EMh is None or len(EMh) == 0:
            return
        EMh = XRm.Xft(EMh)
        oeF = list(set(EMh) - set(self._subject_manager.Vsf()))
        if len(oeF) == 0:
            return
        self._subject_manager.IWC(oeF, history)
        if self._client_state.hid() == NYb.cDJ:
            self.pur(oeF)
    def pur(self, subjects_string):
        jiT = self._transport_encoder.GqZ(self._cluster.XKi().Cdx())
        for qxh in subjects_string:
            self.QBT(jiT, self._subject_manager.get_subject(qxh))
        self._transport_encoder.Skw(jiT)
        self._write(jiT.jWm())
    def _write(self, message):
        if self._writer is not None:
            self._writer.qbU(message)
            try:
                self._logger.debug(wPc.Uiv + message.decode('utf-8'))
            except UnicodeDecodeError:
                self._logger.debug(wPc.Uiv + str(message))
    def QBT(self, jiT, qxh):
        self._push_encoder.XOx(jiT.YoI, qxh, self._session)
    def unsubscribe(self, subjects_string):
        if subjects_string is None or len(subjects_string) == 0:
            return
        OeD = list(set(subjects_string) & set(self._subject_manager.Vsf()))
        if len(OeD) == 0:
            return
        FZV = self._subject_manager.dHb(OeD)
        if self._client_state.hid() == NYb.cDJ:
            self.IRX(FZV)
    def IRX(self, EMh):
        jiT = self._transport_encoder.GqZ(self._cluster.XKi().Cdx())
        for qxh in EMh:
            self._push_encoder.fkD(jiT.YoI, self._session, qxh)
        self._transport_encoder.Skw(jiT)
        self._write(jiT.jWm())
    def publish(self, message):
        if self._client_state.hid() != NYb.cDJ:
            self.ipX(MigratoryDataClient.NOTIFY_PUBLISH_FAILED, message)
        self.dDS(message)
    def dDS(self, message):
        Mwy = message.get_reply_to_subject()
        if Mwy is not None and XRm.VUV(
                Mwy) is True and self._subject_manager.JsP(Mwy) is False:
            self.subscribe([Mwy], 0)
        jiT = self._transport_encoder.GqZ(self._cluster.XKi().Cdx())
        self._push_encoder.Eye(jiT.YoI, message, self._session)
        self._transport_encoder.Skw(jiT)
        if self._max_message_size is not None and (len(jiT.YoI) - jiT.Kif) > self._max_message_size:
            self.ipX(MigratoryDataClient.NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED, message)
            return
        closure = message.get_closure()
        if closure is not None and len(closure) > 0:
            self._publish_closures.append(closure)
        self._write(jiT.jWm())
    def pIu(self):
        for closure in self._publish_closures:
            self._listener_notifier.oYE(
                wPc.YlF + " " + closure)
        self._publish_closures = []
    def ipX(self, notification, message):
        if message is not None and message.get_closure() is not None:
            self._listener_notifier.oYE(notification, message.get_closure())
    def XUo(self):
        jiT = self._transport_encoder.GqZ(self._cluster.XKi().Cdx())
        self._push_encoder.vAi(jiT.YoI, self._session)
        self._transport_encoder.Skw(jiT)
        if self._writer is not None:
            self._write(jiT.jWm())
    def nCJ(self, uuid, disconnect_reason, from_):
        if uuid == self.vxD():
            self._client_state.ZQg(NYb.xHp)
            self._loop.LKe(QPy.UTJ(uuid, disconnect_reason))
            self._logger.debug(
                wPc.sOi + str(self._current_connection_id) + str(from_))
    def uyq(self, disconnect_info):
        self._logger.error("[" + str(disconnect_info) + "] [" + str(self._cluster.XKi()) + "]")
        self._logger.info("Lost connection with the clust Member: " + str(self._cluster.XKi()))
        if self._session_received is False:
            self._servers_down_count += 1
            if self._is_server_down is False:
                if self._servers_down_count >= self._configuration.servers_down_before_notify:
                    self._is_server_down = True
                    self._listener_notifier.oYE(MigratoryDataClient.NOTIFY_SERVER_DOWN,
                                                         self._cluster.XKi().Inb())
                    self._logger.debug(wPc.QoC + str(disconnect_info))
    def cLP(self):
        self._is_server_down = False
        self._servers_down_count = 0
    def NOV(self):
        self._logger.info("Connected to the clust Member: " + str(self._cluster.XKi()))
        self.cLP()
        self._listener_notifier.oYE(MigratoryDataClient.NOTIFY_SERVER_UP,
                                             self._cluster.XKi().Inb())
        self._logger.debug(wPc.hSv + MigratoryDataClient.NOTIFY_SERVER_UP + str(
            self.vxD()))
    def Zxd(self):
        return self._reconnect_retries
    def wLb(self):
        self._reconnect_retries += 1
        return self._reconnect_retries
    def pIY(self, sWa):
        with self._lock:
            self._current_connection_id = sWa
    def vxD(self):
        with self._lock:
            return self._current_connection_id
    def iit(self, loop):
        self._loop = loop
    def maU(self):
        return self._loop
    def vMz(self):
        return self._app_state
class XcA:
    def __init__(self):
        self._connection = None
    def JoW(self, connection):
        self._connection = connection
    def on_message(self, message):
        self._connection._scheduler.BVr(self._connection.vxD(),
                                                                   self._connection, Xkt.zrx)
        VFw = message.VFw
        if message.operation == oWA.zmZ:
            self.hSz(VFw)
        elif message.operation == oWA.rUO:
            self.PGi(VFw, message)
        elif message.operation == oWA.LOZ:
            self.xgx(VFw)
        elif message.operation == oWA.CLIENT_PUBLISH_RESPONSE:
            self.yWM(VFw)
        elif message.operation == oWA.fEB:
            self.moI()
        elif message.operation == oWA.wiS:
            self.FNC(VFw)
        elif message.operation == oWA.dCD:
            self.UFA(VFw)
        else:
            self._connection._logger.warn("No existing operation for msg: " + str(message))
    def xgx(self, VFw):
        ltF = VFw.get(PsT.bCA)
        if ltF is not None:
            self._connection.NOV()
            self._connection._session = ltF
            self._connection._session_received = True
            self._connection._reconnect_retries = 0
            RVm = VFw.get(PsT.GVE)
            if RVm is not None and RVm == 1:
                self._connection._node_type = Ard.OkM
            if RVm is not None and RVm == 2:
                self._connection._node_type = Ard.HKO
            ffv = VFw.get(PsT.lEV)
            if ffv is not None:
                self._connection._scheduler.uFI(ffv)
                self._connection._scheduler.BVr(
                    self._connection.vxD(), self._connection, Xkt.zrx)
            self._connection._client_state.ZQg(NYb.cDJ)
            NKv = VFw.get(PsT.MWI)
            self.HKk(NKv)
            DNW = VFw.get(PsT.Wqe)
            if DNW is not None:
                self._connection._max_message_size = DNW
            EMh = self._connection._subject_manager.Vsf()
            if len(EMh) > 0:
                self._connection.pur(EMh)
    def hSz(self, VFw):
        pass
    def moI(self):
        pass
    def PGi(self, VFw, msg):
        qxh = VFw.get(PsT.SSa)
        sCn = self._connection._subject_manager.get_subject(qxh)
        if sCn is None:
            return
        NKv = VFw.get(PsT.MWI)
        self.HKk(NKv)
        glt = VFw.get(PsT.dBF)
        closure = VFw.get(PsT.MDF)
        retained = False
        Zfn = VFw.get(PsT.Mvk)
        if Zfn is not None and Zfn == 1:
            retained = True
        Lec = False
        gMM = VFw.get(PsT.oxp)
        if gMM is not None and gMM == 1:
            Lec = True
        if Lec == True:
            glt = self._connection._push_encoder.tKT(glt)
        irB = MessageType.UPDATE
        RIo = VFw.get(PsT.uWt)
        if RIo is not None:
            if RIo == oxm.SNAPSHOT:
                irB = MessageType.SNAPSHOT
            elif RIo == oxm.RECOVERED:
                irB = MessageType.RECOVERED
            elif RIo == oxm.HISTORICAL:
                irB = MessageType.HISTORICAL
        VXt = QoS.GUARANTEED
        OAL = VFw.get(PsT.Xxs)
        if OAL is not None and OAL == QoS.STANDARD:
            VXt = QoS.STANDARD
        if self._connection._node_type == Ard.OkM and VXt == QoS.GUARANTEED:
            message = asV(qxh, glt, closure, retained, irB, QoS.GUARANTEED,
                                                   VFw.get(PsT.rDh), Lec)
            CvH = VFw.get(PsT.qPC)
            wRp = VFw.get(PsT.HkI)
            message.ZFD(CvH)
            message.nnO(wRp)
            fBg = XRm.Xda(sCn, CvH, wRp, self._connection._listener_notifier,
                                             self._connection._logger)
            if fBg == QZW.EtN:
                self._connection._listener_notifier.neo(message)
                self._connection._logger.debug(wPc.qlo + str(message))
            elif fBg == QZW.KVJ:
                self._connection.nCJ(self._connection.vxD(),
                                           XRm.bhx, "seq_higher")
        elif self._connection._node_type == Ard.HKO and VXt == QoS.GUARANTEED:
            message = asV(qxh, glt, closure, retained, irB, QoS.GUARANTEED,
                                                   VFw.get(PsT.rDh), Lec)
            CvH = VFw.get(PsT.qPC)
            wRp = VFw.get(PsT.HkI)
            message.ZFD(CvH)
            message.nnO(wRp)
            fBg = XRm.aji(sCn, CvH, wRp, self._connection._listener_notifier,
                                             self._connection._logger)
            if fBg == QZW.EtN:
                self._connection._listener_notifier.neo(message)
                self._connection._logger.debug(wPc.qlo + str(message))
        else:
            message = asV(qxh, glt, closure, retained, irB, QoS.STANDARD,
                                                   VFw.get(PsT.rDh), Lec)
            self._connection._listener_notifier.neo(message)
            self._connection._logger.debug(wPc.qlo + str(message))
    def yWM(self, VFw):
        if VFw is None:
            return
        closure = VFw.get(PsT.MDF)
        YUz = VFw.get(PsT.KAY)
        if closure is not None and YUz is not None:
            status = MigratoryDataClient.NOTIFY_PUBLISH_FAILED
            if YUz == XRm.lFF:
                status = MigratoryDataClient.NOTIFY_PUBLISH_DENIED
            elif YUz == XRm.saS:
                status = MigratoryDataClient.NOTIFY_PUBLISH_OK
            self._connection._listener_notifier.oYE(status, closure)
            self._connection._logger.debug(
                wPc.rla + str(status) + str(closure))
            if self._connection._publish_closures.__contains__(closure):
                self._connection._publish_closures.remove(closure)
    def FNC(self, VFw):
        uZm = VFw.get(PsT.KAY)
        qxh = VFw.get(PsT.SSa)
        if uZm is not None and qxh is not None:
            eXo = True
            UdU = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if uZm == Snd.UZd:
                UdU = MigratoryDataClient.NOTIFY_SUBSCRIBE_ALLOW
                eXo = False
            elif uZm == Snd.eFU:
                UdU = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if eXo is True:
                self._connection._subject_manager.dHb([qxh])
            self._connection._listener_notifier.oYE(UdU, qxh)
            self._connection._logger.debug(wPc.Cqx + str(
                qxh + str(uZm) + str(UdU)))
    def UFA(self, VFw):
        qxh = VFw.get(PsT.SSa)
        status = VFw.get(PsT.uWt)
        self._connection._logger.info("Recovery Status for subj: " + str(qxh) + " is:" + str(status))
        if XRm.UDL == status:
            EMh = self._connection._subject_manager.Vsf()
            for s in EMh:
                sCn = self._connection._subject_manager.get_subject(s)
                cxN = sCn.GUr()
                if XRm.iTW == cxN or XRm.HOr == cxN or XRm.tZk == cxN:
                    sCn.vjU()
                else:
                    sCn.QfX()
        else:
            sCn = self._connection._subject_manager.get_subject(qxh)
            if sCn is not None:
                sCn.kzZ(status)
    def HKk(self, _received_cluster_token):
        if _received_cluster_token is not None:
            if self._connection._cluster_token is None:
                self._connection._cluster_token = _received_cluster_token
            else:
                if _received_cluster_token != self._connection._cluster_token:
                    self._connection._cluster_token = _received_cluster_token
                    self._connection._subject_manager.qmK()
import uuid
class hsd:
    HTTP = 0
    IWR = 1
class mPU:
    def __init__(self, session_type, user_agent):
        self.bwH = 6
        self.id = str(uuid.uuid4())
        self.session_type = session_type
        self.user_agent = user_agent + ", version:" + str(self.bwH)
        self.DEFAULT_KEEP_ALIVE_TIMEOUT = 30
        self.PING_INTERVAL = 900
        self.OPERATION_TIMEOUT_INTERVAL = 10
        self.reconnect_policy = MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF
        self.reconnect_time_interval = 20
        self.reconnect_max_delay = 360
        self.quick_reconnect_max_retries = 3
        self.quick_reconnect_initial_delay = 5
        self.servers_down_before_notify = 1
        self.entitlement_token = None
        self.encryption = False
        self.socket_timeout_seconds = 2
        self._subjects = {}
        self.trans_type = hsd.IWR
    def IWC(self, EMh, history):
        for qxh in EMh:
            self._subjects[qxh] = history
    def cfM(self, EMh):
        for qxh in EMh:
            try:
                del self._subjects[qxh]
            except KeyError:
                pass
    def get_subjects(self):
        return self._subjects
class IWe(sBj):
    def __init__(self, connection, AEu):
        self._connection = connection
        self._scheduler = AEu
    def LSS(self, NFc):
        if NFc.operation == nnZ.LOZ:
            self._connection.connect()
        elif NFc.operation == nnZ.zmZ:
            self._connection.subscribe(NFc.EMh, NFc.history)
        elif NFc.operation == nnZ.fEB:
            self._connection.unsubscribe(NFc.EMh)
        elif NFc.operation == nnZ.rUO:
            self._connection.publish(NFc.md_message)
        elif NFc.operation == nnZ.CYA:
            self._connection.YbJ().on_message(NFc.message)
        elif NFc.operation == nnZ.xHp:
            if NFc.connection_uuid == self._connection.vxD():
                self._connection.disconnect()
                self._connection.pIu()
                self._scheduler.nCJ(NFc.connection_uuid, self._connection,
                                          NFc.disconnect_reason)
        elif NFc.operation == nnZ.ZBr:
            self._connection.XUo()
            self._scheduler.MRX(self._connection)
        elif NFc.operation == nnZ.afK:
            self._connection.zkL()
        elif NFc.operation == nnZ.OSM:
            self._connection.SFQ()
        elif NFc.operation == nnZ.nCc:
            self._connection.MpD()
        elif NFc.operation == nnZ.juR:
            self._connection.resume()
        elif NFc.operation == nnZ.iDL:
            self._scheduler.BVr(self._connection.vxD(),
                                                           self._connection, Xkt.zrx)
import threading
import random
import time
class uOp(tNh):
    def __init__(self, configuration, client_state):
        self._keep_alive_timer_task = None
        self._reconnect_timer_task = None
        self._ping_operation_timer_task = None
        self._configuration = configuration
        self._client_state = client_state
        self._keep_alive_timeout = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
    def nCJ(self, sWa, connection, disconnect_info):
        if connection.vMz() != zHn.vsv:
            return
        EKE = connection.vxD()
        if EKE is None or EKE != sWa:
            return
        connection.pIY(None)
        connection.uyq(disconnect_info)
        rIy = connection.wLb()
        aUS = self.bFs(rIy, False)
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
        self._reconnect_timer_task = threading.Timer(aUS, self.rzi, [connection, disconnect_info])
        self._reconnect_timer_task.start()
    def rzi(self, connection, disconnect_info):
        connection.maU().LKe(QPy.lFD(disconnect_info))
    def MRX(self, connection):
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        self._ping_operation_timer_task = threading.Timer(self._configuration.PING_INTERVAL,
                                                          self.PKs, [connection])
        self._ping_operation_timer_task.start()
    def PKs(self, connection):
        connection.maU().LKe(QPy.Wdz())
    def cancel(self):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
    def BVr(self, sWa, connection, keep_alive):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        aUS = self._keep_alive_timeout
        if keep_alive == Xkt.LOZ:
            rIy = connection.Zxd()
            aUS = self.bFs(rIy, True)
        if aUS > 0:
            self._keep_alive_timer_task = threading.Timer(aUS,
                                                          self.XXj, [sWa, connection])
            self._keep_alive_timer_task.start()
    def XXj(self, uuid, connection):
        EKE = connection.vxD()
        if EKE is None or EKE != uuid:
            return
        self._client_state.ZQg(NYb.xHp)
        connection.maU().LKe(
            QPy.UTJ(uuid, XRm.acu))
    def uFI(self, value):
        self._keep_alive_timeout = value * 1.4
    def bFs(self, rIy, verify_timeout):
        aUS = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
        if rIy > 0:
            if rIy <= self._configuration.quick_reconnect_max_retries:
                aUS = (rIy * self._configuration.quick_reconnect_initial_delay) - int(
                    random.uniform(0, 1) * self._configuration.quick_reconnect_initial_delay)
            else:
                if self._configuration.reconnect_policy == MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF:
                    count = rIy - self._configuration.quick_reconnect_max_retries
                    aUS = int(min(self._configuration.reconnect_time_interval * pow(2, count) - int(
                        random.uniform(0, 1) * self._configuration.reconnect_time_interval * count),
                                      self._configuration.reconnect_max_delay))
                else:
                    aUS = self._configuration.reconnect_time_interval
            if verify_timeout and aUS < self._configuration.OPERATION_TIMEOUT_INTERVAL:
                aUS = self._configuration.OPERATION_TIMEOUT_INTERVAL
        return aUS
import sys
import threading
class Byj:
    def __init__(self):
        self._lock = threading.Lock()
        self._running = False
        self._configuration = None
        self._connection = None
        self._single_thread_event_loop = None
        self._listener_notifier = None
        self._servers = None
        self._migratory_data_listener = None
        self._client_state = iFm()
        self.MgJ = Bhs.ucE
        self.gMY = "MigratoryDataClient/v6.0 Python/" + str(sys.version)
        self._logger = AcC()
        self._configuration = mPU(self.MgJ, self.gMY)
    def ybN(self):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError("Error: connect() - already connected")
            if self._servers is None:
                raise RuntimeError(
                    "Error: connect() - no server to connect to; use set_servers() to specify one or more servers")
            if self._migratory_data_listener is None:
                raise RuntimeError(
                    "Error: connect() - no listener set; use set_listener() to specify a listener handler")
            self._running = True
            FfZ = icR(self._servers, self._configuration.encryption)
            self._listener_notifier = YfI(self._migratory_data_listener)
            self._listener_notifier.start()
            AEu = uOp(self._configuration, self._client_state)
            self._connection = Connection(self._configuration, self._listener_notifier, FfZ, AEu,
                                          self._client_state, self._logger)
            mcD = IWe(self._connection, AEu)
            self._single_thread_event_loop = Pkk(mcD, self._logger)
            self._connection.iit(self._single_thread_event_loop)
            self._single_thread_event_loop.LKe(QPy.chE())
            EMh = self._configuration.get_subjects()
            for NQe in EMh:
                self._single_thread_event_loop.LKe(
                    QPy.dDL([NQe], EMh[NQe]))
                self._logger.debug(wPc.eSc + str([NQe]))
            self._single_thread_event_loop.start()
        finally:
            self._lock.release()
    def CFc(self, _servers):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError("Error: set_servers() - already connected; use this method before connect()")
            if _servers is None:
                raise TypeError("Error: set_servers() - servers has None value")
            if len(_servers) == 0:
                raise ValueError("Error: set_servers() - The list of servers is empty")
            self._logger.info("Setting Servers to connect to: " + str(_servers))
            self._servers = _servers
        finally:
            self._lock.release()
    def hmD(self):
        self._lock.acquire()
        try:
            listener = self._migratory_data_listener
        finally:
            self._lock.release()
        return listener
    def STe(self, _listener):
        self._lock.acquire()
        try:
            if self._running is False:
                if _listener is None:
                    raise TypeError("Listener has None value")
                self._migratory_data_listener = _listener
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def Ukq(self, _log_listener, _log_level):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.yFI(_log_listener, _log_level)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def SFQ(self):
        self._lock.acquire()
        try:
            self._logger.info("Disposing")
            if self._running is False:
                return
            self._running = False
            if self._single_thread_event_loop is not None:
                self._single_thread_event_loop.LKe(QPy.DPM())
                self._logger.debug(wPc.GQQ)
                self._single_thread_event_loop.fqB()
                self._single_thread_event_loop = None
            if self._listener_notifier is not None:
                self._listener_notifier.SUb()
                self._listener_notifier = None
        finally:
            self._lock.release()
    def rkH(self, token):
        self._lock.acquire()
        try:
            if self._running is False:
                self._configuration.entitlement_token = token
                self._logger.info("Configuring Entitlement token: " + token)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def Qpk(self, _subjects, history):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            for qxh in _subjects:
                if qxh is None or len(qxh) == 0 or XRm.VUV(qxh) is False:
                    raise TypeError("Subscribe with invalid qxh: " + str(qxh))
            if history < 0:
                raise ValueError(
                    "Error: subscribeWithHistory() - the argument numberOfHistoricalMessages should be a positive number or zero!")
            self._logger.info("Subscribing to: " + str(_subjects))
            self._configuration.IWC(_subjects, history)
            if self._running is True:
                self._single_thread_event_loop.LKe(
                    QPy.dDL(_subjects, history))
                self._logger.debug(wPc.eSc + str(_subjects))
        finally:
            self._lock.release()
    def UDM(self, _subjects):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            for qxh in _subjects:
                if qxh is None or len(qxh) == 0 or XRm.VUV(qxh) is False:
                    raise TypeError("Unsubscribe with invalid qxh: " + str(qxh))
            self._logger.info("Unsubscribing from: " + str(_subjects))
            self._configuration.cfM(_subjects)
            if self._running is True:
                self._single_thread_event_loop.LKe(QPy.VYS(_subjects))
                self._logger.debug(wPc.Mhi + str(_subjects))
        finally:
            self._lock.release()
    def XMe(self, _message):
        self._lock.acquire()
        try:
            if self._running is True:
                qxh = _message.get_subject()
                ejx = _message.get_content()
                if qxh is None or len(qxh) == 0 or XRm.VUV(qxh) is False:
                    raise TypeError("Msg with invalid subj: " + str(qxh))
                if ejx is None:
                    raise TypeError("Msg with null content")
                self._single_thread_event_loop.LKe(QPy.tEa(_message))
                self._logger.debug(wPc.oYn + str(_message))
            else:
                raise RuntimeError("Error: publish() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def KoP(self, _encryption_bool):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.info("Configuring encryption to: " + str(_encryption_bool))
                self._configuration.encryption = _encryption_bool
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def IgL(self, nr):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Notify_after_reconnect_retries() - already connected; use this method before connect")
            if nr < 1:
                raise ValueError(
                    "Error: Notify_after_reconnect_retries() - invalid argument; expected a positive integer")
            self._configuration.servers_down_before_notify = nr
            self._logger.info(
                "Configuring the number of failed connection attempts before sending a notification: " + str(nr))
        finally:
            self._lock.release()
    def PqW(self):
        self._lock.acquire()
        try:
            return list(self._configuration.get_subjects().keys())
        finally:
            self._lock.release()
    def MpD(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls pause")
                self._logger.debug(wPc.TwE)
                self._single_thread_event_loop.LKe(QPy.Qkq())
            else:
                raise RuntimeError("Error: pause() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def LOM(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls resume")
                self._logger.debug(wPc.LmE)
                self._single_thread_event_loop.LKe(QPy.bUY())
            else:
                raise RuntimeError("Error: resume() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def qUU(self, nr):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_quick_reconnect_max_retries() - already connected; use this method before connect")
            if nr < 2:
                raise ValueError(
                    "Error: Set_quick_reconnect_max_retries() - invalid argument; expected an integer integer higher or equal to 2")
            self._configuration.quick_reconnect_max_retries = nr
            self._logger.info("Configuring quickReconnect max Retries to: " + str(nr))
        finally:
            self._lock.release()
    def Gyr(self, interval):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_quick_reconnect_initial_delay() - already connected; use this method before connect")
            if interval < 1:
                raise ValueError(
                    "Error: Set_quick_reconnect_initial_delay() - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.quick_initial_delay = interval
            self._logger.info("Configuring quickReconnectInitial delay to: " + str(interval))
        finally:
            self._lock.release()
    def QLn(self, _policy):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_policy - already connected; use this method before connect")
            if _policy or (
                            _policy != MigratoryDataClient.CONSTANT_WINDOW_BACKOFF and _policy != MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF):
                raise ValueError(
                    "Error: Set_reconnect_policy - invalid argument; expected MigratoryDataClient.CONSTANT_WINDOW_BACKOFF_ or MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF_")
            self._configuration.reconnect_policy = _policy
            self._logger.info("Configuring Reconnect Policy to: " + _policy)
        finally:
            self._lock.release()
    def IgW(self, interval):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_time_interval() - already connected; use this method before connect")
            if interval < 1:
                raise ValueError(
                    "Error: Set_reconnect_time_interval - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.reconnect_time_interval = interval
            self._logger.info("Configuring setReconnectTime interval  to: " + str(interval))
        finally:
            self._lock.release()
    def Yhu(self, delay):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_max_delay() - already connected; use this method before connect")
            if delay < 1:
                raise ValueError(
                    "Error: Set_reconnect_max_delay() - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.reconnect_max_delay = delay
            self._logger.info("Configuring setReconnectMax delay  to: " + str(delay))
        finally:
            self._lock.release()
    def eGX(self, type):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_transport() - already connected; use this method before connect")
            if type == MigratoryDataClient.TRANSPORT_HTTP:
                self._configuration.trans_type = hsd.HTTP
            self._logger.info("Configuring transport type to: " + type)
        finally:
            self._lock.release()
class MigratoryDataClient:
    NOTIFY_SERVER_UP = "NOTIFY_SERVER_UP"
    NOTIFY_SERVER_DOWN = "NOTIFY_SERVER_DOWN"
    NOTIFY_DATA_SYNC = "NOTIFY_DATA_SYNC"
    NOTIFY_DATA_RESYNC = "NOTIFY_DATA_RESYNC"
    NOTIFY_SUBSCRIBE_ALLOW = "NOTIFY_SUBSCRIBE_ALLOW"
    NOTIFY_SUBSCRIBE_DENY = "NOTIFY_SUBSCRIBE_DENY"
    NOTIFY_PUBLISH_OK = "NOTIFY_PUBLISH_OK"
    NOTIFY_PUBLISH_FAILED = "NOTIFY_PUBLISH_FAILED"
    NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED = "NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED"
    NOTIFY_PUBLISH_DENIED = "NOTIFY_PUBLISH_DENIED"
    CONSTANT_WINDOW_BACKOFF = "CONSTANT_WINDOW_BACKOFF"
    TRUNCATED_EXPONENTIAL_BACKOFF = "TRUNCATED_EXPONENTIAL_BACKOFF"
    TRANSPORT_HTTP = "TRANSPORT_HTTP"
    TRANSPORT_WEBSOCKET = "TRANSPORT_WEBSOCKET"
    def __init__(self):
        self._client_impl = Byj()
    def connect(self):
        self._client_impl.ybN()
    def disconnect(self):
        self._client_impl.SFQ()
    def set_listener(self, listener):
        if issubclass(type(listener), MigratoryDataListener) is False:
            raise TypeError("Argument for set_listener must be a subclass MigratoryDataListener")
        self._client_impl.STe(listener)
    def get_listener(self):
        return self._client_impl.hmD()
    def set_log_listener(self, log_listener, log_level):
        if issubclass(type(log_listener), MigratoryDataLogListener) is False:
            raise TypeError("First argument for set_log_listener must be a subclass MigratoryDataLogListener")
        if type(log_level) is not int:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        if log_level < 0 or log_level > 4:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        self._client_impl.Ukq(log_listener, log_level)
    def set_entitlement_token(self, entitlement_token):
        if type(entitlement_token) is not str:
            raise TypeError("Argument for set_entitlement_token must be of type string")
        self._client_impl.rkH(entitlement_token)
    def set_servers(self, servers):
        self._check_if_is_string_list(servers, "set_servers")
        self._client_impl.CFc(servers)
    def _check_if_is_string_list(self, string_list, method_name):
        if type(string_list) is not list:
            raise TypeError("First argument for " + method_name + " must be a list of strings")
        for TYE in string_list:
            if type(TYE) is not str:
                raise TypeError("First argument for " + method_name + " must be a list of strings")
    def subscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "subscribe")
        self._client_impl.Qpk(subject_list, 0)
    def subscribe_with_history(self, subject_list, number_of_historical_messages):
        self._check_if_is_string_list(subject_list, "subscribe_with_history")
        if type(number_of_historical_messages) is not int:
            raise TypeError("Second argument for subscribe_with_history must be of type int")
        self._client_impl.Qpk(subject_list, number_of_historical_messages)
    def unsubscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "unsubscribe")
        self._client_impl.UDM(subject_list)
    def publish(self, message):
        if type(message) is not MigratoryDataMessage:
            raise TypeError("Argument for publish must be of type MigratoryDataMessage")
        self._client_impl.XMe(message)
    def set_encryption(self, encryption_bool):
        if type(encryption_bool) is not bool:
            raise TypeError("Argument for set_encryption must be of type bool")
        self._client_impl.KoP(encryption_bool)
    def get_subjects(self):
        return self._client_impl.PqW()
    def pause(self):
        self._client_impl.MpD()
    def resume(self):
        self._client_impl.LOM()
    def notify_after_failed_connection_attempts(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for notify_after_failed_connection_attempts must be of type int")
        self._client_impl.IgL(retries_number)
    def set_quick_reconnect_max_retries(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for set_quick_reconnect_max_retries must be of type int")
        self._client_impl.qUU(retries_number)
    def set_quick_reconnect_initial_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_quick_reconnect_initial_delay must be of type int")
        self._client_impl.Gyr(seconds)
    def set_reconnect_policy(self, policy):
        if type(policy) is not str:
            raise TypeError("Argument for set_reconnect_policy must be of type string")
        self._client_impl.QLn(policy)
    def set_reconnect_time_interval(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_time_interval must be of type int")
        self._client_impl.IgW(seconds)
    def set_reconnect_max_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_max_delay must be of type int")
        self._client_impl.Yhu(seconds)
    def set_transport(self, transport_type):
        if transport_type != MigratoryDataClient.TRANSPORT_HTTP and transport_type != MigratoryDataClient.TRANSPORT_WEBSOCKET:
            raise TypeError(
                "Argument for set_transport must be MigratoryDataClient.TRANSPORT_WEBSOCKET or MigratoryDataClient.TRANSPORT_HTTP")
        self._client_impl.eGX(transport_type)
