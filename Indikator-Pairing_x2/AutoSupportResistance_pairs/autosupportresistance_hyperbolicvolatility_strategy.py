import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
