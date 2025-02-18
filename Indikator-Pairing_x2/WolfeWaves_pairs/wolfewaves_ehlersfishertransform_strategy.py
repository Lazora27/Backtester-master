import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
