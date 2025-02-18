import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WolfeWaves': 1.0
        })
    )
