import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
