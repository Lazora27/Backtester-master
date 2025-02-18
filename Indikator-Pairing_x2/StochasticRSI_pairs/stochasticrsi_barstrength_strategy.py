import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BarStrength
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BarStrength': 1.0
        })
    )
