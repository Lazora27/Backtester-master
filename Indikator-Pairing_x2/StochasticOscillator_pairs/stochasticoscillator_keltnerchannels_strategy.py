import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
