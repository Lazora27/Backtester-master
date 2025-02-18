import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
