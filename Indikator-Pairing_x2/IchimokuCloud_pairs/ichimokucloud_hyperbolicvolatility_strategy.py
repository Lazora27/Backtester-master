import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
