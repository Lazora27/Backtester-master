import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
