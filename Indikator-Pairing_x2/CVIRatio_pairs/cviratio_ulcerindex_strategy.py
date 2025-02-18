import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'UlcerIndex': 1.0
        })
    )
