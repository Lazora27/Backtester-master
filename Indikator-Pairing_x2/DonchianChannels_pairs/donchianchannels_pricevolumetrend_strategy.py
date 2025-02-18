import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
