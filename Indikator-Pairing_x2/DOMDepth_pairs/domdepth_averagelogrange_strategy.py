import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AverageLogRange': 1.0
        })
    )
