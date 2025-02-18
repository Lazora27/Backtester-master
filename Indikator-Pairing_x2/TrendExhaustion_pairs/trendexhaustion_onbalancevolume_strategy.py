import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
