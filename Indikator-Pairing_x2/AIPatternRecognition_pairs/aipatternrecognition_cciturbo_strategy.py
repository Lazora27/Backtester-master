import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CCITurbo': 1.0
        })
    )
