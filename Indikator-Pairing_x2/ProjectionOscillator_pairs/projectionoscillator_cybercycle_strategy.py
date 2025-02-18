import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'CyberCycle': 1.0
        })
    )
