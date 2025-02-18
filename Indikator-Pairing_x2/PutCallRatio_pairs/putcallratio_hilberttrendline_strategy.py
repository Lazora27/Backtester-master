import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HilbertTrendline': 1.0
        })
    )
