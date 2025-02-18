import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
