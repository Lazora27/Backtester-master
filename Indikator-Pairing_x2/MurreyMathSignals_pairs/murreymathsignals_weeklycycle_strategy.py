import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'WeeklyCycle': 1.0
        })
    )
