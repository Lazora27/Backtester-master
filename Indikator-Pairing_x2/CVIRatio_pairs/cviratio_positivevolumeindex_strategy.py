import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
