import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
