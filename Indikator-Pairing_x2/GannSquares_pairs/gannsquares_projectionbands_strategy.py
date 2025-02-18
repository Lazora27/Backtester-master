import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ProjectionBands': 1.0
        })
    )
