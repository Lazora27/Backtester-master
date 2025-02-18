import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'IchimokuCloud': 1.0
        })
    )
