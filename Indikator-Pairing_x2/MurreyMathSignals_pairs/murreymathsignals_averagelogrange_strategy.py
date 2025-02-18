import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AverageLogRange': 1.0
        })
    )
