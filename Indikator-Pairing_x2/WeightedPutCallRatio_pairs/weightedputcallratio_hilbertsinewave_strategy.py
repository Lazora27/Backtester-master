import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'HilbertSinewave': 1.0
        })
    )
