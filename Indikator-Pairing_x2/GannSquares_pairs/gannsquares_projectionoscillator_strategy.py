import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
