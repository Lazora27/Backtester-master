import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'CCITurbo': 1.0
        })
    )
