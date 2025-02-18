import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'IchimokuCloud': 1.0
        })
    )
