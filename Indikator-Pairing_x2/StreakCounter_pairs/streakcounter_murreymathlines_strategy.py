import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MurreyMathLines': 1.0
        })
    )
