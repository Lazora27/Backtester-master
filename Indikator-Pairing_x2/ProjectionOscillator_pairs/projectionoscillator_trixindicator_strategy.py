import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'TRIXIndicator': 1.0
        })
    )
