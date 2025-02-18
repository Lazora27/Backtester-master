import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'VWAPBands': 1.0
        })
    )
