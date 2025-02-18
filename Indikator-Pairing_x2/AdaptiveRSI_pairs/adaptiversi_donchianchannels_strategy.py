import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'DonchianChannels': 1.0
        })
    )
