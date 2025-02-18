import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
