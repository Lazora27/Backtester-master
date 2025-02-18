import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
