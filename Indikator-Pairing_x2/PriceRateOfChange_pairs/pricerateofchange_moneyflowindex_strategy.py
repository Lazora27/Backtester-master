import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
