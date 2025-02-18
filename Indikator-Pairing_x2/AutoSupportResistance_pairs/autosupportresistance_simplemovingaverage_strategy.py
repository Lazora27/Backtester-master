import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
