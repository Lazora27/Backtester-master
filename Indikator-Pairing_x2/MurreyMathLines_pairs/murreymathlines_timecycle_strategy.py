import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'TimeCycle': 1.0
        })
    )
