import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'AverageTrueRange': 1.0
        })
    )
