import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
