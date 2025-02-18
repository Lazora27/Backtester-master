import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'GannSquareReversal': 1.0
        })
    )
