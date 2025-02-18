import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'DonchianChannels': 1.0
        })
    )
