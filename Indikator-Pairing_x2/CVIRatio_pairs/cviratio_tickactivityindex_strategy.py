import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TickActivityIndex': 1.0
        })
    )
