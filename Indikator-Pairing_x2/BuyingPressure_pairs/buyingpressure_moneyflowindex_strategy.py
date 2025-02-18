import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
