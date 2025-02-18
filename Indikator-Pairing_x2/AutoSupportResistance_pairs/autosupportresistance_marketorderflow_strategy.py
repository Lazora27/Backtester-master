import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
