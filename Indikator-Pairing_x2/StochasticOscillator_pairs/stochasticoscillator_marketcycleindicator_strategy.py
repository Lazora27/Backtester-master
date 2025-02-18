import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
