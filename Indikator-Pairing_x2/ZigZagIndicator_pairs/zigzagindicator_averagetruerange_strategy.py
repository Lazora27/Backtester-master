import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
