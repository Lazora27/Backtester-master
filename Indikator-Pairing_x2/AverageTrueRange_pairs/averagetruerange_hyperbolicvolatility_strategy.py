import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
