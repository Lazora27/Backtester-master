import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'WeightedCycle': 1.0
        })
    )
