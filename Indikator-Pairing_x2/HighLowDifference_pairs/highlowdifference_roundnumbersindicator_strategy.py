import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
