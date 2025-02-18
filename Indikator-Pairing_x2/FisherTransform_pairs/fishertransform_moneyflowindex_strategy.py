import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
