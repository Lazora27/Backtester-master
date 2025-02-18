import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MACDPredictor': 1.0
        })
    )
