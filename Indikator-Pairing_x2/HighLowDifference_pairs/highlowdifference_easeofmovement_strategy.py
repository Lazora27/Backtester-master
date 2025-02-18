import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'EaseOfMovement': 1.0
        })
    )
