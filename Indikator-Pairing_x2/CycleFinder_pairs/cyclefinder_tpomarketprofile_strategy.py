import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
