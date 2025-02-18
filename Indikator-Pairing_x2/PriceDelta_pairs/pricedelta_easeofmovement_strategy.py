import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'EaseOfMovement': 1.0
        })
    )
