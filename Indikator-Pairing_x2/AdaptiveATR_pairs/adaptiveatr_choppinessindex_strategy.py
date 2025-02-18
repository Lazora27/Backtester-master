import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
