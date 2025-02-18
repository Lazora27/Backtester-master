import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
