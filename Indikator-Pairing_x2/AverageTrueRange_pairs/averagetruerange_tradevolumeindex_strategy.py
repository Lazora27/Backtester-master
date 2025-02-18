import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
