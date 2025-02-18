import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
