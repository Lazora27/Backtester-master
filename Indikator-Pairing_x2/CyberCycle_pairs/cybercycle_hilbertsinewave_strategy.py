import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'HilbertSinewave': 1.0
        })
    )
