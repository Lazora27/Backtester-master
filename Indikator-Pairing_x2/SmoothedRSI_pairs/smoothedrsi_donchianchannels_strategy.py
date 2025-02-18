import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DonchianChannels': 1.0
        })
    )
