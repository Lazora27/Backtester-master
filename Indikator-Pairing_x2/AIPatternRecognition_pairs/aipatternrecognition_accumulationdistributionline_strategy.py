import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
