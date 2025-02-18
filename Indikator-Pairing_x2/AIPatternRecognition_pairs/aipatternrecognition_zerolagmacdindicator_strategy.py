import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ZeroLagMACDIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ZeroLagMACDIndicator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ZeroLagMACDIndicator': 1.0
        })
    )
