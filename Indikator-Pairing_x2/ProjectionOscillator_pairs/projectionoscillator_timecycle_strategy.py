import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
