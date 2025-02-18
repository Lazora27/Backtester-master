import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
