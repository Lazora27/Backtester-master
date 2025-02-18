import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DonchianChannels': 1.0
        })
    )
