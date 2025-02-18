import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und GannSquares
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'GannSquares': 1.0
        })
    )
