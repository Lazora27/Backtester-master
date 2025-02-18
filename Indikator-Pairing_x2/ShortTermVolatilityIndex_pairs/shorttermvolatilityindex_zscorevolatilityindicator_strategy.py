import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ShortTermVolatilityIndex_ZScoreVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ShortTermVolatilityIndex und ZScoreVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            },
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            }
        }),
        ('weights', {
            'ShortTermVolatilityIndex': 1.0,
            'ZScoreVolatilityIndicator': 1.0
        })
    )
