import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
