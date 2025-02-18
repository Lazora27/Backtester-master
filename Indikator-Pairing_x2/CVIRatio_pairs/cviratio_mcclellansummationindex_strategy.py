import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
