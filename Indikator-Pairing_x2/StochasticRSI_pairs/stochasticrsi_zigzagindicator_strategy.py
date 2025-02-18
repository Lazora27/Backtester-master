import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
