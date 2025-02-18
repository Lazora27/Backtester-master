import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HighLowIndex': 1.0
        })
    )
