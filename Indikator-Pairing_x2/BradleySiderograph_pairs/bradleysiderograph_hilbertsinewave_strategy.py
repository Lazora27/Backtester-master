import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'HilbertSinewave': 1.0
        })
    )
