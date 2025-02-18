import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MarketBalance': 1.0
        })
    )
