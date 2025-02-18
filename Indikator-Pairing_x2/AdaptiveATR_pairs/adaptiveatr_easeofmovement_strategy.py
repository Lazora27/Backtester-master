import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'EaseOfMovement': 1.0
        })
    )
