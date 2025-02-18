import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
