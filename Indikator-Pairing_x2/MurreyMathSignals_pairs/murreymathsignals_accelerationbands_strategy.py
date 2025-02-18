import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AccelerationBands': 1.0
        })
    )
