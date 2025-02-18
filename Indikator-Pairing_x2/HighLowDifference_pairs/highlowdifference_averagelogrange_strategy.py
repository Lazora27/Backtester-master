import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AverageLogRange': 1.0
        })
    )
