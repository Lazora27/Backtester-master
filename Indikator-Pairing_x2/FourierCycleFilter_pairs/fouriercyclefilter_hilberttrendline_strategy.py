import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'HilbertTrendline': 1.0
        })
    )
