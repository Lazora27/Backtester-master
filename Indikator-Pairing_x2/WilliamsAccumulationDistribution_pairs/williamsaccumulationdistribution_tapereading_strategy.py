import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsAccumulationDistribution_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsAccumulationDistribution und TapeReading
    """
    
    params = (
        ('indicators', {
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'WilliamsAccumulationDistribution': 1.0,
            'TapeReading': 1.0
        })
    )
