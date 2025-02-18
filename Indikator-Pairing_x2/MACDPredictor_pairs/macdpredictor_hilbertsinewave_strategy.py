import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HilbertSinewave': 1.0
        })
    )
