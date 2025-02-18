import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
