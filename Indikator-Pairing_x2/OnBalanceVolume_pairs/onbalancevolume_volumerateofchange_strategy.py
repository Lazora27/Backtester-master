import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
