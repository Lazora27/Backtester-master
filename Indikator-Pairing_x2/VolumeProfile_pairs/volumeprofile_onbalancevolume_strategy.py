import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
