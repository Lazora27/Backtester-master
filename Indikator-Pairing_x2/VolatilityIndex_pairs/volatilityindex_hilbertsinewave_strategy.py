import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
