import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VWAPBands
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VWAPBands': 1.0
        })
    )
