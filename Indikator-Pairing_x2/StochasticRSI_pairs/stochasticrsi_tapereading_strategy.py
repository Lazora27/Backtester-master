import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TapeReading
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TapeReading': 1.0
        })
    )
