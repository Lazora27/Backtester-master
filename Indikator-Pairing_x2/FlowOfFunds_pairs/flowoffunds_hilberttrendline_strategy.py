import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'HilbertTrendline': 1.0
        })
    )
