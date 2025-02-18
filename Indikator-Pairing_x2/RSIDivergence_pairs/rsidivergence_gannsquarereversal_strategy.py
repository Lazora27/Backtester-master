import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'GannSquareReversal': 1.0
        })
    )
