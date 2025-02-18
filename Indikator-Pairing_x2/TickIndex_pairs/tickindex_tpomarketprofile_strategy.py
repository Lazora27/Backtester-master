import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
