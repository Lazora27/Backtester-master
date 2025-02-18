import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'SeasonalStrength': 1.0
        })
    )
