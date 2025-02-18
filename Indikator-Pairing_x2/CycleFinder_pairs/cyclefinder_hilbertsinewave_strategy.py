import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'HilbertSinewave': 1.0
        })
    )
