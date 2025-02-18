import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
