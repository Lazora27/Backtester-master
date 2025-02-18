import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
