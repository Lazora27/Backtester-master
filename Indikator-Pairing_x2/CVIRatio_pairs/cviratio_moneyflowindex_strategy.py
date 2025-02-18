import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
