import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'WolfeWaves': 1.0
        })
    )
