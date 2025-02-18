import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TapeReading
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TapeReading': 1.0
        })
    )
