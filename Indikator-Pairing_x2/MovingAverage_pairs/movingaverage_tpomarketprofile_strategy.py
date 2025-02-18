import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
