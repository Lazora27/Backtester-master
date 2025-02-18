import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TickIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TickIndex': 1.0
        })
    )
