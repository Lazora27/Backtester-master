import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AdaptiveATR': 1.0
        })
    )
