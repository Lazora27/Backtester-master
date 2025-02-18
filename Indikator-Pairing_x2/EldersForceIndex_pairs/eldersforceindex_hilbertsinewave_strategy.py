import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
