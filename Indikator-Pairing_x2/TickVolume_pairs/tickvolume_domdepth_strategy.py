import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DOMDepth
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DOMDepth': 1.0
        })
    )
