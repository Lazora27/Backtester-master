import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
