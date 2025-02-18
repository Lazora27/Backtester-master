import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
