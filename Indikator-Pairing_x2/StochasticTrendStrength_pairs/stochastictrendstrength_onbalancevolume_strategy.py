import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
