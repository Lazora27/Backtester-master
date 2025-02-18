import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
