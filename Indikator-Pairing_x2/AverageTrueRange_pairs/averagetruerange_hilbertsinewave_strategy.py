import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HilbertSinewave': 1.0
        })
    )
