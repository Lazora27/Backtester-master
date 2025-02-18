import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
