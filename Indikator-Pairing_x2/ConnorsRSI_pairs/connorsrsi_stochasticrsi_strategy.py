import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'StochasticRSI': 1.0
        })
    )
