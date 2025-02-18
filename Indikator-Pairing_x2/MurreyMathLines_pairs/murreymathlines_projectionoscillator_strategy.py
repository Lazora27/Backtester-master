import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
