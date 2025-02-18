import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
