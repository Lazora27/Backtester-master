import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MurreyMathLines': 1.0
        })
    )
