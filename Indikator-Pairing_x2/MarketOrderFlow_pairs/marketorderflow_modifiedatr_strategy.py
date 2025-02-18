import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ModifiedATR': 1.0
        })
    )
