import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
