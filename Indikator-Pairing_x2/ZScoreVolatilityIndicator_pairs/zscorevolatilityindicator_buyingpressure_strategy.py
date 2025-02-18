import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZScoreVolatilityIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZScoreVolatilityIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ZScoreVolatilityIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
