import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
