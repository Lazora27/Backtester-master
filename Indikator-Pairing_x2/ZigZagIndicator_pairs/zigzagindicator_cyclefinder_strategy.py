import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
