import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
