import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
