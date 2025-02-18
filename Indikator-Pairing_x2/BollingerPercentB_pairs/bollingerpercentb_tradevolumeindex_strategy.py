import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
