import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MurreyMathLines': 1.0
        })
    )
