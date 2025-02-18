import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'DPOCycles': 1.0
        })
    )
