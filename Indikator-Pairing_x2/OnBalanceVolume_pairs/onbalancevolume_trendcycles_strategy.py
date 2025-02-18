import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und TrendCycles
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'TrendCycles': 1.0
        })
    )
