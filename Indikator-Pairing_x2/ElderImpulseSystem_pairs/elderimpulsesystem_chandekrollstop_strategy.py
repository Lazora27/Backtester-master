import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
