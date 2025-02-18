import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
