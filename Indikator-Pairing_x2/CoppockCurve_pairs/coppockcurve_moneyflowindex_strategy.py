import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
