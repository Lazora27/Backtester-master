import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
