import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
