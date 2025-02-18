import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MarketBalance': 1.0
        })
    )
