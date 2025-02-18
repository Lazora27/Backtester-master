import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ProjectionBands': 1.0
        })
    )
