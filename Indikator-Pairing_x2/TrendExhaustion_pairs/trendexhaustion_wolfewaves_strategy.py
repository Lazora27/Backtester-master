import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'WolfeWaves': 1.0
        })
    )
