import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
