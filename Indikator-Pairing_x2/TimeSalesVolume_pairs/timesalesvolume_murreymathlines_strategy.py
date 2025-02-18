import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'MurreyMathLines': 1.0
        })
    )
