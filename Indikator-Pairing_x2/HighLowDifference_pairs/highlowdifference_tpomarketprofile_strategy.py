import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
