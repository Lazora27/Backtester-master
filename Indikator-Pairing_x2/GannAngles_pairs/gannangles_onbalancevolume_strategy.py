import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
