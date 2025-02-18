import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
