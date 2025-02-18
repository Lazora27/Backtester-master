import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CyberCycle
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CyberCycle': 1.0
        })
    )
