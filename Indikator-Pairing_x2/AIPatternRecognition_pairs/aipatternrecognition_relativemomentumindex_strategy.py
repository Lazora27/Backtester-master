import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
