import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolatilityIndex': 1.0
        })
    )
