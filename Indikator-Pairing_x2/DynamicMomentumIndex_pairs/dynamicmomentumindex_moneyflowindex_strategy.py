import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
