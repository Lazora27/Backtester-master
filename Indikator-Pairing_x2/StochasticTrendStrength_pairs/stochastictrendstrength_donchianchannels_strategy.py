import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'DonchianChannels': 1.0
        })
    )
