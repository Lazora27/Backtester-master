import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
