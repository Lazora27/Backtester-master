import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
