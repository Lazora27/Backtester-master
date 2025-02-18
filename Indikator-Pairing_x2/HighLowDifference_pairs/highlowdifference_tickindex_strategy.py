import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TickIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TickIndex': 1.0
        })
    )
