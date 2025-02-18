import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
