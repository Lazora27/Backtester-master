import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VortexIndicator': 1.0
        })
    )
