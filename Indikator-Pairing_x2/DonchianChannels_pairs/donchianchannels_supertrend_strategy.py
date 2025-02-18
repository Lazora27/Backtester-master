import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SuperTrend
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SuperTrend': 1.0
        })
    )
