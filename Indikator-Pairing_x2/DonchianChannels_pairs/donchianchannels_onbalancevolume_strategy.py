import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
