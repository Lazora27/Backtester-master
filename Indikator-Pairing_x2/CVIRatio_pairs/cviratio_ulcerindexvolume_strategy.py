import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
