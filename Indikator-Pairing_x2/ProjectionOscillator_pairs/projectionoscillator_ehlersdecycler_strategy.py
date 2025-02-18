import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
