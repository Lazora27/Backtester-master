import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SmoothedRSI': 1.0
        })
    )
