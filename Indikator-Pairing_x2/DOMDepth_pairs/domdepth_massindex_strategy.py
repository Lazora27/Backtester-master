import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MassIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MassIndex': 1.0
        })
    )
