import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
