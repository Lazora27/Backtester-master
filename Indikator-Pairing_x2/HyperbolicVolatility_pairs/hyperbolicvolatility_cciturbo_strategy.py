import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'CCITurbo': 1.0
        })
    )
