import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
