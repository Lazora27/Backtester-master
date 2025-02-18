import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedVolatilityIndicator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedVolatilityIndicator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'SmoothedVolatilityIndicator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
