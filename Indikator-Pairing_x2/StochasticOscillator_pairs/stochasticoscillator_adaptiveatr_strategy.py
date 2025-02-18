import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'AdaptiveATR': 1.0
        })
    )
