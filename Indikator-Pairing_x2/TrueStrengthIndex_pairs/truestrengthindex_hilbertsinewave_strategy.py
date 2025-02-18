import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
