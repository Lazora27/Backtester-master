import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'WolfeWaves': 1.0
        })
    )
