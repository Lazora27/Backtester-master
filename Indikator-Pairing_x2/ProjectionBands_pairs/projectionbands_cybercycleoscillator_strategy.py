import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
