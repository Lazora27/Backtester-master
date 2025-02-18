import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'GannSquareReversal': 1.0
        })
    )
