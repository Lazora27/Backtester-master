import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSIMomentum_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSIMomentum und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ConnorsRSIMomentum': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
