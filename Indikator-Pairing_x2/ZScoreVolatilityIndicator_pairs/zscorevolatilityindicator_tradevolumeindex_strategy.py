import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZScoreVolatilityIndicator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZScoreVolatilityIndicator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ZScoreVolatilityIndicator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
