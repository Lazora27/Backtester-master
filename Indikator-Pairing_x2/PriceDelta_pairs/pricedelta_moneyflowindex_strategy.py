import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
