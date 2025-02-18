import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
