import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AroonIndicator': 1.0
        })
    )
