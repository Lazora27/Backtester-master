import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und MassIndex
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'MassIndex': 1.0
        })
    )
