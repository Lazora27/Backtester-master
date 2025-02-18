import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ConnorsRSI': 1.0
        })
    )
