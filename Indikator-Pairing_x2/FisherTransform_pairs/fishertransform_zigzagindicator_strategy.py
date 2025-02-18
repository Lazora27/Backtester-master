import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
