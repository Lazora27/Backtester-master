import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
