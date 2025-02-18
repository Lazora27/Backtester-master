import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
