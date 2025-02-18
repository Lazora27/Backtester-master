import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TrendCycles': 1.0
        })
    )
