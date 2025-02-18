import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PutCallRatio': 1.0
        })
    )
