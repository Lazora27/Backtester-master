import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AroonIndicator': 1.0
        })
    )
