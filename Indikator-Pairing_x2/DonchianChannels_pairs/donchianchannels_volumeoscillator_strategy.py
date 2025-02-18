import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'VolumeOscillator': 1.0
        })
    )
