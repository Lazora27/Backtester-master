import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MACDHistogram': 1.0
        })
    )
