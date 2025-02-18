import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
