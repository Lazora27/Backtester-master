import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
