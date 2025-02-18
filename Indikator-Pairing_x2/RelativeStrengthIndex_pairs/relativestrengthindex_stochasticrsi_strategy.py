import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
