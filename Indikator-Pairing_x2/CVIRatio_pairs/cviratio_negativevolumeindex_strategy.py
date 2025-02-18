import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
