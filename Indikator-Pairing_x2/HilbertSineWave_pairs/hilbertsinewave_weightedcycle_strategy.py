import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'WeightedCycle': 1.0
        })
    )
