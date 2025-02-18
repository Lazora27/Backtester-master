import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
