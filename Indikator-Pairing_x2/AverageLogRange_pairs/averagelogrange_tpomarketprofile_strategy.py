import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
