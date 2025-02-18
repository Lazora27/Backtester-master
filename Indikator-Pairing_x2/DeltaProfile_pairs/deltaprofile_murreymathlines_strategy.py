import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MurreyMathLines': 1.0
        })
    )
