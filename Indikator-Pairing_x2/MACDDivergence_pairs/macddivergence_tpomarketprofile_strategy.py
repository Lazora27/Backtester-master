import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
