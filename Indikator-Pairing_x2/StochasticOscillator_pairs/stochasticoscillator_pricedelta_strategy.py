import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'PriceDelta': 1.0
        })
    )
