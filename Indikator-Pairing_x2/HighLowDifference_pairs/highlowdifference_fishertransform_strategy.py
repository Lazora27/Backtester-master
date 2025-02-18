import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FisherTransform
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FisherTransform': 1.0
        })
    )
