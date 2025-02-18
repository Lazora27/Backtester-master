import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
