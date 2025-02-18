import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
