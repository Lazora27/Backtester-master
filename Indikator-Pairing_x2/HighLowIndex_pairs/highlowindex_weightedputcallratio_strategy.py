import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
