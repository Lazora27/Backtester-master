import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AccelerationBands': 1.0
        })
    )
