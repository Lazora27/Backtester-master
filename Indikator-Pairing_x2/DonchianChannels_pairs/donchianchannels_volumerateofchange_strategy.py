import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
