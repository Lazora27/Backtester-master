import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'AdaptiveATR': 1.0
        })
    )
