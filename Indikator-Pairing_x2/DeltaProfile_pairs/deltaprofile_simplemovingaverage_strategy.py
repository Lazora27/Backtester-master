import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
