import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und GannFans
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'GannFans': 1.0
        })
    )
