import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MurreyMathLines': 1.0
        })
    )
