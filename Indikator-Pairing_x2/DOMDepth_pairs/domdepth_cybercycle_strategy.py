import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und CyberCycle
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'CyberCycle': 1.0
        })
    )
