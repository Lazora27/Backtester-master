import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'FisherSignals': 1.0
        })
    )
