import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
