import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HilbertSinewave': 1.0
        })
    )
