import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
