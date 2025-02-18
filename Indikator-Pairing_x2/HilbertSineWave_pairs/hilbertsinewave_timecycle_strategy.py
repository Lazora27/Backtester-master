import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'TimeCycle': 1.0
        })
    )
