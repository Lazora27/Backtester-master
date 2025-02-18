import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
