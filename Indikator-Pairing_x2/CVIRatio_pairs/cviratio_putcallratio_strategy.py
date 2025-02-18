import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PutCallRatio': 1.0
        })
    )
