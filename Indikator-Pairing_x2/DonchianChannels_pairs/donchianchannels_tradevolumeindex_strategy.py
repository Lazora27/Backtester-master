import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
