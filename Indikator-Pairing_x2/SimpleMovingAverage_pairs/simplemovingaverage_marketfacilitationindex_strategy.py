import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
