import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
