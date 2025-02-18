import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
