import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
