import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedVolatilityIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedVolatilityIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'NormalizedVolatilityIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
