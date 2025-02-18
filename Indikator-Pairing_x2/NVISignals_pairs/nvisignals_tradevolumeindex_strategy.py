import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
