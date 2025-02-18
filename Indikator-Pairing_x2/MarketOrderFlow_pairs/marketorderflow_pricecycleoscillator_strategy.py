import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
