import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und GannSquares
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'GannSquares': 1.0
        })
    )
