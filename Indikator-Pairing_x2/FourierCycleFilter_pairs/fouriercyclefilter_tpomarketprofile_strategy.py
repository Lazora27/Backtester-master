import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
