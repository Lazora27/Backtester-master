import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
