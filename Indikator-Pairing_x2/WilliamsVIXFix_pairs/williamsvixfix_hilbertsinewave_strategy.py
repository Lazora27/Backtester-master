import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HilbertSinewave': 1.0
        })
    )
