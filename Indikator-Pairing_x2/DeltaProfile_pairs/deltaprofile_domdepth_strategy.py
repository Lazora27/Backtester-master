import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DOMDepth
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DOMDepth': 1.0
        })
    )
