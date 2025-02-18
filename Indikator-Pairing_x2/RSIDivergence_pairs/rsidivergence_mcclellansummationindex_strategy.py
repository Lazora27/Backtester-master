import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
