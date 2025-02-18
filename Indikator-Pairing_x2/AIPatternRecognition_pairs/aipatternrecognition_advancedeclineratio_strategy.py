import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AdvanceDeclineRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AdvanceDeclineRatio
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AdvanceDeclineRatio': 1.0
        })
    )
