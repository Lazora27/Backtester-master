import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'DonchianChannels': 1.0
        })
    )
