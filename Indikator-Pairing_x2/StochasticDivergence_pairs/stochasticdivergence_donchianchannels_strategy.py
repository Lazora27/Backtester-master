import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DonchianChannels': 1.0
        })
    )
