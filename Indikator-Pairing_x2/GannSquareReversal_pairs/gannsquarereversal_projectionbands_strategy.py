import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ProjectionBands': 1.0
        })
    )
