import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
