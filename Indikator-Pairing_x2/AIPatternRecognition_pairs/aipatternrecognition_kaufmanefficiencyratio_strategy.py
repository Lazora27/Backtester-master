import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_KaufmanEfficiencyRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und KaufmanEfficiencyRatio
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'KaufmanEfficiencyRatio': 1.0
        })
    )
