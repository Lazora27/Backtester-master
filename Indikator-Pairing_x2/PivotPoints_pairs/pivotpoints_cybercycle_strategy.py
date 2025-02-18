import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und CyberCycle
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'CyberCycle': 1.0
        })
    )
