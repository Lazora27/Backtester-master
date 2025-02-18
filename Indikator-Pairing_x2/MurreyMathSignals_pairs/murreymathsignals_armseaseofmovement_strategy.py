import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ArmsEaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ArmsEaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ArmsEaseOfMovement': 1.0
        })
    )
