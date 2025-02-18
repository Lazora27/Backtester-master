import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BalanceMomentum': 1.0
        })
    )
