import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
