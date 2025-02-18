import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
