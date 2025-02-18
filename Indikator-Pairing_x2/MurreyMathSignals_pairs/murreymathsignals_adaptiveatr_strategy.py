import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AdaptiveATR': 1.0
        })
    )
