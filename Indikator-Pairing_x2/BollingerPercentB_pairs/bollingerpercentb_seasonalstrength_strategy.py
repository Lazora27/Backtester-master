import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'SeasonalStrength': 1.0
        })
    )
