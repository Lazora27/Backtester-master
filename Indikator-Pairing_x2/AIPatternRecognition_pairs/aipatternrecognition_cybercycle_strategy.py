import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CyberCycle': 1.0
        })
    )
