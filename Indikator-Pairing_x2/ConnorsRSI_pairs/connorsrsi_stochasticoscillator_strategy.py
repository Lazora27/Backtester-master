import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'StochasticOscillator': 1.0
        })
    )
