import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
