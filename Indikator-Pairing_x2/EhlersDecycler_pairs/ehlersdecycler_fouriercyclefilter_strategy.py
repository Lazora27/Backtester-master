import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
