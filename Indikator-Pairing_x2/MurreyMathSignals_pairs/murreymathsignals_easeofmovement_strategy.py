import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'EaseOfMovement': 1.0
        })
    )
