import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
