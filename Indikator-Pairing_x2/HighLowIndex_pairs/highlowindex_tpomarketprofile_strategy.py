import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
