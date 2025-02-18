import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
