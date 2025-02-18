import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'HilbertSinewave': 1.0
        })
    )
