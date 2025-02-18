import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TickActivityIndex': 1.0
        })
    )
