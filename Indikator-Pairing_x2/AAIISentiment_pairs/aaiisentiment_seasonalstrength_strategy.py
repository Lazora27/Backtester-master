import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SeasonalStrength': 1.0
        })
    )
