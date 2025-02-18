import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CVIRatio
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CVIRatio': 1.0
        })
    )
