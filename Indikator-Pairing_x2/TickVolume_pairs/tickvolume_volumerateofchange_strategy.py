import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
