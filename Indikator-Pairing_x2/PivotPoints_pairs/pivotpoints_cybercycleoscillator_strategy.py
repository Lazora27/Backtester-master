import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
