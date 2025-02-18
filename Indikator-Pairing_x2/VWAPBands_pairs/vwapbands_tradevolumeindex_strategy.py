import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
