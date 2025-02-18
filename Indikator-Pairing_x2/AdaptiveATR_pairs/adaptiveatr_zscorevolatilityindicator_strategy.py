import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_ZScoreVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und ZScoreVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'ZScoreVolatilityIndicator': 1.0
        })
    )
