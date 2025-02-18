import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AIPatternRecognition_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AIPatternRecognition
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AIPatternRecognition': 1.0
        })
    )
