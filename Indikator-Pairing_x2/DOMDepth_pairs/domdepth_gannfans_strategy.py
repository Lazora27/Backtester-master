import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und GannFans
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'GannFans': 1.0
        })
    )
