import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HistoricalATR': 1.0
        })
    )
