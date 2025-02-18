import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
