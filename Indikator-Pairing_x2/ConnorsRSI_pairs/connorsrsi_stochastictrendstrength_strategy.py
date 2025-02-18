import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
