import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_ZScoreVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und ZScoreVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'ZScoreVolatilityIndicator': 1.0
        })
    )
