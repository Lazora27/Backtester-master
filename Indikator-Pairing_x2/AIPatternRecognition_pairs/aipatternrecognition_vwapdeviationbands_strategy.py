import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
