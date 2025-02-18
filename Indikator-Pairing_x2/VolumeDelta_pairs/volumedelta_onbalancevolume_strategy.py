import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
