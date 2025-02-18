import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
