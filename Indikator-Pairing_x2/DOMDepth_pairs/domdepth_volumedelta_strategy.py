import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolumeDelta': 1.0
        })
    )
