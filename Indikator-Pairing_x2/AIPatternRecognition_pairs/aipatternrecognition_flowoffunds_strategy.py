import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'FlowOfFunds': 1.0
        })
    )
