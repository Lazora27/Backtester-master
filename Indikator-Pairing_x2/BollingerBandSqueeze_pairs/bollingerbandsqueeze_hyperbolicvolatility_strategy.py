import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
