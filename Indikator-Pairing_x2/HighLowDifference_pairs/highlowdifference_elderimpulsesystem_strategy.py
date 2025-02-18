import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
