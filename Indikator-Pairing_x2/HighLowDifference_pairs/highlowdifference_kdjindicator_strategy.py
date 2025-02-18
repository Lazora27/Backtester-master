import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'KDJIndicator': 1.0
        })
    )
