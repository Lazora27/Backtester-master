import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
