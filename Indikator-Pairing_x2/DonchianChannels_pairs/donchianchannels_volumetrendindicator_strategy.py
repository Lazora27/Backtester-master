import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
