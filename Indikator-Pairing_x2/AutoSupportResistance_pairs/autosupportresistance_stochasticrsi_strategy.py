import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'StochasticRSI': 1.0
        })
    )
