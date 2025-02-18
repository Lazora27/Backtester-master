import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AverageTrueRange': 1.0
        })
    )
