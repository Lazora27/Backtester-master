import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TapeReading
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TapeReading': 1.0
        })
    )
