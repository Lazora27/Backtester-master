import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und GannAngles
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'GannAngles': 1.0
        })
    )
