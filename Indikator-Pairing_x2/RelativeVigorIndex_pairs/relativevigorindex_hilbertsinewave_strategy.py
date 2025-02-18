import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
