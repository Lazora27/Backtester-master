import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
