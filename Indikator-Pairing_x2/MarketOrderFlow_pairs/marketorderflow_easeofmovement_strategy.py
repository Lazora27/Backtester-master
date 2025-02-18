import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'EaseOfMovement': 1.0
        })
    )
