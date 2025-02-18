import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
