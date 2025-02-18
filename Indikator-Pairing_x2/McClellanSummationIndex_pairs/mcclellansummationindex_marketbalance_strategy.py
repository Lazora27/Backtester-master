import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
