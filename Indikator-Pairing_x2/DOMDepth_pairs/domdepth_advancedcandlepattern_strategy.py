import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
