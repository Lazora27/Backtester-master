import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TickActivityIndex': 1.0
        })
    )
