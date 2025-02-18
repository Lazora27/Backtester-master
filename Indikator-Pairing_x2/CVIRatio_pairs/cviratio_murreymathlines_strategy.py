import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MurreyMathLines': 1.0
        })
    )
