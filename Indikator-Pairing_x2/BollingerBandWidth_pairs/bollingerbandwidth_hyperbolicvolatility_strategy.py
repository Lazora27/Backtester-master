import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
