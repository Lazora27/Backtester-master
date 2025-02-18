import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BradleySiderograph': 1.0
        })
    )
