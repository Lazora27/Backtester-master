import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'SmoothedCycle': 1.0
        })
    )
