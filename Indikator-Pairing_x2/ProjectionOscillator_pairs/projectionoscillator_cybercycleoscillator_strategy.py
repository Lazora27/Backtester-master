import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
