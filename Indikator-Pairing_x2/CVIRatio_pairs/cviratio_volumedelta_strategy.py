import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VolumeDelta': 1.0
        })
    )
