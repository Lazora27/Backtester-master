import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
