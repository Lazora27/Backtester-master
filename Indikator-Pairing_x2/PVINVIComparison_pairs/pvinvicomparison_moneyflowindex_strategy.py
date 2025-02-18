import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
