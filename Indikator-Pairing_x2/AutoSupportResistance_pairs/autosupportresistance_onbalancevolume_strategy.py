import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
