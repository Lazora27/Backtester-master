import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
