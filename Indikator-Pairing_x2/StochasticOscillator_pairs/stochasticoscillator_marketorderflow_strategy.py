import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
