import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
