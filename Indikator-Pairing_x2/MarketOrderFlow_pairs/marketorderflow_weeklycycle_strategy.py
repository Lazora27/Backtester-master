import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'WeeklyCycle': 1.0
        })
    )
