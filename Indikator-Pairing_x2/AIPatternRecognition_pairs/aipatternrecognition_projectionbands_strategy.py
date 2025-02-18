import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ProjectionBands': 1.0
        })
    )
