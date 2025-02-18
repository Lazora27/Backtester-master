import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
