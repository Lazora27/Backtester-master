import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
