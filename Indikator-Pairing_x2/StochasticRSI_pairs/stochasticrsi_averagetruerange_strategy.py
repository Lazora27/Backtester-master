import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AverageTrueRange': 1.0
        })
    )
