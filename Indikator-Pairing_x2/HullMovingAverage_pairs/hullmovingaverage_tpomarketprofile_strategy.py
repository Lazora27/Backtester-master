import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
