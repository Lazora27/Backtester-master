import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
