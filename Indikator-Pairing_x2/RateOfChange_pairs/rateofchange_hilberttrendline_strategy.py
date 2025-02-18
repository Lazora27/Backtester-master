import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HilbertTrendline': 1.0
        })
    )
