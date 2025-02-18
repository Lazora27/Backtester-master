import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
