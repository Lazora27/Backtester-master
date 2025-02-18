import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
