import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
