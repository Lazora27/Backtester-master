import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'KeltnerChannels': 1.0
        })
    )
