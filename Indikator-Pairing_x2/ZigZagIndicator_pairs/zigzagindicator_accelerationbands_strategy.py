import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
