import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
