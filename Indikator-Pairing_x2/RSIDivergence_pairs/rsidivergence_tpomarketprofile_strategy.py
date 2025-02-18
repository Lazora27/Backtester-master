import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
