import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'PutCallRatio': 1.0
        })
    )
