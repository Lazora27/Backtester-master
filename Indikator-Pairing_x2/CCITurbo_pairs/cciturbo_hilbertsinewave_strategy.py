import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'HilbertSinewave': 1.0
        })
    )
