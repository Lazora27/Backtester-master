import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ChandeMomentumOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ChandeMomentumOscillator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ChandeMomentumOscillator': 1.0
        })
    )
