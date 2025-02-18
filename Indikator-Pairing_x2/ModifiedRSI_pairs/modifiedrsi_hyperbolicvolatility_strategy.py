import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
