import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
