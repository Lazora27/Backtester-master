import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
