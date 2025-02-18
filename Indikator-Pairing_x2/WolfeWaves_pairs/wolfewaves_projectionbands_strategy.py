import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ProjectionBands': 1.0
        })
    )
