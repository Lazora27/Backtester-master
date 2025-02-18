import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
