import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
