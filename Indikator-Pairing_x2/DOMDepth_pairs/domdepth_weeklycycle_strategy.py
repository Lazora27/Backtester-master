import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'WeeklyCycle': 1.0
        })
    )
