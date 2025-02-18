import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedAverageTrueRange_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedAverageTrueRange und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'NormalizedAverageTrueRange': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
