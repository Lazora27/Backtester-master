import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und GannSquares
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'GannSquares': 1.0
        })
    )
