import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
