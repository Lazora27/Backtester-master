import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
