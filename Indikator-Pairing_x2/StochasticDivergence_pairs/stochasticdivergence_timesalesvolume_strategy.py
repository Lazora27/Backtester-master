import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
