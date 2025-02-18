import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
