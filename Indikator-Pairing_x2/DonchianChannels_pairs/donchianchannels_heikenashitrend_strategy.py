import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
