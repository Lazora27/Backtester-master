import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ParabolicSAR': 1.0
        })
    )
