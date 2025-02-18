import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'PhaseDivergence': 1.0
        })
    )
