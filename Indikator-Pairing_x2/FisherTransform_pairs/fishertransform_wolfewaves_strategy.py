import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WolfeWaves': 1.0
        })
    )
