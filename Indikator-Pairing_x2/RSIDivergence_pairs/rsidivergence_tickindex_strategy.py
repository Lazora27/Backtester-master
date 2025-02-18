import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TickIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TickIndex': 1.0
        })
    )
