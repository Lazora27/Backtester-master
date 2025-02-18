import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SeasonalStrength': 1.0
        })
    )
