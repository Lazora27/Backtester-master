import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'DonchianChannels': 1.0
        })
    )
