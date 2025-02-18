import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
