import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AverageLogRange': 1.0
        })
    )
