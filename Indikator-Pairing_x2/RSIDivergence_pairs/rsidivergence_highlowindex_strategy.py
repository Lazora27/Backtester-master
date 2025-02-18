import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HighLowIndex': 1.0
        })
    )
