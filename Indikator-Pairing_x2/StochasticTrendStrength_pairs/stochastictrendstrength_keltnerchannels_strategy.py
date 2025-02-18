import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'KeltnerChannels': 1.0
        })
    )
