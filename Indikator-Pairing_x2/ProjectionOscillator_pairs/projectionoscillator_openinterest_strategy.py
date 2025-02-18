import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
