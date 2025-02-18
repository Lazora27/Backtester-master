import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'TapeReading': 1.0
        })
    )
