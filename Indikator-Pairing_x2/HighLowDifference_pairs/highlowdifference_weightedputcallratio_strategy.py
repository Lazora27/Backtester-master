import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
