import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'KeltnerChannels': 1.0
        })
    )
