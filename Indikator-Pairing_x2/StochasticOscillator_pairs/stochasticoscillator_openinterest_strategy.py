import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
