import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
