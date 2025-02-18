import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
