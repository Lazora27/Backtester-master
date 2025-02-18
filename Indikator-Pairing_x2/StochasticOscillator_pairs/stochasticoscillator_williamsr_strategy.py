import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'WilliamsR': 1.0
        })
    )
