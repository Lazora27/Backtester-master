import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
