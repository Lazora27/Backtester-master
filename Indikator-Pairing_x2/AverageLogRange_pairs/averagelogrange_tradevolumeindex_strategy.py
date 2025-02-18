import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
