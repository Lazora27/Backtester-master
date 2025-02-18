import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TimeCycle': 1.0
        })
    )
