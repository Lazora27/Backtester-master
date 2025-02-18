import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BradleySiderograph': 1.0
        })
    )
