import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'SmoothedCycle': 1.0
        })
    )
