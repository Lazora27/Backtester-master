import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VolatilityIndex': 1.0
        })
    )
