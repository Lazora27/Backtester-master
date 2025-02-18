import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MurreyMathLines': 1.0
        })
    )
